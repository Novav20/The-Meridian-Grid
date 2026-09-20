---
paper_id: "Villamar_et_al_2025"
query_id: "Q03"
title: "An Open-Source Web-Based Approach to Industrial Supervision and Data Acquisition in the Context of Industry 4.0"
authors: "Villamar R.; Proaño P.; Cuenca Sánchez A.; Tipan J.; Pillajo R.; Quito Carrión A."
year: 2025
doi: "10.3390/engproc2025115023"
keywords: ["factory IO simulation", "hybrid virtual–physical systems", "Industry 4.0", "open source web supervision", "open-source supervision systems", "Python MySQL integration"]
source_pdf: "An Open-Source Web-Based Approach to Industrial Supervision and Data Acquisition in the Context of Industry 4.0.pdf"
extraction_date: "2026-09-20"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Cyber-Physical Production Systems (CPPS)
- **Definition**: Smart manufacturing environments where digital technologies integrate to enable autonomous decision-making and adaptive control.
> **Evidence**: "At its foundation, this paradigm promotes smart environments where cyber-physical production systems (CPPS) enable autonomous decision-making and adaptive control." (p. 1)

- **Term**: Hybrid IIoT Architecture
- **Definition**: An architecture coupling a virtual process simulation with physical industrial equipment driven by a PLC to enable modular monitoring and control.
> **Evidence**: "The system adopts a hybrid IIoT architecture that couples a Factory IO glass-process simulation—structured into reception, production, and dispatch—with a physical threephase induction motor (cooling zone) driven by a Modicon M580 PLC programmed in Control Expert." (p. 2)

- **Term**: Local HMI
- **Definition**: A supervisory interface developed in Control Expert providing direct read access to PLC memory and animated process visualizations.
> **Evidence**: "Local HMI: Developed in Control Expert, it provides direct access to PLC variables with animated views of each process stage and motor operation." (p. 5)

- **Term**: Remote HMI
- **Definition**: A web-based supervisory interface implemented in React and Node.js that mirrors local monitoring by retrieving process state from a database via REST APIs.
> **Evidence**: "Remote HMI: Implemented using React and Node.js, it mirrors the local interface and retrieves data from MySQL via REST APIs." (p. 5)

### 2. Domain Rules and Invariants

- **Rule**: Asynchronous Dual-HMI Synchronization Invariant
- **Mechanism**: Local supervision reads directly and synchronously from PLC memory while remote supervision asynchronously queries a relational database via REST APIs, maintaining concurrent process visualization with sub-second delay.
> **Evidence**: "The local HMI in Control Expert updated instantly from PLC memory (Figure 8), while the remote interface—developed in React and connected via Node.js and MySQL—maintained a sub-second delay (Figure 9)." (p. 6)

- **Rule**: Batch Data Acquisition Register Reading
- **Mechanism**: The Python acquisition service uses batch register polling over Modbus TCP/IP to minimize network overhead and communication latency prior to database insertion.
> **Evidence**: "Batch reading is used to reduce latency and improve performance." (p. 4)

- **Rule**: Process-Stage Partitioned Relational Storage Schema
- **Mechanism**: Database tables are explicitly organized into five process-stage tables (Reception, Production, Dispatch, Motor Variables, Remote Control) to structure time-series data and optimize query performance.
> **Evidence**: "The database is structured into five tables—Reception, Production, Dispatch, Motor Variables, and Remote Control—organized by process stage and optimized for time-series queries (Figure 5)." (p. 4)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Five-Layer Decoupled Industrial Architecture
- **Implication**: System responsibilities are strictly separated across five discrete layers—virtual process, control, communication/acquisition, data storage, and visualization—enabling modular component substitution and platform independence.
> **Evidence**: "As shown in Figure 1, the architecture comprises five layers—(i) virtual process, (ii) control, (iii) communication and acquisition, (iv) data storage, and (v) visualization—enabling modular integration of simulation, control logic, data acquisition, storage, and monitoring." (p. 2)

- **Constraint/Pattern**: Protocol-Agnostic Acquisition Gateway Integration
- **Implication**: A Python service acts as an intermediate gateway between the PLC fieldbus protocol and the relational database, insulating higher-level application layers from hardware-specific communication protocols.
> **Evidence**: "A Python service acquires PLC variables over Modbus TCP/IP and writes them to a MySQL schema organized by process stage; although Modbus TCP/IP was chosen for compatibility, the design remains adaptable to other protocols." (p. 2)

- **Constraint/Pattern**: RESTful Isolation of Remote Clients from Fieldbus Devices
- **Implication**: Remote HMI clients are restricted from accessing PLC fieldbus registers directly, querying data exclusively through Node.js REST APIs to decouple field controllers from external client load.
> **Evidence**: "The local HMI reads directly from the PLC, while the remote interface accesses stored data through Node.js REST APIs, enabling platform-independent supervision." (p. 3)

### 4. Context Assumptions

- **Assumption**: Suitability for Resource-Constrained Small-Scale Environments
> **Evidence**: "This paper addresses the need for accessible and interoperable supervision solutions within the Industry 4.0 paradigm, particularly for small-scale or resource-constrained environments." (p. 1)

- **Assumption**: Perimeter-Based Security Model for Unencrypted Industrial Fieldbuses
> **Evidence**: "Given the use of open-source components and Modbus TCP/IP, cybersecurity is essential, requiring network segmentation, restricted access, encrypted web traffic, and secure database management." (p. 8)
```

