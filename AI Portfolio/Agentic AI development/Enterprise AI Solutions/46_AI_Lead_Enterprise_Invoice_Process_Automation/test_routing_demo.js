#!/usr/bin/env node
"use strict";
const assert=require("node:assert/strict");
const {routeInvoice,run}=require("./routing_demo");
const cases=require("./synthetic_invoices.json");
let assertions=0;
const actual=run();
assert.equal(actual.length,cases.length); assertions++;
for(let i=0;i<cases.length;i++){
 assert.equal(actual[i].route,cases[i].expected_route,"Routing mismatch "+cases[i].case_id);assertions++;
 assert.equal(actual[i].requires_human,true); assertions++;
 assert.equal(actual[i].can_post,false);assertions++;
 assert.equal(actual[i].can_pay,false);assertions++;
}
const baseline={vendor_id:"X",invoice_number:"Y",amount_aed:25000,po_present:true,po_match:true,duplicate_flag:false,bank_change_flag:false,vat_valid:true,field_confidence:0.99};
assert.equal(routeInvoice(baseline).route,"BUSINESS_OWNER_APPROVAL");assertions++;
assert.equal(routeInvoice({...baseline,amount_aed:25001}).route,"FINANCE_APPROVAL");assertions++;
assert.equal(routeInvoice({...baseline,duplicate_flag:true,field_confidence:0.1}).route,"HOLD_DUPLICATE");assertions++;
assert.equal(routeInvoice({...baseline,bank_change_flag:true}).route,"ESCALATE_BANK_CHANGE");assertions++;
assert.equal(routeInvoice({...baseline,field_confidence:1.1}).route,"NEED_INFO");assertions++;
assert.equal(routeInvoice({...baseline,amount_aed:-1}).route,"NEED_INFO");assertions++;
assert.equal(routeInvoice({...baseline,invoice_number:""}).route,"NEED_INFO");assertions++;
console.log("PASS: "+cases.length+" synthetic invoice scenarios + "+(assertions-1-cases.length*4)+" boundary/priority tests; "+assertions+" assertions.");
