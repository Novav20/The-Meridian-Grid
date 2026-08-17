This pragmatic, 4-step Systematic Literature Review (SLR) protocol is designed for a solo software engineer to efficiently investigate a problem space, drawing on the rigorous methodologies of Kitchenham and Wieringa.

### Step 1: Research Question Formulation (PICOC)

To define the scope of your investigation, you must transform your need for information into an answerable question. Use the **PICOC criteria** to ensure the question is meaningful to both practitioners and researchers.

|Criterion|Definition|Reusable SE Template|
|:--|:--|:--|
|**Population**|The target group or application area affected by the problem.|Which types of software projects or engineering teams are under study?|
|**Intervention**|The software engineering artifact, technology, or method being investigated.|What specific tool, notation, or process is being evaluated?|
|**Comparison**|The baseline or traditional "control" method used for contrast.|What is the alternative or current "industry standard" practice?|
|**Outcomes**|The specific metrics for improvement or performance.|What are the success factors (e.g., reduced effort, increased quality, accuracy)?|
|**Context**|The real-world setting or conditions of practice.|Is this an industrial setting, an open-source project, or a lab experiment?|

**Solo Strategy:** Frame your question as an **Improvement Problem**: "Improve `<a problem context>` by `<designing/using an artifact>` that satisfies `<requirements>` so that `<stakeholder goals>` are achieved".

### Step 2: Search Strategy

A solo researcher must balance completeness with limited resources. Use an automated search strategy validated against a small "known set" of papers to ensure reliability.

1. **Constructing Boolean Strings:**
    - Identify synonyms for your **Intervention** and **Population**.
    - Connect the primary concepts with `AND` (e.g., "Intervention" AND "Population").
    - Connect synonyms within concepts with `OR` (e.g., "Scrum" OR "Agile").
    - **Rule:** Keep search strings simple; complex strings often deliver too many false positives in SE databases.
2. **Target Databases:** Prioritize Scopus, IEEEXplore (IEEE), ACM Digital Library, and ScienceDirect (Elsevier).
3. **Search Validation (Solo Rule):** Use the **Quasi-Gold Standard**. Perform a manual search of 1–2 key journals (e.g., _IEEE Transactions on Software Engineering_) for a limited time period to find 10–30 relevant papers. If your automated Boolean string finds >80% of these, it is acceptable.

### Step 3: Study Selection (Matrix Format)

Use a multi-stage screening process to rapidly filter out irrelevant abstracts.

|Criteria Level|Inclusion Criteria (Keep if...)|Exclusion Criteria (Discard if...)|
|:--|:--|:--|
|**Primary (Stage 1: Title/Abstract)**|1. Directly addresses the Intervention.2. Matches the defined Population.3. Published within the target timeframe.|1. Clearly irrelevant to the research question.2. Duplicates of previously screened papers.3. PowerPoint slides or extended abstracts only.|
|**Secondary (Stage 2: Full-Text)**|1. Reports a primary study with direct measurements.2. Provides data needed for synthesis (Outcomes).3. Written in English.|1. "Grey literature" without a clear peer-review source.2. Low-quality reporting (fails basic quality checklist).3. Opinions/Anecdotes without empirical evidence.|

**Solo Consistency Check:** Use a **test-retest** approach. Re-screen a random sample of 10% of your excluded papers after a time delay to ensure your criteria haven't drifted.

### Step 4: Data Extraction Template

Once papers are selected, use this template to extract the "Knowledge Context" necessary for designing a solution.

|Data Category|Extraction Elements|DDD/Design Science Alignment|
|:--|:--|:--|
|**Ubiquitous Language**|Extract specialized business terminology and mental models used by domain experts.|Identify one-and-only-one meanings for terms to eliminate ambiguity.|
|**Domain Rules**|Extract business logic, invariants (rules to be protected), and cause-effect relationships.|Define the "mechanisms" that produce observed system-level phenomena.|
|**Architectural Constraints**|Extract physical boundaries, composition relations (how systems interact), and communication patterns.|Identify "bounded contexts" where a specific model or language is valid.|
|**Context Assumptions**|Extract conditions of practice, participant demographics, and technical settings.|Note where the artifact interacts with specific problem environments.|

**Validation for the Solo Engineer:** Store all extracted text segments with page numbers to ensure **traceability** back to the primary source, allowing for a repeatable audit trail of your conclusions.