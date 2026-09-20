---
paper_id: "Koltsova_et_al_2026"
query_id: "Q03"
title: "Composite Microservice Architecture of the Digital Twin"
authors: "Koltsova E.; Pysin M.; Lobanov A.; Antipov A.; Arkhipov A.; Perekatov A.; Krasheninnikov R."
year: 2026
doi: "10.3390/info17080760"
keywords: ["3D modeling", "automated visualization", "composite architecture", "digital twin", "microservice architecture", "SCADA"]
source_pdf: "Composite Microservice Architecture of the Digital Twin.pdf"
extraction_date: "2026-09-20"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Digital Twin
- **Definition**: An up-to-date virtual representation of a physical object or process with two-way data communication used for monitoring, simulation, and optimization.
> **Evidence**: "A digital twin is defined as an up-to-date virtual representation of a physical object or process with two-way data communication used for monitoring, simulation, and optimization" (p. 2)

- **Term**: Composite Architecture
- **Definition**: A software architecture constructed from a set of loosely coupled, independently developed, deployed, and scalable components that interact exclusively through clearly defined interfaces.
> **Evidence**: "A composite architecture is one in which a software system is constructed from a set of loosely coupled, independently developed, deployed, and scalable components" (p. 4)

- **Term**: Unified Data Exchange Subsystem
- **Definition**: An architectural component serving as an API gateway that abstracts disparate systems, introduces persistent versioned contracts, and ensures a consistent interaction environment without taking ownership of subject data.
> **Evidence**: "The proposed architecture envisions the implementation of a unified data exchange system, which will abstract all disparate systems and introduce persistent contracts, support and guarantee their versioning, and ensure a consistent exchange environment." (p. 6)

- **Term**: High Internal Cohesion and Loose External Coupling
- **Definition**: Architectural principles where a component internally groups functions sharing a common responsibility and lifecycle, while externally interacting through a limited set of explicit contracts independent of internal implementations.
> **Evidence**: "High internal cohesion means combining functions related to a common responsibility and lifecycle. Loose external coupling means that the component interacts with other parts through a limited set of explicit contracts and is independent of their internal implementation." (p. 5)

### 2. Domain Rules and Invariants

- **Rule**: Data Ownership Preservation Invariant
- **Mechanism**: The data exchange subsystem provides delivery, presentation, and access interfaces but is prohibited from assuming data ownership; the generating component remains the sole authoritative source of truth.
> **Evidence**: "It is critical that the exchange subsystem does not become the owner of all subject data. The component responsible for its generation and correctness remains the owner. The exchange environment ensures delivery, presentation, and access, but does not blur responsibility." (p. 6)

- **Rule**: Backward-Compatible Contract Permanence Rule
- **Mechanism**: Interfaces, data schemas, and interaction protocols must be modified in a controlled, backward-compatible manner, preventing updates in individual components from causing failures in dependent subsystems.
> **Evidence**: "Interfaces, data structures, and interaction rules are changed in a controlled manner and with backward compatibility in mind. Purpose: Preventing failures of dependent subsystems when updating individual components." (p. 11)

- **Rule**: Universal Payload Standardization via JSON Protocol
- **Mechanism**: All component interactions passing through the central data exchange layer are standardized using JSON payloads over HTTP/WebSocket, enabling technological heterogeneity across disparate software stacks.
> **Evidence**: "As can be seen from the component diagram, all interactions with the data exchange system are carried out via the JSON protocol, which allows any system to supply and consume data." (p. 6)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Higher-Order Composite System-of-Systems Pattern
- **Implication**: Large, autonomous industrial systems (such as SCADA platforms, dynamic process simulators, and CAD environments) act as microservice-level service components at the digital twin level without requiring fine-grained code decomposition or a single unified technology stack.
> **Evidence**: "In this context, each individual subsystem will be a microservice, with all the advantages of independence, decentralization, and scalability. Furthermore, each part will be loosely coupled to the others and fits the description of domain-driven design concepts." (p. 10)

- **Constraint/Pattern**: Passive Caching API Gateway Pattern
- **Implication**: The unified data exchange subsystem operates passively by caching data pushed to it by components rather than actively querying external systems, eliminating direct point-to-point coupling and preventing cascading call failures.
> **Evidence**: "Its main difference from typical implementations of such solutions is that it does not directly access other systems, but rather waits for them to provide information and caches it." (p. 6)

### 4. Context Assumptions

- **Assumption**: Incompressibility of Complex Legacy Industrial Software
> **Evidence**: "An industrial digital twin presents a different situation: it may include large software systems that cannot be rationally decomposed into smaller services or rewritten within a single technology stack." (p. 2)

- **Assumption**: HTTP Protocol Dependency in Legacy Industrial Runtimes
> **Evidence**: "However, since the digital twin will always be based on existing solutions, the external interface must rely on the HTTP protocol, as existing software and its runtimes may not be adapted to implementations using more modern alternatives." (p. 10)
```

