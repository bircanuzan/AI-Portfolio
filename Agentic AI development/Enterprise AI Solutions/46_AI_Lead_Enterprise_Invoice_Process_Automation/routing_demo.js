#!/usr/bin/env node
/** Independent, synthetic demonstration. NOT an OCR, AI or ERP integration. */
"use strict";
const fs=require("node:fs");
const path=require("node:path");
const routeInvoice=function routeInvoice(r) {
  const caseId = typeof r?.case_id==="string"&&r.case_id.trim()?r.case_id:"UNKNOWN_CASE";
  const outcome=(route,reason)=>({case_id:caseId,route,reason,requires_human:true,can_post:false,can_pay:false});
  if(!r||typeof r!=="object") return outcome("NEED_INFO","Missing input record");
  if(r.duplicate_flag===true) return outcome("HOLD_DUPLICATE","Suspected duplicate: block onward processing and investigate");
  if(r.bank_change_flag===true) return outcome("ESCALATE_BANK_CHANGE","Bank instruction change: independent verification required");
  if(typeof r.invoice_number!=="string"||!r.invoice_number.trim()||typeof r.vendor_id!=="string"||!r.vendor_id.trim()||typeof r.amount_aed!=="number"||!Number.isFinite(r.amount_aed)||r.amount_aed<=0) return outcome("NEED_INFO","Invoice identifier, supplier or positive amount missing/invalid");
  if(typeof r.field_confidence!=="number"||!Number.isFinite(r.field_confidence)||r.field_confidence<0||r.field_confidence>1) return outcome("NEED_INFO","Extraction confidence missing or outside [0,1]");
  if(r.vat_valid!==true) return outcome("REVIEW_TAX","Tax marker requires human review");
  if(r.field_confidence<0.9) return outcome("REVIEW_EXTRACTION","Proposed field confidence below illustrative threshold");
  if(r.po_present!==true) return outcome("MANUAL_PO_EXCEPTION","Purchase order missing: procurement review");
  if(r.po_match!==true) return outcome("REVIEW_PO_MISMATCH","Purchase order mismatch: owner review");
  if(r.amount_aed>25000) return outcome("FINANCE_APPROVAL","Illustrative delegation threshold exceeded: controller approval");
  return outcome("BUSINESS_OWNER_APPROVAL","Matched case within illustrative limit: human business-owner approval");
};
function run(inputFile=path.join(__dirname,"synthetic_invoices.json")){
 const source=JSON.parse(fs.readFileSync(inputFile,"utf8"));
 if(!Array.isArray(source))throw Error("Expected JSON array");
 return source.map(routeInvoice);
}
if(require.main===module){const file=process.argv[2]||path.join(__dirname,"synthetic_invoices.json"); console.log(JSON.stringify(run(file),null,2));}
module.exports={routeInvoice,run};
