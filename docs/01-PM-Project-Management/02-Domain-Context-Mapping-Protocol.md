---
document_type: "Methodological Protocol"
authoritative_source: "Vlad Khononov (2022), Learning Domain-Driven Design (O'Reilly)"
framework: "Domain-Driven Design (Strategic Design)"
version: "1.0.0"
date: "2026-09-20"
---

# Domain Context Mapping Protocol

This protocol codifies the theoretical rules, integration patterns, and structural documentation templates for constructing the architectural Context Map for The Meridian Grid (TMG), grounded in Vlad Khononov's *Learning Domain-Driven Design* (2022).

---

## 1. Definition and Purpose of a Context Map

- **Definition**: A **Context Map** is a visual representation and graphical notation that plots the communication and integration patterns between a system’s Bounded Contexts. It provides an architectural bird’s-eye view of a project's integration and collaboration landscapes.
- **Problems Solved in System Architecture**:
  1. **Managing Boundary Dependencies & Language Inconsistencies**: In non-trivial software systems, attempting to build a single enterprise-wide domain model fails because different domain experts hold conflicting mental models and business terminology. Bounded Contexts define explicit consistency boundaries within which a specific Ubiquitous Language is valid. A Context Map makes cross-context dependencies, translation needs, and model boundaries explicit.
  2. **Exposing High-Level System Architecture**: It provides architects with a structural overview of all system components, the domain models they implement, and their integration touchpoints.
  3. **Surfacing Organizational Dynamics & Friction**: System architecture is deeply connected to team organization. A Context Map highlights organizational dynamics, communication impediments, and team friction (e.g., where downstream consumers must build protective translation layers).

---

## 2. Bounded Context Integration Patterns

Khononov categorizes integration patterns into three primary groups based on collaboration styles and power balances: **Cooperation**, **Customer–Supplier**, and **Separate Ways**.

### A. Cooperation Patterns
Used between teams with well-established communication channels, shared goals, or single-team/solo ownership.

- **Partnership**: Integration between Bounded Contexts is coordinated in an ad hoc, two-way manner. Neither side dictates the contract; instead, both collaborate continuously, adjust APIs cooperatively, and resolve issues without organizational conflict. *(Chapter 4, p. 50)*.
- **Shared Kernel**: Two or more Bounded Contexts overlap and share a limited subset of a domain model (such as shared data structures or integration contracts). Any modification to the shared kernel codebase immediately impacts all participating Bounded Contexts, requiring continuous automated integration tests across all affected contexts. *(Chapter 4, pp. 50–52)*.

### B. Customer–Supplier Patterns
Used when an asymmetric balance of power exists between an upstream service provider (supplier) and a downstream consumer (customer).

- **Conformist**: The power balance favors the upstream team, which provides an integration contract on a "take it or leave it" basis. The downstream team chooses to conform its internal model entirely to the upstream model, surrendering design autonomy because the supplier model is sufficient or represents an industry standard. *(Chapter 4, pp. 53–54)*.
- **Anticorruption Layer (ACL)**: The power lies with the upstream provider, but the downstream consumer is unwilling to conform to a foreign or messy model. The downstream team implements a translation layer (ACL) that converts incoming upstream contracts into its own clean Ubiquitous Language. *(Chapter 4, pp. 54–55)*.
- **Open-Host Service (OHS)**: The upstream provider protects its consumers by decoupling its internal implementation model from its public API via a dedicated, integration-oriented contract called a **Published Language (PL)**. This allows the upstream system to evolve independently and serve multiple API versions simultaneously. *(Chapter 4, pp. 55–56)*.

### C. Separate Ways Pattern
Used when teams choose not to collaborate at all.

- **Separate Ways**: Teams duplicate functionality locally within their respective Bounded Contexts rather than integrating. This is driven by severe communication barriers or when duplicating a Generic subdomain is far cheaper than cross-service integration overhead. **Invariant:** This pattern must **never** be used for Core subdomains. *(Chapter 4, pp. 56–57)*.

---

## 3. Strategic Subdomain Classification and Mapping

Khononov categorizes subdomains along two core axes: **Business Differentiation** (Competitive Advantage) and **Business Logic Complexity**.

### Subdomain Classification
1. **Core Subdomain**:
   - **Definition**: The primary source of a company's competitive advantage and differentiation.
   - **Characteristics**: High business logic complexity, high volatility, and frequent requirement changes.
   - **Strategy**: Must be implemented strictly **in-house** using advanced modeling patterns and assigned top engineering focus. *(Chapter 1, pp. 4–5, 8–10)*.
2. **Generic Subdomain**:
   - **Definition**: Solved, complex business problems common across all industry players that offer zero competitive edge (e.g., authentication, encryption, time-series storage engines, basic MQTT transport).
   - **Characteristics**: High complexity, low volatility.
   - **Strategy**: **Adopt off-the-shelf software**, open-source solutions, or managed cloud services. *(Chapter 1, pp. 6, 8–10)*.
3. **Supporting Subdomain**:
   - **Definition**: Auxiliary business functions required to support operations that offer no competitive advantage (e.g., basic ETL scripts, configuration loaders).
   - **Characteristics**: Low business logic complexity (CRUD screens, simple data mapping) and low volatility.
   - **Strategy**: Implement in-house or outsource using simple patterns like Transaction Script or Active Record. *(Chapter 1, pp. 6, 8–10)*.

### Structural Mapping Strategies
- **Discovered vs. Designed**: Subdomains are **discovered** during domain analysis (problem space), whereas Bounded Contexts are **designed** as software architecture decisions (solution space).
- **1:1 Alignment**: Each subdomain maps directly to its own Bounded Context (ideal for Core subdomains).
- **Many:1 Alignment (Monolithic Bounded Context)**: Multiple subdomains exist within a single Bounded Context (avoids premature distributed complexity during early development stages).

---

## 4. Documentation Template for Technical Specifications

To document a Context Map in technical specifications, adhere to this minimal structural layout:

```markdown
# Architectural Context Map Specification

## 1. Visual Context Map Diagram
[Mermaid.js diagram plotting Bounded Context nodes and directed edges annotated with 
 badges: Upstream [U], Downstream [D], ACL, OHS, PL, Partners, Shared Kernel]

## 2. Bounded Context Registry
### Context: [Bounded Context Name]
*   **Strategic Purpose**: [Concise definition of the problem domain and model boundary]
*   **Encompassed Subdomains**: [Subdomain Name(s)] — [Classification: Core / Generic / Supporting]
*   **Team Ownership**: [Single assigned engineering team / Solo Developer]
*   **Ubiquitous Language Scope**: [Summary of core entities and invariants valid within this boundary]

## 3. Integration & Relationship Matrix
| Source Context (Upstream / Partner) | Target Context (Downstream / Partner) | Integration Pattern | Contract / Published Language | Communication Protocol |
| :--- | :--- | :--- | :--- | :--- |
| [Context A (U)] | [Context B (D)] | Open-Host Service / Published Language | [Protobuf / JSON Schema] | Asynchronous (WebSocket / MQTT) |
| [Context C] | [Context D] | Partnership | Shared Ad-hoc APIs | Synchronous (HTTP / REST) |
| [Context E] | [Context F] | Shared Kernel | [Shared Library / NPM package] | Shared Codebase |

## 4. Cross-Context Boundary Invariants
*   **Data Ownership Invariants**: Clear delineation of authoritative data writers vs read-only consumers.
*   **Latency & Performance Bounds**: Hard real-time vs near-real-time synchronization boundaries.
```