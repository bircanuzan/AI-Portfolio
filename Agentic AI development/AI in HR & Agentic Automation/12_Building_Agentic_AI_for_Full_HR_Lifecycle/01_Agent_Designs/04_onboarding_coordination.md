# Onboarding Coordination Agent

## Goal
Coordinate approved onboarding actions, monitor completion, answer grounded questions and escalate delays.

## Trigger
A validated HR event, request, planning cycle, or authorised user instruction relevant to this agent.

## Approved inputs
- New-joiner workflow
- Approved onboarding content
- Task status

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
- Task creation
- Reminder workflow
- Knowledge retrieval
- Status summarization

## Human checkpoint
HR/manager resolves exceptions and approves employment-related changes.

## Exception handling
Do not guess. State the missing/uncertain evidence, preserve current workflow state, and route to the accountable HR role.

## Audit trail
Record request ID, approved sources, tool actions, generated output, human approval/override, exception path and final status.

## Evaluation measures
- On-time task completion
- Escalation precision
- FAQ grounding
- Overdue-action reduction
