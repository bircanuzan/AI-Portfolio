# Azure Foundry / OpenAI / LangChain / n8n / Databricks / Fabric — execution runbook

The scripts in `integrations/` are **optional real-service adapters**. They are not proof of account provisioning, live service invocation, Azure deployment, n8n flow execution, data residency compliance, or production quality. Charges may apply.

## A. Local first (no cost and no credentials)
```
python run_lab.py ingest
python run_lab.py ask --query "What is our annual leave policy?"
python run_lab.py eval
python -m unittest discover -s tests -v
```

## B. OpenAI API + LangChain (needs credentials, may incur costs)
```
python -m pip install -r requirements-optional.txt
# Set OPENAI_API_KEY using secure local environment/secrets vault; never commit the value
python integrations/openai_langchain.py embed
python integrations/openai_langchain.py ask --semantic --query "What is the annual leave policy?"
```
This invokes LangChain's `OpenAIEmbeddings` to create neural vectors stored in local SQLite and `ChatOpenAI` via a grounded prompt chain. It cannot be classified as successful until real outputs, model ID, source text and independent scoring are captured. Real LLM answers may still be wrong despite prompt instructions.

## C. Microsoft Foundry hosted agent (Azure billing and access)
Prerequisites: Foundry resource/project, a model deployment, appropriate `Foundry User`/project RBAC, `az login` or managed identity, `AZURE_AI_PROJECT_ENDPOINT`, `AZURE_AI_MODEL_DEPLOYMENT_NAME`. Microsoft's **current 2.x SDK** (`azure-ai-projects>=2.3.0`) is used. Provisioning **creates** an Azure agent; treat the flags as an intentional billable operation.
```
python integrations/azure/foundry_agent.py provision --agent-name hr-service-agent-lab --confirm-billable-azure
python integrations/azure/foundry_agent.py ask --agent-name hr-service-agent-lab --query "What is our annual leave policy?" --confirm-billable-azure
```
Version creation, hosted invocation and cleanup must be validated against the tenant/SDK version. Save *redacted* agent name/version, endpoint region, model deployment, response ID, timestamp, usage, reviewer score and deprovision proof. Do not grant access to real HR files.

Official reference: https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview and https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/agents-overview .

## D. n8n workflow (import candidate, NOT run)
Use n8n **on the same local machine** as the Python API because the template points to `127.0.0.1:8000`. Import `integrations/n8n/hr_agent_intake_workflow.json` through the n8n UI, inspect and repair node versions as needed, run `python run_lab.py serve`, then exercise the test webhook with `{"query":"What is the annual leave policy?"}` and save n8n execution ID, timestamps and returned JSON. If n8n is inside Docker, `127.0.0.1` points to the container, **not the host**: design a private authenticated network bridge before testing; do not simply expose the unauthenticated lab API to the internet. Human approval remains a **local queue status**, not a linked Teams approval.

Official n8n import reference: https://docs.n8n.io/workflows/export-import/ .

## E. PySpark / Databricks (not run)
In a Databricks development workspace, upload synthetic `data/policies.json`, configure least-privilege Unity Catalog access and run `integrations/databricks/pyspark_policy_etl.py` as a job/notebook, passing the JSON input path and Delta silver/quarantine paths. Validate `count`, nulls, duplicates, schema evolution, effective-date logic, reruns, access control and observed cluster cost. No Databricks pipeline has been executed in this project.

## F. Microsoft Fabric (architecture mapping only)
OneLake/ADLS landing zone → Dataflow Gen2 or Fabric Spark Notebook validation → Lakehouse Delta Silver → Warehouse/service semantic model → Power BI quality and SLA metrics; sync policy index to Azure AI Search or a project-managed vector index. No workspace, connector, lakehouse, dataflow or Fabric result currently exists.

## G. Deployment/LLMOps for production (future)
API Management identity policies, Container Apps/AKS readiness probes, managed secrets, VNet/Private Link, event-driven queue (Service Bus), approvals, observability (OpenTelemetry/Azure Monitor), reproducible container builds/SBOM, branch policies, CI tests, CD sandbox approvals, regression and live safety gates. Document actual runtime, tokens/100 requests, p95 latency, cost and outages; never infer production scalability from local SQLite tests.
