# Azure Skills Profile — AZ-900 & AZ-104

## AZ-900: Microsoft Azure Fundamentals
**Source:** John Savill’s Technical Training — *AZ-900 Full 8.5-hour Course Playlist*  
**Focus:** Cloud architecture fundamentals, Azure service landscape, security, governance, pricing, and support.

### Cloud Concepts and Shared Responsibility
- Explain IaaS, PaaS, and SaaS and select the appropriate model for a workload.
- Explain public, private, and hybrid cloud deployment models and their trade-offs.
- Apply the shared responsibility model across infrastructure, platform, and software services.
- Explain elasticity, scalability, high availability, fault tolerance, disaster recovery, and reliability.
- Compare capital expenditure (CapEx) and operational expenditure (OpEx) in cloud consumption.
- Describe consumption-based pricing, pay-as-you-go, reserved capacity, and cloud economics.

### Core Azure Architecture
- Describe Azure regions, availability zones, region pairs, and geography-based data residency.
- Select between availability sets and availability zones for VM resilience.
- Explain Azure resource hierarchy: management groups, subscriptions, resource groups, and resources.
- Use Azure Resource Manager (ARM) as the deployment and management layer.
- Describe resource providers, resource IDs, deployment stacks, and ARM template deployment concepts.
- Use the Azure portal, Azure CLI, Azure PowerShell, Cloud Shell, and Azure mobile app for administration.

### Compute Services
- Select between Azure Virtual Machines, VM Scale Sets, Azure App Service, Azure Functions, Azure Container Instances, and Azure Kubernetes Service (AKS).
- Explain serverless computing and event-driven execution with Azure Functions.
- Describe containers, images, orchestration, and the role of Azure Container Registry.
- Explain Azure Virtual Desktop and Azure Batch for virtual desktops and large-scale parallel workloads.
- Describe when to use Azure VMware Solution, Azure Dedicated Host, and Azure Stack for specialized hosting scenarios.

### Networking Services
- Explain Azure Virtual Networks (VNets), subnets, private IP addressing, and public IP addresses.
- Describe VNet peering, VPN Gateway, ExpressRoute, and hybrid connectivity patterns.
- Use Azure DNS, Azure Load Balancer, Application Gateway, Traffic Manager, and Azure Front Door for traffic distribution.
- Explain Azure Bastion, Network Security Groups (NSGs), Azure Firewall, and DDoS Protection.
- Describe Azure Virtual WAN and Azure Network Watcher for connectivity and diagnostics.

### Storage Services
- Select between Azure Blob Storage, Azure Files, Azure Disk Storage, Azure Queues, and Azure Tables.
- Explain storage access tiers: Hot, Cool, Cold, and Archive.
- Describe storage redundancy options: LRS, ZRS, GRS, GZRS, and read-access GRS/GZRS.
- Use shared access signatures (SAS), storage account keys, and Microsoft Entra ID-based access for securing storage.
- Explain Azure Storage Explorer, AzCopy, Azure File Sync, and Azure Data Box for data movement.
- Describe managed disks, disk types, snapshots, and storage encryption.

### Database and Analytics Services
- Differentiate relational and non-relational database workloads.
- Describe Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs.
- Explain Azure Database for PostgreSQL, MySQL, and MariaDB.
- Describe Cosmos DB, Azure Cache for Redis, Azure Table Storage, and Azure Data Lake Storage.
- Explain Azure Synapse Analytics, Azure Databricks, Azure Data Factory, Azure HDInsight, and Azure Analysis Services.
- Describe Azure AI services, Azure Machine Learning, Azure Cognitive Search, and Azure AI Bot Service at a fundamental level.

### Identity, Access, and Security
- Describe Microsoft Entra ID (formerly Azure Active Directory), tenants, users, groups, and device identity.
- Explain authentication versus authorization and the role of Microsoft Entra ID in each.
- Use Multi-Factor Authentication (MFA), Conditional Access, and self-service password reset (SSPR).
- Explain Single Sign-On (SSO), external identities, and Microsoft Entra External ID.
- Apply Role-Based Access Control (RBAC) with roles, security principals, scopes, and role assignments.
- Describe Zero Trust, defense in depth, encryption at rest and in transit, Microsoft Defender for Cloud, and Microsoft Sentinel.
- Explain Microsoft Entra ID Governance, Microsoft Entra Permissions Management, and Microsoft Entra Verified ID at a conceptual level.

### Governance, Compliance, and Cost Management
- Use Azure Policy to enforce organizational standards and remediate non-compliant resources.
- Use resource locks, tags, and resource groups for governance and organization.
- Describe Azure Blueprints, Microsoft Purview, and Service Trust Portal for compliance and governance.
- Interpret Azure pricing, Total Cost of Ownership (TCO) Calculator, and Pricing Calculator.
- Use Azure Cost Management + Billing, budgets, alerts, and Azure Advisor cost recommendations.
- Explain support plans, Azure Service Health, and creating Azure support requests.

---

## AZ-104: Microsoft Azure Administrator
**Source:** Official Microsoft Learn AZ-104 learning paths and the current AZ-104 skills-measured study guide.  
**Focus:** Hands-on administration of identity, governance, storage, compute, virtual networking, monitoring, backup, and disaster recovery.

### Azure Administration Prerequisites
- Administer Azure using the Azure portal, Azure PowerShell, Azure CLI, and Azure Cloud Shell.
- Write and deploy JSON-based ARM templates using Visual Studio Code.
- Apply PowerShell fundamentals for task automation and configuration management.
- Understand Azure resource hierarchy, ARM deployments, resource providers, and infrastructure-as-code principles.
- Use Azure Cloud Shell for interactive command-line administration from a browser.

### Identity and Governance
- Create and manage Microsoft Entra ID users, groups, administrative units, and user properties.
- Manage group membership, dynamic groups, and group-based licensing.
- Configure external user access, guest invitations, and collaboration restrictions.
- Configure and validate self-service password reset (SSPR).
- Assign built-in Azure RBAC roles at management group, subscription, resource group, and resource scopes.
- Interpret effective permissions, role assignments, deny assignments, and access-review results.
- Create and manage management groups, subscriptions, resource groups, and resource moves.
- Author, assign, and manage Azure Policy definitions, initiatives, exemptions, and remediation tasks.
- Apply and manage resource tags for cost allocation, automation, and governance.
- Configure resource locks to prevent accidental deletion or modification.
- Manage costs using budgets, cost alerts, Azure Advisor recommendations, and Cost Management views.

### Storage Administration
- Create and configure General Purpose v2 storage accounts, performance tiers, and access tiers.
- Configure storage redundancy: LRS, ZRS, GRS, GZRS, RA-GRS, and RA-GZRS.
- Configure storage account firewalls, virtual-network rules, private endpoints, and trusted Microsoft services.
- Generate and use account SAS, service SAS, and user delegation SAS tokens.
- Configure stored access policies and rotate or revoke storage account keys.
- Configure identity-based access for Azure Files using Microsoft Entra Kerberos or Microsoft Entra Domain Services.
- Manage data with Azure Storage Explorer and AzCopy.
- Create and configure Azure Files shares, snapshots, soft delete, and share-level permissions.
- Create Blob containers, configure public access levels, and manage blob metadata.
- Configure blob lifecycle-management policies to transition or delete data across Hot, Cool, Cold, and Archive tiers.
- Configure blob versioning, point-in-time restore, soft delete, immutable storage, and object replication.
- Configure encryption with Microsoft-managed keys and customer-managed keys in Azure Key Vault.

### Compute and Virtual Machines
- Create Windows and Linux virtual machines from the portal, CLI, PowerShell, and ARM/Bicep templates.
- Select and resize VM sizes based on CPU, memory, storage, GPU, and workload requirements.
- Configure VM availability using availability sets, availability zones, and fault/update domains.
- Configure OS disks, data disks, disk caching, managed disk types, snapshots, and disk encryption.
- Configure encryption at host for Azure virtual machines.
- Move VMs between resource groups, subscriptions, and regions.
- Configure VM networking, NICs, IP configurations, network security rules, and diagnostics.
- Deploy and manage Virtual Machine Scale Sets, including scaling rules, instance protection, and rolling upgrades.
- Use Azure Backup for VM protection and Azure Site Recovery for regional failover.
- Troubleshoot VM boot, performance, connectivity, and extension-related issues.

### Containers and App Service
- Create and manage Azure Container Registry, including image push/pull and registry security.
- Provision and scale containers using Azure Container Instances.
- Deploy containerized applications using Azure Container Apps, including scaling and environment configuration.
- Create App Service plans and select appropriate pricing tiers for scaling and features.
- Create, deploy, and configure web apps in Azure App Service.
- Configure autoscaling rules, deployment slots, continuous deployment, and app settings.
- Configure custom domains, managed certificates, TLS/SSL bindings, and HTTPS-only access.
- Configure App Service networking, including virtual-network integration, private endpoints, and access restrictions.
- Configure App Service backups and restore operations.

### Infrastructure as Code with ARM and Bicep
- Interpret ARM template structure: parameters, variables, resources, outputs, and functions.
- Modify existing ARM templates to change resource properties, add resources, or parameterize deployments.
- Interpret and modify Bicep files, including modules, parameters, variables, resource declarations, and outputs.
- Deploy resources using ARM templates and Bicep through the portal, Azure CLI, PowerShell, and deployment pipelines.
- Export an existing resource group or deployment as an ARM template.
- Convert ARM JSON templates to Bicep and use Bicep for repeatable, consistent infrastructure deployment.

### Virtual Networking
- Create and configure VNets, subnets, address spaces, and IP addressing.
- Create and configure public IP addresses, including SKU selection and allocation methods.
- Configure VNet peering, including global peering, gateway transit, and service chaining.
- Create and manage route tables and user-defined routes (UDRs) to control traffic flow.
- Troubleshoot network connectivity using effective routes, IP flow verify, and Network Watcher.
- Create and configure Network Security Groups (NSGs), application security groups (ASGs), and security rules.
- Evaluate effective security rules and diagnose NSG rule precedence and conflicts.
- Deploy and use Azure Bastion for secure VM access without public RDP/SSH exposure.
- Configure service endpoints and private endpoints for Azure PaaS services.
- Configure Azure DNS zones, records, custom DNS, and DNS resolution for private endpoints.
- Configure internal and public Azure Load Balancers, health probes, backend pools, and load-balancing rules.
- Troubleshoot load-balancing behavior and backend health.
- Understand when to use Application Gateway, Azure Front Door, and Traffic Manager for advanced traffic distribution.

### Monitoring and Operational Health
- Interpret platform metrics in Azure Monitor and create metric-based alerts.
- Configure diagnostic settings to route logs and metrics to Log Analytics, Storage, and Event Hubs.
- Query and analyze logs using Kusto Query Language (KQL) in Azure Monitor Log Analytics.
- Create alert rules, action groups, and alert-processing rules for automated incident response.
- Use VM insights, Storage insights, and Network insights to interpret resource health and performance.
- Use Azure Network Watcher, Connection Monitor, and connection troubleshooting tools.
- Monitor application and infrastructure availability using Azure Monitor and Azure Service Health.
- Configure Azure Monitor Workbooks and dashboards for operational visibility.

### Backup and Disaster Recovery
- Create and configure Recovery Services vaults and Azure Backup vaults.
- Create and configure backup policies for VMs, Azure Files, Azure Blobs, and databases.
- Perform on-demand backups, scheduled backups, and restore operations using Azure Backup.
- Restore VMs, files, folders, and storage data using appropriate recovery options.
- Configure soft delete, security PINs, and backup-reporting alerts.
- Configure Azure Site Recovery for Azure-to-Azure disaster recovery.
- Perform planned and unplanned failover to a secondary region using Azure Site Recovery.
- Configure recovery plans, replication health, RPO/RTO awareness, and failback operations.
- Interpret backup reports and configure backup-related alerts.