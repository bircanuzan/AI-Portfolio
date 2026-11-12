# Project 16 — Enterprise Voice AI Agent: Conversation Design, Integration Plan and QA

**Independent portfolio case study** inspired by the skills in ElevenLabs UAE Forward Deployed Software Engineer, Deployment Strategist and Adoption Strategist roles. Not affiliated with, commissioned by or deployed at ElevenLabs. No live ElevenAgents workspace or customer integration has been provisioned.

## Customer challenge
A fictional UAE enterprise has high-volume customer calls about general service availability, billing and application status. Prototype an AI-assisted conversation flow to answer only vetted general FAQs, avoid disclosure of individual case details, and transfer sensitive or unanswerable requests to humans.

## What the demonstration actually does
- Runnable deterministic Python conversation router with synthetic intents, an approved FAQ list and escalation decisions.
- Tests and a synthetic conversation-evaluation harness that can be executed locally.
- Solution architecture and proposed ElevenAgents integration, API tools, security controls and deployment checklist.
- Proposed QA across simulated conversation outcomes, next replies and tool-call permissions aligned with ElevenLabs agent-testing concepts.
- Customer discovery to pilot-to-scale lifecycle and enterprise outcome metrics.

## Getting started (offline, no account/key needed)
Python 3.10+ required, standard library only:
1. python src/agent.py
2. python src/evaluate.py
3. python -m unittest discover -s tests -v

## Files
- src/agent.py — rule-based FAQ/intent routing and guardrails (NOT a voice model or LLM)
- src/evaluate.py — read synthetic scenarios and report pass rates
- tests/test_agent.py — deterministic test coverage
- data/scenarios.json — synthetic conversation test cases
- docs/solution_architecture.md — voice integration and customer journey specification
- docs/enterprise_deployment_checklist.md — discovery, security, reliability and technical QA

## ElevenLabs product alignment
The proposed system would use ElevenAgents for speech-enabled conversations, a governed knowledge base, permitted server-side tools, human transfer and evaluations. The prototype DOES NOT create or administer ElevenLabs agents or handle real audio. See official ElevenLabs agent testing documentation: https://elevenlabs.io/docs/eleven-agents/customization/agent-testing

## Boundaries and risk management
No call recording, personal/customer data, credentials, live CRM access or autonomous HR decisions. All sample conversations are fictional. Any real voice deployment needs account configuration, consent, system authentication, provider terms, logging/privacy review, multilingual native-speaker QA and operational owners.

**CV-safe description:** "Designed an illustrative ElevenLabs-aligned enterprise voice-agent architecture, offline routing demo, synthetic conversation test harness and governance checklist." Do not present as professional production deployment.
