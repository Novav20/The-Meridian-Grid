# LESSON AUTHORING GUIDELINES & SPECIFICATION

This document establishes the strict architectural, pedagogical, visual design, and asset governance standards for authoring domain mastery lessons and technical assets within `docs/00-Domain-Mastery/` for **The Meridian Grid (TMG)** platform.

---

## 1. Directory & Asset Architecture (NO SYMLINKS)

To guarantee cross-platform compatibility across Linux, Windows, macOS, Git, and Obsidian vaults, the domain mastery directory is organized into strictly isolated, real folders:

```text
docs/00-Domain-Mastery/
├── 00-Lesson-Authoring-Guidelines.md
├── Glossary.md                           <-- Single Source of Truth & Ubiquitous Language Index
├── images/                               <-- REAL DIRECTORY: Modular Vector SVGs
│   ├── 01-purdue-hierarchy.svg
│   ├── 11-monolith-vs-web-scada-stack.svg
│   ├── 11-web-scada-component-architecture.svg
│   └── 11-web-scada-deployment-topology.svg
├── photos/                               <-- REAL DIRECTORY: Real Equipment Photos
│   ├── 11-legacy-scada-workstation.png
│   ├── 11-field-controller-plc.png
│   ├── 11-remote-io-terminal-rack.png
│   ├── 11-dual-homed-eon-gateway.png
│   ├── 11-modern-control-room-console.png
│   └── 11-rugged-field-tablet.png
└── lessons/                              <-- REAL DIRECTORY: Lesson Notes
    ├── 01-Purdue-vs-UNS.md
    ├── 02-Modbus-TCP-Mechanics.md
    └── 11-Monolithic-vs-Web-SCADA.md
```

### Mandatory Asset Rules:
1. **Real Folders Only:** `images/`, `photos/`, and `lessons/` MUST be physical filesystem directories. **Never use symbolic links (`ln -s`)** inside git-tracked paths.
2. **Unified HTML `<figure>` & `<figcaption>` Standard:** All figures — whether vector SVGs or real equipment photographs — MUST be wrapped in semantic HTML5 `<figure align="center">` containers with `<figcaption>` labels. This ensures perfect centering, responsive scaling, and full-text searchability in Obsidian, GitHub, and browser previews.
3. **No Embedded Captions Inside SVGs or Photos:** Figure captions must live exclusively inside the markdown `<figcaption>` element directly below the visual asset, never baked into the graphic files themselves.

---

## 2. Pedagogical Framework: Cognitive Science & Systems Engineering

All lessons must be designed around cognitive load optimization and mental schema construction:

### A. Reducing Extraneous Cognitive Load & Schema Construction (Sweller, 1988)
- **The Fluid Narrative Mandate (Anti-Pattern: The Disconnected Catalog):**
  - Lessons must NEVER read like an encyclopedic API dictionary or a disconnected glossary.
  - Every concept must be linked in a **causal progression**:
    $$\text{Field Hardware Reality} \longrightarrow \text{Physical Bottleneck / Vulnerability} \longrightarrow \text{Network / Protocol Invariant} \longrightarrow \text{Software Architecture} \longrightarrow \text{Industrial Deployment}$$
  - Every subsection must answer: *"What operational, safety, or financial failure occurs if an engineer ignores this mechanical constraint?"*
- **Scaffold Physical Primitives First:** Before introducing software layers (UNS brokers, WebSockets, reactive UI stores), explicitly trace physical realities (transceiver pins, dual NICs, kernel IP forwarding, controller scan cycles, physical isolation).
- **Controlled Industrial Grounding:** Ground concepts in concrete automation hardware (e.g., Rockwell ControlLogix, Siemens S7-1500, Moxa DIN-rail IPCs, RS-485 termination resistors, IDMZ reverse proxies).

### B. The 5-Act Causal Narrative Arc (Pedagogical Spine, NOT Literal Headings)
The 5-Act Arc governs the **underlying pedagogical progression** of the document. To maintain a professional, natural engineering tone, **never write "Act 1", "Act 2" literally in section headings**. Use direct, domain-specific titles that embody the arc:

1. **Act 1: Physical Reality & Field Equipment (Prerequisites):** 
   - *Example Heading:* `## 1. Physical Reality & Field Equipment (Prerequisites)`
   - Hardware baseline (PLCs, RTUs, sensors, fieldbuses, operator workstations, hardware dongles), physical operating environments, and mechanical/electrical failure modes. Grounded with **real equipment photos** and comparison SVGs.
2. **Act 2: Architectural Pitfalls & Protocol Invariants (The Tension):**
   - *Example Heading:* `## 2. Architectural Pitfalls of Desktop Monoliths`
   - The systemic breakdown of legacy approaches (e.g., the $\mathcal{O}(N^2)$ integration tax of point-to-point polling, direct IP routing attack surfaces, commercial tag licensing traps, and compilation downtime).
3. **Act 3: Decoupled Web-Native Component Architecture (The Solution):**
   - *Example Heading:* `## 3. Decoupled Web SCADA Component Architecture`
   - Modular breakdown of the target system (Scene Graph Renderer, Headless Gateway, Unified Namespace Broker, Append-Only Historian), accompanied by UML Component / C4 diagrams.
4. **Act 4: Enterprise Deployment Topology across Purdue & IDMZ (TMG Production Reality):**
   - *Example Heading:* `## 4. Enterprise Deployment Topology across Purdue & IDMZ`
   - Concrete physical/virtual network topology respecting ISA/IEC 62443 zones and conduits, dual-homed edge gateways (`net.ipv4.ip_forward = 0`), and firewall configurations (Port 443 / Port 8883).
5. **Act 5: Active-Recall Consolidation (Deliberate Practice):**
   - *Example Heading:* `## 6. Active-Recall Assessments`
   - Active-recall collapsible FAQ accordions (`> [!FAQ]- ...`) reinforcing core invariants, physical failure modes, and architectural trade-offs with literature citations.

### C. Dual-Coding & Spatial Contiguity (Paivio & Mayer)
- **Positioning:** Every visual illustration (photo or SVG) MUST appear **immediately after** the textual concept is explained, never before.
- **Complementary Information:** Diagrams must never repeat verbatim sentences from the text; they must visually communicate topology, state transitions, message flows, and security zones.

### D. Acronym Policy & Centralized Glossary Anchoring (Spaced Retrieval)
- **First-Mention Acronym Expansion:**
  - Define the acronym upon its **first appearance** in a lesson: `Full Technical Term (ACRONYM)`.
  * For all subsequent references within that lesson, use the acronym alone (`ACRONYM`). Repeating the full phrase in parenthesis is strictly prohibited to prevent extraneous visual parsing noise.
- **Wikilinking to Centralized Glossary:**
  - To support spaced retrieval and knowledge graph indexing in Obsidian, link critical domain terms to their canonical anchor inside `Glossary.md`:
    ```markdown
    [[../Glossary#Double-Point Status (Dbpos)|Dbpos]]
    [[../Glossary#Moving Analog Indicator (MAI)|Moving Analog Indicator]]
    [[../Glossary#Unified Namespace (UNS)|Unified Namespace]]
    ```
  - This allows the reader to look up formal invariants instantly without context switching, while populating Obsidian backlink panels with multi-lesson cross-references.

### E. Project Context & Decision Status
- Mention **The Meridian Grid (TMG)** when applying an established requirement or invariant to the platform; do not append the project name to generic protocol or domain explanations merely for branding.
- A lesson must distinguish status explicitly:
  - **Baseline / requirement:** stated in [`README.md`](../../README.md) or `docs/02-SI-Requirements/`.
  - **Candidate:** listed as subject to Phase 2 ADR evaluation in [`README.md`](../../README.md).
  - **Lesson pattern:** an illustrative implementation or trade-off that is not a project commitment.
- Do not use words such as *implemented*, *enforces*, *mandated*, *the platform uses*, or *strictly* for a candidate or lesson pattern. Use *proposes*, *illustrates*, *one option is*, or *would* instead.
- A project-specific claim must link to its source requirement or ADR. If no source exists, present it as a lesson pattern and state that it is not yet decided.

---

## 3. Figure & Figcaption Markup Standards

Obsidian is built on Chromium, providing complete native support for HTML5 `<figure>` and `<figcaption>` elements. Native Obsidian markdown does not feature a built-in caption tag; hence, `<figure>` is the authoritative standard across all lessons.

### A. Single Vector SVG Figure
For architectural diagrams and UML schematics:
```html
<figure align="center">
  <img src="../images/XX-diagram-slug.svg" alt="Descriptive Alt Text" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure XX.Y: Concise descriptive figure caption detailing data flow and architectural tiers.</em></figcaption>
</figure>
```

### B. Single Real Equipment Photograph
For individual pieces of hardware:
```html
<figure align="center">
  <img src="../photos/XX-equipment-slug.png" alt="Descriptive Equipment Alt Text" style="max-width: 750px; width: 100%; height: auto; border-radius: 6px;" />
  <figcaption><em>Figure XX.Y: Descriptive caption specifying equipment make, model, and operational tier.</em></figcaption>
</figure>
```

### C. Split Subfigure Layout: (a) and (b) Side-by-Side
When a figure covers two distinct, complementary pieces of industrial equipment (e.g., Central Controller CPU vs. Distributed Remote I/O, or Control Room Console vs. Field Tablet), use a responsive flexbox container inside `<figure>`:

```html
<figure align="center">
  <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <div style="flex: 1 1 340px; max-width: 48%; text-align: center;">
      <img src="../photos/XX-equipment-a.png" alt="Equipment A Alt Text" style="width: 100%; height: auto; border-radius: 6px;" />
      <br>
      <small><strong>(a)</strong> Equipment A Title and Model</small>
    </div>
    <div style="flex: 1 1 340px; max-width: 48%; text-align: center;">
      <img src="../photos/XX-equipment-b.png" alt="Equipment B Alt Text" style="width: 100%; height: auto; border-radius: 6px;" />
      <br>
      <small><strong>(b)</strong> Equipment B Title and Model</small>
    </div>
  </div>
  <figcaption><em>Figure XX.Y: High-Level Figure Caption: (a) Detailed description of equipment A; (b) Detailed description of equipment B.</em></figcaption>
</figure>
```

### D. Full-Text Searchability & Vault Navigation
Obsidian's vault-wide search scans HTML tag content identically to markdown text:
- Both `<figcaption>` text and `<img> alt` attributes are indexed.
- Searching for specific vendors or models (e.g., `ControlLogix`, `S7-1500`, `WinCC`, `HASP dongle`, `Moxa DIN-rail`) in Obsidian immediately surfaces the exact figure and paragraph.

### E. Visual Contribution & Non-Redundancy
- Every figure MUST add a visual dimension that the surrounding prose does not convey by itself: spatial relationship, temporal sequence, causal mechanism, quantitative comparison, state transition, ownership boundary, or failure boundary.
- Do not reproduce a paragraph as labels inside an SVG. Keep equations, exhaustive component lists, and detailed definitions in the lesson text; use the figure to show how those elements relate.
- A figure may repeat a short label when necessary for orientation, but its dominant teaching purpose must be legible from the visual structure alone.
- Captions MUST state the figure's teaching purpose, not restate every label. When the prose already derives a result, the figure should show the operational consequence or decision that follows from it.
- Before accepting a figure, ask: **What can a learner infer from the image that they could not infer from the adjacent paragraphs?** If the answer is “nothing,” redesign or remove it.

---

## 4. SVG Visual Design & Semantic Color Standards (ANSI/ISA-101.01)

To eliminate visual fatigue, eliminate preattentive distraction, and enforce **ANSI/ISA-101.01 High-Performance HMI** ergonomics, all SVG diagrams must adhere to the **3-Tone Disciplined Palette**:

### The 3-Tone Architectural Palette:
| Visual Layer | Proportion | Hex Values | Functional Usage & Meaning |
| :--- | :--- | :--- | :--- |
| **Structural Baseline** | **~80%** | `#16191f` / `#0d1117` / `#161b22`<br>Borders: `#30363d` | Dark background canvas, outer tier containers, and component cards. All software tiers share this neutral baseline to demonstrate that they form **one cohesive platform**, preventing arbitrary categorical color chaos. |
| **Unified Data Flow** | **~15%** | **Cool Cyan / Blue** (`#388bfd` / `#58a6ff` / `#79c0ff`) | Connectors, conduits (`WSS :443`, `MQTTS :8883`), directional arrows (`#arr-blue`), component stereotype tags (`«component»`), and active interfaces. Visual continuity allows the learner's visual cortex to trace data flow from edge to browser without distracting hue shifts. |
| **High-Salience Accents** | **~5%** | **Coral Red** (`#f85149` / `#ff7b72`)<br>**Muted Green** (`#3fb950`) | **Strictly functional exceptions:**<br>• **Coral Red:** Reserved *exclusively* for unsegmented direct IP attack vectors, monolithic vulnerabilities, and firewall perimeter boundaries (`FW 1`, `FW 2`).<br>• **Muted Green:** Reserved *exclusively* for verified security checkmarks (`✓ Complete Air-Gap`). |

> [!WARNING] Anti-Pattern: The Rainbow Palette
> Never assign distinct decorative colors (e.g. amber for Node.js, purple for broker, green for edge, blue for client) to different software tiers. Categorical color coding induces extraneous cognitive load (Sweller, 1988) and falsely triggers alarm mental models (e.g., amber is reserved for Priority 2 Alarms under ISA-18.2).


---

## 5. Traceability & Epistemological Governance (ISO/IEC 29110)

1. **Mandatory Literature Traceability:** Every domain constraint, protocol standard, and architectural assertion MUST cite empirical research extractions from `docs/02-SI-Requirements/Domain-Research/extractions/` using Obsidian links:
   - Example: `[[Guo_et_al_2022|Guo et al., 2022]]`
   - Example: `[[Villamar_et_al_2025|Villamar et al., 2025]]`
   - Example: `[[Bellini_et_al_2022|Bellini et al., 2022]]`
2. **Normative Standard Grounding:** All network architectures, security boundaries, and telemetry taxonomies must align with:
   - **ANSI/ISA-95 (IEC 62264):** Equipment hierarchy taxonomy (`Enterprise/Site/Area/Line/Cell`).
   - **Eclipse Sparkplug B v3.0:** State management and Protobuf payload contracts over MQTT.
   - **ANSI/ISA-101.01:** Ergonomic, gray-scale high-performance HMI design.
   - **ISA/IEC 62443:** Security zones, conduits, and Industrial DMZ (IDMZ) reverse-access isolation.

---

## 6. Standard Lesson Note Template

Every lesson file (`docs/00-Domain-Mastery/lessons/XX-<Topic-Name>.md`) must follow this exact template:

```markdown
---
title: "XX: <Topic Title>"
tags:
  - scada
  - iiot
  - web-scada
  - industrial-automation
  - purdue-model
  - uns
  - iec62443
  - isa95
date: YYYY-MM-DD
module: <Module Number>
lesson: <Lesson Number>
status: pilot-gold
---

# Lesson XX: <Topic Title>

<Brief, high-impact opening framing the concept within high-reliability industrial automation>

---

## 1. Physical Reality & Field Equipment (Prerequisites)
<Detailed explanation of physical automation hardware, electrical interfaces, and controller execution>

<figure align="center">
  <img src="../photos/XX-<equipment-slug-1>.png" alt="<Equipment 1 Description>" style="max-width: 750px; width: 100%; height: auto; border-radius: 6px;" />
  <figcaption><em>Figure XX.1: <Caption describing real physical equipment 1></em></figcaption>
</figure>

<figure align="center">
  <img src="../images/XX-<vector-comparison>.svg" alt="<Diagram Description>" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure XX.2: <Caption describing conceptual vector architecture></em></figcaption>
</figure>

---

## 2. Architectural Pitfalls & Protocol Invariants
<Rigorous analysis of legacy architectural bottlenecks, integration tax math, security vulnerabilities, or licensing traps>

---

## 3. Decoupled Web-Native Component Architecture
<Detailed software breakdown across Presentation, Headless Gateway, Unified Namespace, and Storage tiers>

<figure align="center">
  <img src="../images/XX-<component-architecture>.svg" alt="<Component Diagram Description>" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure XX.3: <Caption describing UML Component architectural breakdown></em></figcaption>
</figure>

---

## 4. Enterprise Deployment Topology across Purdue & IDMZ
<Physical and virtual node deployment, dual-homed network isolation, firewall conduits, and ISA/IEC 62443 zoning>

<figure align="center">
  <img src="../images/XX-<deployment-topology>.svg" alt="<Deployment Diagram Description>" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure XX.4: <Caption describing UML Deployment topology></em></figcaption>
</figure>

---

## 5. Structural Comparison
<Comparative evaluation table>

---

## 6. Active-Recall Assessments

> [!FAQ]- Question 1?
> Answer 1 with literature citation.

> [!FAQ]- Question 2?
> Answer 2 with literature citation.
```
