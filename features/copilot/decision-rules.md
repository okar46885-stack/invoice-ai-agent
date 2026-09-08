# Decision Rules for Copilot layer

This document defines the decision thresholds and rules used by the Copilot layer (Milestone 1).

Critical fields
- Invoice No.
- Date
- GSTIN
- Total
- Customer

Confidence thresholds (percentage values 0.0 - 100.0)
- HIGH_CONFIDENCE (eligible for auto-approval): >= 95.0
- SUGGESTION_RANGE (show suggestions, still require review): 85.0 <= confidence < 95.0
- HUMAN_REVIEW (mandatory human review): confidence < 85.0

Rules
- Never auto-approve a document if any critical field has confidence < 85.0.
- For fields in [85.0, 95.0), suggestions MAY be shown but the field remains reviewable.
- Never invent missing or uncertain data. If no SuggestionProvider is configured, the service MUST return 503 for suggestion requests and MUST NOT fabricate values.
- Every suggestion must include: confidence, provenance (when available), and a reason for the suggestion.

Reviewer actions
- Apply: reviewer accepts a suggestion; the applied value is written as the final value for the field, a feedback record is stored, and an immutable audit event is recorded.
- Edit: reviewer supplies a corrected value; corrected value is stored, feedback recorded, and an audit event logged.
- Reject: reviewer rejects the suggestion; suggestion status is updated to rejected and an audit event is recorded. The original extracted value remains unchanged.

Audit & immutability
- All reviewer feedback and suggestion lifecycle events must be recorded in immutable audit log rows with timestamps, reviewer id, and references to suggestion ids when applicable.

Provenance
- Every suggestion should preserve provenance information where available (page, coordinates, extracted text span) and include it in suggestion payloads and persisted rows.
