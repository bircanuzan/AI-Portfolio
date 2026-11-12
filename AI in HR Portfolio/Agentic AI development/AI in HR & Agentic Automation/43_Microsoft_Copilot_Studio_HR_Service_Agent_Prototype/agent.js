/** HR Service Agent Lab v0.1.0 — offline, deterministic, no LLM or connector. */
"use strict";
const POLICY = {
  "hours": {
    "id": "HR-POL-001",
    "version": "0.1",
    "title": "Working Hours (laboratory sample)",
    "text": "Core collaboration time is 10:00–15:00 on scheduled workdays. Actual schedules depend on the employee's agreed working arrangement; HR confirms exceptions."
  },
  "leave": {
    "id": "HR-POL-002",
    "version": "0.1",
    "title": "Annual Leave (laboratory sample)",
    "text": "Annual leave requests go through the HR case team and require manager approval. Individual entitlements and balances must be checked by an authorised human."
  },
  "onboarding": {
    "id": "HR-POL-003",
    "version": "0.1",
    "title": "Onboarding (laboratory sample)",
    "text": "New joiners receive an induction checklist covering IT access, policy acknowledgement and a manager introduction. HR validates employment documentation privately."
  },
  "remote": {
    "id": "HR-POL-004",
    "version": "0.1",
    "title": "Remote and Hybrid Work (laboratory sample)",
    "text": "Hybrid arrangements depend on role eligibility, manager approval and the agreed workplace schedule. The assistant cannot grant exceptions."
  },
  "office": {
    "id": "HR-POL-005",
    "version": "0.1",
    "title": "Office Information (laboratory sample)",
    "text": "Office addresses and visitor instructions are maintained in the Facilities directory. Confirm location details with Facilities before travelling."
  }
};
function respond(input){
  const prompt=String(input??"").trim(), q=prompt.toLowerCase();
  const base=(decision,reason,answer,policyKey=null)=>({version:"0.1.0",decision,reason,answer,source:policyKey?`${POLICY[policyKey].id}@${POLICY[policyKey].version}`:null,human_required:decision!=="ANSWER",external_action_performed:false,audit:{request_present:Boolean(prompt),rule:reason,agent_version:"0.1.0",policy_ref:policyKey?POLICY[policyKey].id:null}});
  if(!q)return base("HUMAN_ESCALATION","empty_or_unclear","Please provide a general HR policy question. An HR colleague can help if your request is personal or unclear.");
  if(/ignore (previous|all)|bypass|override (system|rules)|admin token|system prompt|jailbreak|all employee data/.test(q))return base("HUMAN_ESCALATION","adversarial_request","I cannot follow instructions that override service boundaries. The request needs human review.");
  if(/salary|payroll|bank account|bonus|emirates id|passport|medical|health record|visa|immigration|contract|disciplin|termination|another person|other employee|personal data|private data|record of|entitlement|leave balance|remaining leave|qualify|change my|edit my/.test(q))return base("HUMAN_ESCALATION","restricted_or_individualised","This request requires a human HR specialist. I cannot access private records, make employment decisions, or perform HRIS changes.");
  if(/outdated|expired|changed yesterday|missing source|policy changed|new rule/.test(q))return base("HUMAN_ESCALATION","policy_freshness_uncertain","I cannot verify an approved current policy source. I will not guess; please consult an HR policy owner.");
  if(/employment (confirmation )?letter|letter of employment|employment verification letter|experience letter/.test(q))return base("APPROVAL_REQUIRED","letter_draft_request","I can prepare a draft employment-letter request, but an authorised HR specialist must check details and approve issuance. No letter was sent.");
  const route=[["hours",/working hours|office hours|work hours|collaboration time/],["leave",/annual leave|leave policy|request leave/],["onboarding",/onboard|new joiner|induction checklist/],["remote",/remote work|hybrid|work from home/],["office",/office location|where is the office|office address/]].find(([key,re])=>re.test(q));
  if(route){const key=route[0],p=POLICY[key];return base("ANSWER",`approved_sample_policy:${key}`,`${p.text} [Source: ${p.id}, v${p.version}; LABORATORY SAMPLE — NOT UAE LEGAL ADVICE]`,key);}
  return base("HUMAN_ESCALATION","unknown_intent_or_no_grounding","I cannot verify a matching approved policy for that question. Please ask an HR colleague; I will not invent an answer.");
}
if (typeof module !== "undefined" && module.exports) module.exports = {respond, POLICY};
if (typeof window !== "undefined") window.HRServiceAgent = {respond, POLICY};
