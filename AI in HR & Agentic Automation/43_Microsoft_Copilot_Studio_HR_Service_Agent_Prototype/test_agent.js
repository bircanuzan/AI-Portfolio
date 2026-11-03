/** Reproduce evidence by running: node test_agent.js (Node 18+) */
"use strict";
const fs=require("fs"); const path=require("path");
const {respond}=require("./agent");
const tests=JSON.parse(fs.readFileSync(path.join(__dirname,"test_cases.json"),"utf8"));
const records=tests.map(t=>{const actual=respond(t.prompt);return {...t,actual,decision_pass:actual.decision===t.expected_decision,source_pass:actual.source===t.expected_source,pass:actual.decision===t.expected_decision&&actual.source===t.expected_source};});
const humanCases=records.filter(r=>r.expected_decision!=="ANSWER");
const summary={total:records.length,passed:records.filter(r=>r.pass).length,failed:records.filter(r=>!r.pass).length,correctness_pct:100*records.filter(r=>r.pass).length/records.length,mandatory_human_recall_pct:100*humanCases.filter(r=>r.actual.human_required).length/humanCases.length,go_live_recommendation:"HOLD — offline prototype only"};
const evidence={captured_on:new Date().toISOString(),environment:"Node.js local runtime",run_type:"actual deterministic response execution (NOT an LLM/Copilot Studio test)",summary,records};
if(process.argv.includes("--save")){fs.mkdirSync(path.join(__dirname,"evidence"),{recursive:true});fs.writeFileSync(path.join(__dirname,"evidence","latest_local_run.json"),JSON.stringify(evidence,null,2)+"\n");}
console.log(JSON.stringify(summary,null,2));
for(const r of records.filter(r=>!r.pass))console.log("FAIL",r.id,r.prompt,"expected",r.expected_decision,"got",r.actual.decision);
if(process.argv.includes("--strict")&&summary.failed)process.exitCode=1;
