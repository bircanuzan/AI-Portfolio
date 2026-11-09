/**
 * Typed, side-effect-free webhook boundary for the synthetic mobility demo.
 *
 * Evidence status: source-code example only. This is NOT a deployed HTTP endpoint,
 * authentication implementation, HRIS connector, or production approval system.
 *
 * Production gateway responsibilities BEFORE calling this function:
 * verify webhook HMAC/signature, request expiry, tenant identity, replay window,
 * TLS, rate limits, and service-account authorization. A schema check alone
 * cannot authenticate a sender or authorize a regulated operation.
 */

export type MobilityCategory =
  | "immigration_document"
  | "payroll_mismatch"
  | "identity_change"
  | "document_check"
  | "policy_question"
  | "case_routing";

export interface MobilityEvent {
  event_id: string;
  case_id: string;
  tenant_id: string;
  source: string;
  category: MobilityCategory;
  jurisdiction: string;
  contains_sensitive_data: boolean;
  document_complete?: boolean;
  effective_date_mismatch?: boolean;
  approved_policy_id?: string;
}

export type ProposedDispatch =
  | { state: "quarantine_for_privacy_review"; reason_code: "sensitive_data"; case_ref: string }
  | { state: "submit_to_python_checker"; event: MobilityEvent };

const APPROVED_KEYS = new Set([
  "event_id", "case_id", "tenant_id", "source",
  "category", "jurisdiction", "contains_sensitive_data",
  "document_complete", "effective_date_mismatch", "approved_policy_id",
]);

const CATEGORIES = new Set<string>([
  "immigration_document", "payroll_mismatch", "identity_change",
  "document_check", "policy_question", "case_routing",
]);

const IDENTIFIER_KEYS: (keyof MobilityEvent)[] = [
  "event_id", "case_id", "tenant_id", "source", "jurisdiction",
];

/** Strictly normalize a JSON-decoded event; reject extra PII-bearing fields. */
export function normalizeMobilityEvent(input: unknown): MobilityEvent {
  if (input === null || typeof input !== "object" || Array.isArray(input)) {
    throw new Error("invalid_event_shape");
  }
  const record = input as Record<string, unknown>;
  if (Object.keys(record).some((key) => !APPROVED_KEYS.has(key))) {
    throw new Error("unapproved_fields_present");
  }
  for (const key of IDENTIFIER_KEYS) {
    const value = record[key];
    if (typeof value !== "string" || value.length < 1 || value.length > 90) {
      throw new Error("invalid_required_field");
    }
  }
  if (typeof record.category !== "string" || !CATEGORIES.has(record.category)) {
    throw new Error("unsupported_case_type");
  }
  if (typeof record.contains_sensitive_data !== "boolean") {
    throw new Error("invalid_sensitivity_flag");
  }
  for (const key of ["document_complete", "effective_date_mismatch"]) {
    if (record[key] !== undefined && typeof record[key] !== "boolean") {
      throw new Error("invalid_boolean_field");
    }
  }
  if (
    record.approved_policy_id !== undefined &&
    typeof record.approved_policy_id !== "string"
  ) {
    throw new Error("invalid_policy_id");
  }
  return record as unknown as MobilityEvent;
}

/**
 * Decide ONLY whether to quarantine or forward a sanitized event to the
 * independent Python checker. This function executes NO external writes.
 */
export function prepareDispatch(input: unknown): ProposedDispatch {
  const event = normalizeMobilityEvent(input);
  if (event.contains_sensitive_data) {
    return {
      state: "quarantine_for_privacy_review",
      reason_code: "sensitive_data",
      case_ref: event.case_id,
    };
  }
  return { state: "submit_to_python_checker", event };
}

/**
 * Do not log arbitrary exceptions, request bodies or raw records.
 * The upstream gateway should return a generic error to external callers,
 * while a controlled internal audit records an allowlisted reason code.
 */
export function safeRejectionReason(error: unknown): string {
  const allowed = new Set([
    "invalid_event_shape",
    "unapproved_fields_present",
    "invalid_required_field",
    "unsupported_case_type",
    "invalid_sensitivity_flag",
    "invalid_boolean_field",
    "invalid_policy_id",
  ]);
  const reason = error instanceof Error ? error.message : "";
  return allowed.has(reason) ? reason : "validation_error";
}
