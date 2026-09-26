# Engineering Constraints & Quality Governance

## 1. Research & Design Phase Constraints (Problem Space)

1. **Epistemological Constraint (Zero-Speculation):** Every domain requirement, protocol decision, or invariant MUST trace backward to an empirical source (`[[Paper_ID]]`) or official standard (ISA-95, ISA/IEC 62443, Sparkplug B v3.0). Ungrounded assumptions are rejected.
2. **Semantic Non-Ambiguity (DDD Invariant):** Within a single Bounded Context, a term has one and only one definition. Terminology conflicts between papers must be formally resolved or isolated via bounded context boundaries.
3. **Bi-Directional Traceability Matrix (ISO/IEC 29110):** Every requirement must point backward to an extraction source note and forward to an Architectural Decision Record (ADR) and a verification test case.
4. **Physical & Network Boundary Invariants:** System topologies must strictly respect operational security zoning (ISA/IEC 62443). OT zone components (Levels 1–2) cannot accept inbound connections from enterprise networks (Levels 4–5).
5. **Formal Data Contracts First:** Telemetry structures must be formally defined (JSON Schema / Protobuf) and validated against the Ubiquitous Language before writing runtime ingestion or UI code.

## 2. LLM Prompt Governance Policy

A prompt MUST be saved as a Markdown file in `Prompts/*.md` and tracked in `LLM-Prompt-Log.xlsx` IF AND ONLY IF it satisfies at least one criterion:
- **Artifact Generation:** Produces an ISO 29110 work product (Extractions, Ubiquitous Language, Context Maps, ADRs, Schemas).
- **Quality Gate / Audit:** Executes a formal verification, screening, or grounding check.
- **Reusable Automation:** Designed for repeated execution across iterations (e.g., Sub-RQ 1, Sub-RQ 2).

*Ad-hoc exploratory queries and conversational debugging must not be logged.*