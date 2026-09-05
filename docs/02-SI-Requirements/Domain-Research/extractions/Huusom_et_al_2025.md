---
paper_id: "Huusom_et_al_2025"
query_id: "Q01"
title: "Building a scalable digital infrastructure for a (bio)chemical engineering pilot plant: A case study from DTU"
authors: "Huusom J.K.; Jones M.N.; Kager J.; Dam-Johansen K.; Dreyer J.A.H."
year: 2025
doi: "10.1016/j.dche.2025.100269"
keywords: ["Digital infrastructure", "Digitalization", "Pilot plant", "Real-time data", "SCADA", "Unit operation"]
source_pdf: "Building a scalable digital infrastructure for a (bio)chemical engineering pilot plant: A case study from DTU.pdf"
extraction_date: "2026-09-04"
---

### 1. Ubiquitous Language

- **Term**: CloudConnects (CC)
- **Definition**: Hardware communication processors installed directly in control boxes to translate diverse local PLC protocols into unified OPC UA interfaces.
> **Evidence**: "In the present case study, the conversion was achieved via Siemens CloudConnects (CC), which were directly installed in the electronic control boxes of the individual unit operations." (p. 4)

- **Term**: vNode
- **Definition**: A central real-time data hub and industrial gateway that acts as a middleware bridge to compile, organize, and redistribute process data while managing access permissions.
> **Evidence**: "vNode serves as this central real-time data hub. Although optional and replaceable by other middleware, vNode is a commercial software platform originally designed as an Industrial Internet of Things (IIoT) gateway, capable of bridging various industrial protocols and cloud environments." (p. 5)

- **Term**: TimescaleDB
- **Definition**: A database extension for PostgreSQL that provides specialized time-series indexing and partition structures to optimize database query speed and storage management.
> **Evidence**: "The database also includes the TimescaleDB extension, which adds time-series indexing and partitioning features to improve performance and manageability for time-stamped process data." (p. 6)

### 2. Domain Rules and Invariants

- **Rule**: Schema and Code Extensibility Invariant
- **Mechanism**: The architecture decouples data ingestion and structure from the database layer, allowing new hardware or tags to be added dynamically without requiring alterations to the relational schema or parsing scripts.
> **Evidence**: "The system is fully extensible: new units or sensors can be added without modifying the database schema or Python code." (p. 1)

- **Rule**: SQLite Retention Limitation
- **Mechanism**: The SCADA local SQLite storage is restricted to retaining only the most recent 30 days of data to limit disk utilization while sustaining real-time user-interface trends.
> **Evidence**: "Therefore, the SQLite database is configured to store only the most recent 30 days of data, primarily to support real-time plotting within the SCADA web interface." (p. 5)

- **Rule**: Operational Recording Execution
- **Mechanism**: Activating the "Record" function inside the SCADA web interface changes the boolean state tag `is_logging` to true, which triggers vNode to broadcast an MQTT packet that instructs the ingestion service to parse and commit telemetry to the PostgreSQL database.
> **Evidence**: "This sets the WinCC Unified tag is_logging to true, which is then detected by vNode and forwarded as an MQTT message. This signal triggers the real-time logging of data from the corresponding unit operation into the central PostgreSQL database (see Section 3.3)." (p. 5)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Process-to-Cloud Network Isolation
- **Implication**: Physical control networks containing PLCs and HMIs are separated from the campus enterprise network using dual-homed gateway interfaces, preventing direct device exposure to security risks.
> **Evidence**: "Each CC uses two separate networks, one being called the process side and the other being the cloud side (Fig. 2). The process side is connected to the internal network of the unit operation, e.g., the HMI screen and the PLC. The cloud side is connected to the university network. Thus, no reconfiguration of the process network is required and the process hardware itself does not need to be connected to the university network, which improves IT security." (p. 4)

- **Constraint/Pattern**: Redundant Dual-Client Connectivity
- **Implication**: The SCADA runtime and vNode gateway maintain parallel, concurrent connections to the field gateways, ensuring continuous process visualization and control even during a failure of the centralized data pipeline.
> **Evidence**: "Although it would have been technically possible to route all data through a single system, for example, having SCADA retrieve all data from vNode or vice versa, both systems were connected directly to the CloudConnects to ensure redundancy and improve resilience." (p. 4)

- **Constraint/Pattern**: Automated GitLab CI/CD Containerization
- **Implication**: Host administration is strictly programmatic; updates to container files or Kubernetes pod configurations are checked into a central code repository and deployed via automated runners to eliminate errors from manual terminal interventions.
> **Evidence**: "To manage software deployment, Continuous Integration and Continuous Deployment (CI/CD) pipelines were set up, linked to a GitLab repository... This approach avoids ad hoc command-line access to the server, which can lead to cluttered environments, inconsistent deployments, or configuration errors." (p. 6)

### 4. Context Assumptions

- **Assumption**: VPN-Restricted Infrastructure Perimeter
> **Evidence**: "All services are self-hosted on DTU-managed servers, while remote access is provided via the institutional VPN rather than exposing endpoints to the public internet." (p. 2)

- **Assumption**: Non-Continuous Batch Operations
> **Evidence**: "However, at the DTU Pilot Plant, where experiments are performed in discrete batches, often as part of educational courses, continuous logging is neither necessary nor practical." (p. 5)