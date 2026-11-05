# HR Operations Automation Agent

## Goal
Classify HR requests, retrieve policy, execute permitted workflow steps and escalate exceptions with an audit trail.

## Trigger
A validated HR event, request, planning cycle, or authorised user instruction relevant to this agent.

## Approved inputs
- Service request
- Approved service catalogue
- Policy knowledge
- Workflow state

## Knowledge / RAG
Retrieve only from approved, access-controlled HR knowledge and validated analytical sources. Return source references where available.

## Reasoning / orchestration
1. Validate request and required inputs.
2. Retrieve relevant approved evidence.
3. Determine whether the task is deterministic, AI-assisted, or requires human judgement.
4. Use permitted tools only.
5. Stop and escalate when evidence is missing, conflicting, sensitive, or outside scope.
6. Prepare a traceable output and record actions.

## Permitted tools / actions
- Intent classification
- Knowledge retrieval
- Workflow execution
- Case update
- Notification

## Human checkpoint
HR approves sensitive/high-impact cases and handles exceptions.

## Exception handling
Do not guess. State the missing/uncertain evidence, preserve current workflow state, and route to the accountable HR role.

## Audit trail
Record request ID, approved sources, tool actions, generated output, human approval/override, exception path and final status.

## Evaluation measures
- Classification accuracy
- Workflow success
- Escalation accuracy
- SLA improvement
- Audit completeness
