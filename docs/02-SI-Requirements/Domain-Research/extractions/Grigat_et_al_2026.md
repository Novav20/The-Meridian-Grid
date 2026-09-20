---
paper_id: "Grigat_et_al_2026"
query_id: "Q03"
title: "Doberman: a modular and distributed slow control system for small- to medium-scale experiments"
authors: "Grigat J.; Masson D.; Schumann M."
year: 2026
doi: "10.1088/1748-0221/21/07/P07011"
keywords: ["Control and monitor systems online", "Detector control systems (detector and experiment monitoring and slow-control systems, architecture, hardware, algorithms, databases)", "Software architectures (event data models, frameworks and databases)"]
source_pdf: "Doberman: a modular and distributed slow control system for small- to medium-scale experiments.pdf"
extraction_date: "2026-09-20"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Doberman
- **Definition**: A lightweight, modular, and open-source slow control system designed for small- to medium-scale physics experiments.
> **Evidence**: "We present Doberman (Detector OBsERving and Monitoring ApplicatioN), a lightweight, modular, and open-source slow control system designed for small- to medium-scale physics experiments." (p. 1)

- **Term**: Monitor
- **Definition**: The fundamental software building block in Doberman that manages multiple threads executing tasks independently and sleeping for configurable intervals.
> **Evidence**: "The fundamental building block of Doberman is the Monitor class. A Monitor manages multiple threads that run independently: each thread executes a task (e.g. reading out a sensor) and then sleeps for a configurable interval." (p. 4)

- **Term**: Hypervisor
- **Definition**: The central coordinating Monitor process that supervises component health, routes inter-component commands via publish-subscribe messaging, and mediates sensor data distribution.
> **Evidence**: "This role is served by the Hypervisor, which supervises component health, routes commands, and mediates data distribution." (p. 5)

- **Term**: Pipeline
- **Definition**: A continuous processing and automation graph executed in a dedicated thread to evaluate alarms, convert raw values into physical quantities, and execute control logic on sensor streams.
> **Evidence**: "Pipelines implement continuous processing and automation on top of sensor data. They are used to detect alarm conditions, compute derived quantities, and execute control logic (e.g. actuating valves)." (p. 7)

- **Term**: Doberview
- **Definition**: A web-based graphical user interface built on Node.js and Bootstrap providing live visualization, historical data inspection, and interactive configuration tools.
> **Evidence**: "Doberview is a web-based graphical user interface developed as the primary user-facing component of Doberman. It provides live visualization of slow control data, access to historical measurements, and interactive tools to configure sensors, pipelines, and alarms." (p. 9)

### 2. Domain Rules and Invariants

- **Rule**: Hypervisor Failure Decoupling Invariant
- **Mechanism**: If the central Hypervisor process experiences a temporary failure or restart, individual Monitor processes continue running independently, maintaining device readout and writing time-series data directly without data loss.
> **Evidence**: "In the event of a temporary failure of the Hypervisor itself, running Monitors continue operating independently, including ongoing device readout and data storage. After the Hypervisor is restarted, Monitors automatically resume coordinated operation. Since measurement data are written directly to the time-series database, no data are lost during such interruptions." (p. 6)

- **Rule**: Command Execution Acknowledgment Protocol
- **Mechanism**: Commands broadcast across components via ZeroMQ are tagged with unique identifiers/hashes, and receiving DeviceMonitors must explicitly issue an acknowledgment message containing the hash back to the sender after translation and execution.
> **Evidence**: "Each command is associated with a unique identifier and is acknowledged by the receiving Monitor after successful execution." (p. 6)

- **Rule**: Multi-Level Alarm Escalation and Auto-Silence Rule
- **Mechanism**: Alarms evaluate a base severity level and escalate if repeated notifications go unacknowledged, while an auto-silence timer automatically suppresses notification flooding after an initial alert.
> **Evidence**: "Doberman uses a leveled alarm concept: each alarm has a configured base level (from the sensor configuration) and an escalation level that increases if repeated alarm messages are sent without the alarm being cleared." (p. 8)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Distributed Multi-Host Deployment Topology
- **Implication**: DeviceMonitors can be placed on secondary hosts near physical hardware while databases and coordination processes run on a main host, ensuring host-level failures only isolate locally connected sensors without crashing global system monitoring.
> **Evidence**: "Distributing device readout across multiple hosts improves robustness and operational flexibility: a failure of a single host affects only the subset of sensors connected to that machine, while the remaining system continues to operate normally." (p. 3)

- **Constraint/Pattern**: Dual Data Sourcing Pattern via Broker or Time-Series Database
- **Implication**: Pipelines can ingest live data directly from the Hypervisor's in-memory ZeroMQ data broker for sub-25 ms processing, or query InfluxDB for historical time-series contexts at ~100 ms processing latency.
> **Evidence**: "In addition to command routing, the Hypervisor runs a data broker that distributes fresh sensor values to multiple consumers (e.g. pipelines) without requiring repeated database queries. As shown in Figure 2, pipelines can source data either from the broker (preferred for efficiency and reduced database load) or from the time-series database." (p. 6)

- **Constraint/Pattern**: Directed Acyclic Node-Graph Pipeline Pattern
- **Implication**: Automation logic is structured into directed graphs containing source, intermediate, and sink nodes with internal buffers and MergeNodes to support time-aligned multi-stream evaluations and default conservative fail-safe states.
> **Evidence**: "Conceptually, pipelines are represented as directed graphs of nodes. Source nodes ingest data either from the live broker stream or from the database; intermediate nodes perform operations such as filtering, threshold checks, derivatives, or arbitrary expressions; and sink nodes write derived quantities to the database or trigger control actions." (p. 7)

### 4. Context Assumptions

- **Assumption**: External Remote Heartbeat Dependency for Main Host Outages
> **Evidence**: "To protect against rare but critical failure modes (e.g. power outage of the main server or network failures), Doberman supports an external heartbeat mechanism: the Hypervisor periodically updates a file on a remote system (in a different building, institution etc.)." (p. 6)

- **Assumption**: GitHub OAuth Organizational Authentication Sufficiency
> **Evidence**: "Authentication can optionally be enabled via GitHub OAuth, granting write access to members of a designated GitHub organization while allowing unrestricted read-only access in less restrictive deployments. This approach has proven to be low-maintenance, as most collaborations already maintain a GitHub organization for code sharing." (p. 9)
```

