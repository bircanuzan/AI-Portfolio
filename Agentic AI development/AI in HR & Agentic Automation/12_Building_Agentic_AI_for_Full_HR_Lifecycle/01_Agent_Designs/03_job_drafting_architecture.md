# Job Drafting & Job Architecture Agent

## Goal
Draft and quality-check job descriptions against approved job architecture, capability language and inclusive-writing rules.

## Trigger
A validated HR event, request, planning cycle, or authorised user instruction relevant to this agent.

## Approved inputs
- Approved role requirements
- Job-family framework
- Grade/level guidance
- Approved templates

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
- JD drafting
- Skills extraction
- Template validation
- Language quality checks

## Human checkpoint
HR/job owner approves job scope, level, accountabilities and final published description.

## Exception handling
Do not guess. State the missing/uncertain evidence, preserve current workflow state, and route to the accountable HR role.

## Audit trail
Record request ID, approved sources, tool actions, generated output, human approval/override, exception path and final status.

## Evaluation measures
- Template compliance
- Human edit rate
- Missing-requirement rate
- Architecture alignment
