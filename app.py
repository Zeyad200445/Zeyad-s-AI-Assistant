# --- أولاً: تحميل المكتبات ---
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr
import json
from style import EXAMPLES, CSS, JS
# السطر ده بيقرا ملف الـ .env عشان ياخد المفتاح السري منه وميظهرش في الكود
load_dotenv(override=True) 
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

def push(message):
    print(f"Pushing notification: {message}")
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    requests.post(pushover_url, data=payload)

# بنفتح الاتصال مع سيرفرات OpenAI (هو اوتوماتيك بيدور على OPENAI_API_KEY اللي في ملف الـ env)
# --- ثانياً: فتح الاتصال مع OpenAI ---

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    max_retries=5,
)

# --- تجهيز الداتا للخطوة الثالثة ---
# 1. قراءة الـ CV بتاعك
reader = PdfReader("data/cv.pdf")
cv_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        cv_text += text

# 2. قراءة ملف الكورسات
with open("data/Devops-Course-RoadMap.md", "r", encoding="utf-8") as f:
    Devops_Course_RoadMap = f.read()
# قراءة ملف كورسات أزور
with open("data/azure_courses.md", "r", encoding="utf-8") as f:
    azure_courses = f.read()

with open("data/Outline-DevopsProjects-Course.md", "r", encoding="utf-8") as f:
    DevopsProjects = f.read()


# سطر للطباعة عشان لما نشغل الكود نتأكد إن كل حاجة تمام ومفيش errors في قراءة الملفات
print("Done! Reading all files and connect to openai be successfully ")


# --- Third: Setting Up the Agent Persona (System Prompt) ---

# The 'f' prefix before the quotation marks allows you to embed variables directly into the text.
system_prompt = f"""
# Your Role
You are the digital twin and intelligent agent for Zeyad, an engineer specializing in Cloud Engineering and DevOps.
Your task is to interact with HR representatives or technical managers who visit this application, answering their questions regarding Zeyad’s professional career, skills, and projects.
If asked who you are, clearly state that you are an AI assistant programmed by Zeyad to represent him.

# Available Information (Context)
Here are the details from Zeyad’s resume:
{cv_text}

And here are the details of the courses he has completed:
{Devops_Course_RoadMap}
{azure_courses}
{DevopsProjects}
# Rules
1. Be professional, polite, and concise in your responses. Speak on Zeyad’s behalf using the third person (e.g., "Zeyad has experience in...").
2. Use only the information provided in the resume and the list of courses.
3. Very important: If a user asks about something not covered in the provided information, politely apologize, state that you do not have that information, and suggest that they contact Zeyad directly.
4. Do not invent or fabricate any experiences, skills, or technologies that are not mentioned above.
5. Avoid answering any questions that fall outside the professional and technical scope.
If the user would like to get in touch, ask for their email, and use your tool to record their details.
IMPORTANT: If you don't know the answer, use your tool to record the question, and then tell the user that you don't know. Never make up an answer.
"""

# A line to confirm that the prompt is ready
print("Agent persona (System Prompt) has been set up.successfully!")







# --- Step 4: Tools Definition ---

# 1. The actual Python function that performs the task (saving the email)
def record_hr_email_tool(email):
    # Opens a file named hr_emails.txt inside the data folder and appends the email
    with open("data/hr_emails.txt", "a", encoding="utf-8") as f:
        f.write(email + "\n")
    return "Email recorded successfully"

# 2. The JSON schema that tells the AI what this tool is and when to use it
record_hr_email_tool_json = {
    "name": "record_hr_email_tool",
    "description": "Use this tool to record that a recruiter (HR) or user provided their email address to get in touch.",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "The email address of the recruiter or user"}
        },
        "required": ["email"],
        "additionalProperties": False
    }
}

def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"New lead! {name} wants to connect. Email: {email}. Notes: {notes}")
    return "OK"

def record_unknown_question(question):
    push(f"Unanswered question asked by user: {question}")
    return "OK"

record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "The email address of this user"},
            "name": {"type": "string", "description": "The user's name, if they provided it"},
            "notes": {"type": "string", "description": "Any additional info about the conversation that's worth recording"}
        },
        "required": ["email"],
        "additionalProperties": False
    }
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "The question that couldn't be answered"},
        },
        "required": ["question"],
        "additionalProperties": False
    }
}

tools = [
    {"type": "function", "function": record_user_details_json},
    {"type": "function", "function": record_unknown_question_json},
    {"type": "function", "function": record_hr_email_tool_json},
]

print("Tools defined successfully!")





# --- Elegant Tool Handler ---
def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called by AI: {tool_name}")
        
        # Using Python's built-in globals() to dynamically find and call the function
        tool = globals().get(tool_name)
        result = tool(**arguments) if tool else "No tool found"
        
        results.append({
            "role": "tool",
            "content": json.dumps(result),
            "tool_call_id": tool_call.id
        })
    return results




# --- Step 5 & 6: Chat Function and The Agent Loop ---
def chat(message, history):
    # 1. Prepare the context: System prompt + Previous history + New user message
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    
    # 2. First call to OpenAI (using Gemini model)
    response = client.chat.completions.create(model="gemini-3.5-flash", messages=messages, tools=tools)
    
    # 3. The Agent Loop: check if the model decided to call a tool
    while response.choices[0].finish_reason == "tool_calls":
        ai_message = response.choices[0].message
        tool_calls = ai_message.tool_calls
        
        # 4. Execute all requested tools elegantly using our helper function
        results = handle_tool_calls(tool_calls)
        
        # Append the AI's tool request message to the history
        messages.append(ai_message)
        # Append all the tool execution results to the history
        messages.extend(results)
        
        # 5. Second call to OpenAI with the updated context
        response = client.chat.completions.create(model="gemini-3.5-flash", messages=messages, tools=tools)
        
    # 6. Return the final text response
    return response.choices[0].message.content






# --- Step 7: Launching the Frontend Interface ---

print("Starting the AI Agent UI...")
# Create and launch the Gradio chat interface

gr.ChatInterface(
    chat,
    title="Zeyad's AI Assistant",
    description="Ask me anything about Zeyad's professional experience, skills, and courses.",
    examples=EXAMPLES,
).launch(inbrowser=True, css=CSS, js=JS)