<u>Stage 1 “Dockerize”:</u>

First : I build app image by multistage technique .

Second: I run continers of backend service like ( RDS:mysql on port 3306 , memcache port:11211 , rabbit mq port:5672, nginx as a loadbalncer).

third: make a docker-compose to run all services and checks it locally by put it in same network and open url to check all services synchronization.

<u>Stage 2 “Aws: IAAS”:</u>

First: I follow left and shift technique to convert my work from development to production by using IAAS .

Second : I build 5 instances for ( app , backend service, loadbalancer ) then build 3 security group to control the inbound and outbound networking and apply network policies .

Third: Pay a domain name from name.com and make a certification (TLS/SSL) to secure connection.

Forth : build router 53 to mange private connection between app and backend services also between backend services .

Five: build s3 bucket to store artifacts of my app and all files in it and make IAM role to app instance to connect S3 and IAM key pairs to connect my labtop by S3 also.

<u>Stage 3 “Rearchiticture on AWS “
“PASS”</u>

First :
 Use AWS RDS service to build mysql db then use AWSMQ to build rabbitmq service then use AWS memcache to build memcache service and make a security group include all these backend services .

Second:
 Use AWS elastic beanstalk to build and care of my app that using to create instance and security group and loadbalancing and cloudwatch ,bucket,router 53 all these service are building autamaticilly when I build elastic beanstalk.

<u>Third:</u>Use AWS cloudfront service to reduce latency

Forth:
Syncronize my domain with cloudfront to make traffic redirect to cloudfront by router 53.

<u>Stsge 4 : Jenkins CI Pipeline</u>

- Webhook integration (GitHub → Jenkins).

- Step 1: Code Test (JUnit + Jacoco)

- Step 2: Code Analysis (SonarScanner → SonarQube Server)

- Step 3: Build Artifact (Maven) + Publish to Nexus Repository

- Step 4: Slack Notification (CI Success)

<u>Stsge 5 : AWS Native CI Pipeline</u>

- Step 1 :Migrated from GitHub to Bitbucket (Source Control).

- Step 2: AWS CodeArtifact for Maven Dependencies.

- Step 3: AWS CodeBuild for Build + SonarCloud Analysis.

- Step 4: AWS CodePipeline for Orchestration.

- Step 5: S3 Bucket for Artifact Storage.

- Step 6: Fully Serverless CI/CD Pipeline.

<u>Stsge 6 : AWS CICD Pipeline</u>

- Step 1 :SCM Integration with GitHub Webhook

- Step 2 :Code Test (Maven + JUnit + Jacoco)

- Step 3 :Code Analysis (Checkstyle + SonarQube)

- Step 4 :Docker Build (Dockerfile → Image)

- Step 5 :Push to Amazon ECR

- Step 6 :ECS Deploy (Pull from ECR → Run Container)

- Step 7 :ALB + Auto Scaling

<u>Stage 7:Knowloge about building Kubernetes</u>.

<u>Stage 8 : Deploy App on EKS service (AWS)</u>

📌 What I Built:

I deployed all 5 services as Kubernetes manifests inside an Amazon EKS cluster:

step 1 :Tomcat (Application Server) — Deployment + Service + Ingress

step 2 :MySQL (Database) — Deployment + Service + PVC + StorageClass (Amazon EBS).

step 3 : Memcached (Cache) — Deployment + Service

step 4 : RabbitMQ (Message Broker) — Deployment + Service

step 5 : Secrets (DB Credentials) — Kubernetes Secret

📌 The Architecture:

Users → ALB → Ingress Controller → Tomcat Service → Tomcat Pod

↓

├─ RMQ Service → RabbitMQ Pod

├─ MC Service → Memcache Pod

└─ DB Service → DB Pod → PVC → EBS

<u></u>

<u></u>

<u>Stage 9 : Terraform — Infrastructure as Code</u>

### Stage 1: Remote State Bucket

**Goal:** Store Terraform's state in the cloud instead of on a local machine.

* Create an S3 bucket to hold terraform.tfstate (the "bucket with state of cloud" in the diagram).
* Point Terraform to it using backend.tf.
* Run terraform init to connect to the backend and download the AWS provider.

**Why:** The state file is Terraform's record of what it built. Keeping it in S3 lets a team share it and avoids losing it.

### Stage 2: Provider and Variables

**Goal:** Define where and how Terraform builds.

* Configure the AWS provider and region (us-east-1) in providers.tf.
* Keep configurable values (CIDR blocks, instance types, names) in variables.tf.

### Stage 3: VPC and Network Foundation

**Goal:** Build the isolated network from the diagram (vpc.tf).

* Create the **VPC** (the green box).
* Create **2 Availability Zones**, each with a **Public Subnet** and a **Private Subnet**.
* Attach the **Internet Gateway** to the VPC.

### Stage 4: Routing (Internet Gateway, NAT Gateways, Route Tables)

**Goal:** Control how traffic flows.

| **Component** | **Role** |
| --- | --- |
| Public route tables | Send internet traffic to the Internet Gateway |
| NAT Gateway (one per AZ) | Gives private subnets one-way outbound internet |
| Private route tables | Send outbound traffic to the NAT Gateway in the same AZ |

**Result:** Public subnets are reachable from the internet, and private subnets can reach out but cannot be reached.

### Stage 5: Security Groups

**Goal:** Add firewall rules per component (SecurityGroup.tf).

* **Bastion SG** (the red box): allows SSH only from trusted IPs.
* **App / Beanstalk SG:** allows web traffic.
* **Backend SG:** allows DB, cache, and messaging ports only from the app and bastion.

### Stage 6: SSH Key Pair

**Goal:** Create secure access credentials (keypair.tf).

* Generate vprofilekey (private) and vprofilekey.pub (public).
* Register the public key in AWS so instances can use it.

### Stage 7: Bastion Host

**Goal:** Create the only entry point to private resources (BastionHost.tf).

* Launch an EC2 instance in the **public subnet** with the Bastion Security Group and the key pair.
* Use it as a jump server: SSH to the Bastion, then to private resources.

### Stage 8: Backend Services (Private Subnets)

**Goal:** Provision the data layer (backend-services.tf).

* **MySQL database** (RDS) in the private subnets **(inferred)**.
* **Cache node** (ElastiCache) in the private subnets **(inferred)**.
* **RabbitMQ** message broker **(inferred)**, shown by the RabbitMQ button in your app.
* Add a **subnet group** so these services stay in the private subnets.

### Stage 9: Database Initialization

**Goal:** Prepare the database automatically.

* Use templates/db-deploy.tmpl to render a script that runs from the Bastion Host and loads the schema and data into MySQL.

**Proof:** The Users List page (Image 2 of your earlier screenshots) shows users loaded from the DB.

### Stage 10: Application Layer (Elastic Beanstalk)

**Goal:** Deploy the application in the private subnets.

* beans-app.tf: create the Beanstalk application.
* beans-ens.tf: create the environment (instances, load balancer, subnets, security groups).
* Deploy the app.

**Note:** In the diagram this layer is plain **EC2** servers. In your project it is **Elastic Beanstalk**, which manages the EC2 instances for you.

### Stage 11: Outputs

**Goal:** Print useful values after terraform apply (outputs.tf), such as the Bastion IP and service endpoints.

### Stage 12: Apply and Verify

**Goal:** Build everything and test it.

terraform init → terraform plan → terraform apply

| **Check** | **Evidence** |
| --- | --- |
| App is live | Beanstalk URL loads |
| DB connected | Users List page shows users |
| Login works | admin\_vp logs in successfully |
| Full app works | Welcome page, profile, posts, contacts |

### Summary: Diagram → Stage

| **Diagram element** | **Stage** |
| --- | --- |
| S3 bucket (state) | 1 |
| VPC, subnets, Internet Gateway | 3 |
| NAT Gateways, route tables | 4 |
| Bastion security group | 5 |
| Bastion Host | 7 |
| MySQL, Cache | 8 |
| EC2 app servers | 10 (Beanstalk) |

<u></u>

<u></u>

### <u>Phase 10: CI/CD Pipeline for EKS (GitLab + Terraform + Helm + SonarQube)</u> Pipeline 1: CI — Source Code Repo (Build, Test, Docker, Update Helm)

| **Stage** | **What Happens** |
| --- | --- |
| build | mvn clean install -DskipTests — compiles the app, artifact kept 1 hour |
| unit-test | mvn test — runs unit tests, publishes Surefire reports |
| checkstyle | mvn checkstyle:checkstyle — enforces code style rules |
| sonar-analysis | Runs SonarCloud scan (sources, JUnit, JaCoCo, checkstyle reports) |
| quality-gate | Polls SonarCloud's Quality Gate API (up to 12 retries) and fails the pipeline if the gate status is ERROR |
| docker-build | Builds the image via a **multistage Dockerfile**, tags it $CI\_COMMIT\_SHA, pushes to the GitLab Container Registry |
| update-deployment | Clones the **Helm Chart repo** using a token, updates app.image and app.tag in values.yaml with yq, commits and pushes back |

**Triggers:** main, merge\_requests, feature-y.

### Pipeline 2: Deploy Helm Chart Repo (Lint, Package, Deploy, Drift)

| **Stage** | **What Happens** |
| --- | --- |
| lint | helm lint on the chart — validates syntax before packaging |
| package | helm package — produces a .tgz artifact (kept 1 week) |
| deploy | Connects to EKS (aws eks update-kubeconfig), creates the vprofile namespace if missing, then helm upgrade --install with registry credentials injected as --set values |
| drift-check | Runs on a **schedule**: uses helm diff and a --dry-run upgrade to detect if the live cluster state has drifted from the chart in Git |

**Triggers:** main branch for deploy; scheduled pipeline for drift detection.

### Pipeline 3: EKS Infrastructure Pipeline (Terraform)

| **Stage** | **What Happens** |
| --- | --- |
| validate | terraform fmt -check + terraform validate on merge requests |
| plan | terraform plan with output saved as an artifact for review |
| apply | terraform apply — **manual gate** on main, blocked entirely when DESTROY\_MODE is true |
| drift-detection | Scheduled terraform plan -detailed-exitcode to catch infrastructure drift |
| notify | Sends **Slack notifications** for: drift detected/clean, pipeline failure (per failed stage), pipeline success |
| destroy | Fully manual, gated behind DESTROY\_MODE=true **and** a specific commit message (DESTROY\_CLUSTER) as a safety lock |

**State management:** Uses GitLab-managed remote state (TF\_HTTP\_ADDRESS pointing to the GitLab Terraform state API) with lock/unlock endpoints — this is the same state backend involved in the lock issue below.

### Cross-Cutting Setup: Kubernetes & Networking

* **EKS Cluster** provisioned by the Terraform pipeline above.
* **NGINX Ingress Controller** installed on the cluster to manage external traffic routing.
* **TLS/HTTPS** enabled by attaching a certificate ARN annotation to the Ingress resource, connecting it to the Load Balancer.
* App verified running via kubectl get pods -n vprofile — all 4 components (vproapp, vprodb, vpromc, vpromq01) Running 1/1.
* End-to-end verification: public Users List page, login, and full social-media UI functioning against the live EKS-hosted app.

## Troubleshooting Log (Real Incidents)

### 1. ImagePullBackOff — Wrong Registry Reference

**Root cause:** The image reference in the Helm values pointed to an incorrect container registry name, so the cluster had no valid credentials/path to pull the image and treated it as unauthorized access.
**Diagnosis:** kubectl describe pod (revealed the pull error and registry endpoint) and kubectl logs to confirm the container never started.
**Fix:** Corrected the registry name/path in the chart so the pull authenticated against the right repository.

### 2. Cross-Repo Automation via Deploy Tokens

**Setup:** Created a **GitLab Deploy Token** scoped to the Helm Chart repo, then stored it as protected CI/CD variables (CHARTS\_REPO\_TOKEN, CHARTS\_REPO\_URL) in the Source Code repo.
**Flow:** After docker-build pushes a new image, the update-deployment job clones the Helm repo over HTTPS using the token, updates app.image and app.tag via yq, and commits/pushes the change — fully automating the image tag bump without manual intervention.

### 3. HTTPS via Ingress + Certificate Annotation

Installed the **NGINX Ingress Controller** on the EKS cluster, then attached the certificate to the Ingress resource via an annotation referencing the certificate's ARN, linking it to the Load Balancer so the app serves over HTTPS.

### 4. Terraform State Lock

**Scenario:** A destroy job failed midway, leaving the remote state (stored via GitLab's Terraform state backend) **locked**. A later pipeline run (apply/build) failed with a lock error.
**Fix:** Manually released the lock from GitLab's Terraform state UI for the project, then re-ran the pipeline successfully.
**Lesson:** State locks after an interrupted run are expected — always check GitLab's state lock status before assuming corruption.

<u></u>

<u></u>

<u></u>

<u></u>

<u>Phase 11: Continuous Delivery & Configuration Management (Jenkins + Ansible + Nexus)</u>

This phase automates building, packaging, and deploying the VProfile application to a staging server using Jenkins as the CI/CD orchestrator, Nexus as the artifact repository, and Ansible for configuration management and deployment.

### Stage 1: Infrastructure & Access Setup

**Goal:** Prepare the servers and network access needed before any pipeline could run.

| **Task** | **Detail** |
| --- | --- |
| Jenkins server | Migrated from an old AWS EC2 instance to a new one; updated the GitHub webhook with the new Jenkins IP so build triggers kept working |
| App server | Launched a dedicated EC2 instance for app01-staging |
| Artifact repository | Launched and configured a dedicated **Nexus** server to host build artifacts |
| DNS | Created a Route53 record for app01-staging |
| Security Groups | Allowed port 22 (SSH) into App SG from Jenkins SG; allowed port 8081 into Nexus SG from App SG |
| Jenkins prerequisites | Installed Ansible on the Jenkins server, installed the Jenkins Ansible plugin, stored the app server's SSH login credentials in Jenkins Credentials, and configured a timestamp variable used for artifact/backup tagging during deployment |

### Stage 2: Source Control & Ansible Code Preparation

**Goal:** Set up a dedicated pipeline branch and bring in the deployment automation code.

* Created a separate branch in the source code repository specifically for the pipeline work.
* Copied the Ansible automation code from the vprofile-project reference repository into the team's own repository, then adapted it.

### Stage 3: Ansible Configuration Management Design

**Goal:** Build a reusable, OS-aware automation layer for installing Tomcat and deploying the app.

**site.yml** orchestrates two playbooks in order:

tomcat\_setup.yml → vpro-app-setup.yml

| **File** | **Responsibility** |
| --- | --- |
| tomcat\_setup.yml | Installs JDK 8 (conditional on CentOS vs Ubuntu), downloads Tomcat 8.5.37, creates a dedicated tomcat system user/group, extracts and syncs Tomcat into /usr/local/tomcat8, sets correct ownership, and installs the correct service file per OS family (epel7-svcfile.j2, epel6-svcfile.j2, ubuntu14\_15-svcfile.j2, ubuntu16-svcfile.j2), then starts and enables the service |
| vpro-app-setup.yml | Downloads the WAR artifact from Nexus using variables injected from Jenkins (nexusip, reponame, groupid, artifactid, build, vprofile\_version), stops Tomcat, archives the existing ROOT deployment with a timestamp before overwriting it, deploys the new WAR as ROOT.war, and restores the previous version through a rescue block if the deploy step fails, then restarts Tomcat |
| ansible.cfg | Disables host key checking and sets a 30s connection timeout, allowing the pipeline to SSH into new/unknown hosts without manual known\_hosts confirmation |
| stage.inventory | Defines the appsrvgrp host group pointing to the staging server's private IP, connecting as the ubuntu user |

The deployment logic follows a backup-before-overwrite and rescue/restore pattern, ensuring a failed WAR deployment does not leave the staging server in a broken state.

### Stage 4: Jenkins Pipeline Definition (Jenkinsfile)

**Goal:** Tie build, test, packaging, artifact upload, and deployment into a single automated pipeline.

| **Stage** | **What It Does** |
| --- | --- |
| **Build** | mvn -s settings.xml -DskipTests install, then archives the resulting .war as a Jenkins build artifact |
| **Test** | mvn -s settings.xml test |
| **Checkstyle Analysis** | mvn -s settings.xml checkstyle:checkstyle |
| **UploadArtifact** | Uses the nexusArtifactUploader plugin to push the built WAR to the Nexus release repository, versioned by the Jenkins BUILD\_ID |
| **Ansible Deploy to staging** | Runs the Jenkins ansiblePlaybook step against ansible/site.yml with ansible/stage.inventory, passing the Nexus artifact coordinates as extra vars so Ansible knows exactly which WAR to pull and deploy |

**Tooling:** Maven 3.9, JDK 17 (declared via the tools block).
**Notifications:** A post { always { ... } } block sends a Slack message to #jenkinscicd with the build result color-coded (green/red) and a link to the build.

Code quality is enforced through the Checkstyle stage. The pipeline moves directly from artifact upload to Ansible deployment on staging, without an intermediate integration or load testing stage.

### Stage 5: First Successful Pipeline Run (Verification)

**Goal:** Confirm the full pipeline works end-to-end.

**Evidence — Jenkins Build #13**, all stages green:

Checkout SCM → Tool Install → Build → Test → Checkstyle Analysis

→ UploadArtifact → Ansible Deploy to staging → Post Actions

* Ansible was invoked from the Jenkins workspace using a per-build generated private key, targeting ansible/site.yml and ansible/stage.inventory.
* The application was confirmed live and reachable on the staging server's login page after deployment.

### Stage 6: Production Deployment Approach

**Goal:** Promote the same automation to a production environment.

* Ansible code was updated on the prod branch.
* A new production server (app01-prod) was provisioned, with its own Route53 DNS record and inventory file.
* A dedicated production pipeline was created and tested in Jenkins.
* Production deployment is triggered by merging changes into the prod branch, and a fresh server is provisioned and deployed to directly for each release.

### Troubleshooting / Real Issues Solved

| **Issue** | **Root Cause** | **Resolution** |
| --- | --- | --- |
| **Jenkins build triggers stopped working after infrastructure change** | Jenkins was migrated from an aging AWS EC2 instance to a new one, changing its public IP; the GitHub webhook still pointed to the old IP | Updated the GitHub repository webhook configuration to the new Jenkins server IP, restoring automatic pipeline triggers on commit |

<u></u>

<u></u>