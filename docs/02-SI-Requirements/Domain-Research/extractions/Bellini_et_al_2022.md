---
paper_id: "Bellini_et_al_2022"
query_id: "Q02"
title: "High level control of chemical plant by industry 4.0 solutions"
authors: "Bellini P.; Cenni D.; Mitolo N.; Nesi P.; Pantaleo G.; Soderi M."
year: 2022
doi: "10.1016/j.jii.2021.100276"
keywords: ["Data driven", "Industry 4.0", "IoT", "Synoptics"]
source_pdf: "High level control of chemical plant by industry 4.0 solutions.pdf"
extraction_date: "2026-09-20"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Snap4Industry
- **Definition**: An IoT development environment and framework extending Snap4City for implementing the control and supervision of complex industrial plants with multiple DCS/SCADA systems and supply chains under the Industry 4.0 paradigm.
> **Evidence**: "In this paper, Snap4Industry with its IoT development environment and framework for implementing the Control and Supervision of complex plant with multiple DCS and/or chains in the view of Industry 4.0 is presented." (p. 1)

- **Term**: IoT App
- **Definition**: Node.js processes developed in Node-RED using Snap4City MicroServices that run on IoT Edge, Cloud, or mobile devices to execute data ingestion, workflows, data analytics, and user interface business logic.
> **Evidence**: "IoT Apps are Node.JS processes developed in Node-RED using a large set of Snap4City MicroServices for exploiting the architecture services on: storage, search and retrieval, dashboards, synoptics, user interface controls, data analytics, transcoding, semantic search, etc." (p. 5)

- **Term**: Custom Widget Template
- **Definition**: An SVG-based graphic design created using an editor that can be uploaded to the platform and instantiated into interactive, event-driven dashboard widgets or complex synoptics by connecting reading and writing variables to WebSockets.
> **Evidence**: "Thus, our approach started with the possibility of using the design of SVG graphics as a generic tool for creating Custom Widget Templates that can be instantiated to create both single widget and complex Synoptics for Dashboards." (p. 10)

- **Term**: Optimized Production Planner
- **Definition**: A Python-based optimization algorithm implementing the mathematical and chemical formulas of the chemical production process to compute feasible production settings, predictions, and plans for 24 to 48 hours in advance.
> **Evidence**: "In ALTAIR, the Production Plan is decided every day taking the best among Possible Plans computed by mean of an Optimized Production Planner which implements the mathematic/chemical formula describing the chemical production process, and by taking in input a number of parameters, and corrective aspects." (p. 6)

### 2. Domain Rules and Invariants

- **Rule**: Dual 24/48-Hour Rolling Production Plan Requirement
- **Mechanism**: The system computes production plans for 24 hours under normal weekdays, but extends planning to a 2-day horizon (and up to 3 days on Fridays) so that a valid recovery plan remains available if subsequent daily plan computations fail or no new orders arrive over the weekend.
> **Evidence**: "Please note that, even if the production plan is typically performed once a day, the planning is always performed for 2 days to be sure to have a recovery plan in the case in which the next day play would fail for some reason." (p. 7)

- **Rule**: Asynchronous Event-Driven Loop Speed Limits for Synoptics
- **Mechanism**: Synoptics bound to storage-driven loops sustain up to 5 changes/second without message loss, while synoptics directly connected to Node-RED IoT App WebSocket servers sustain up to 20 changes/second (40 WS messages/second), and direct browser-to-WS server shortcuts achieve up to 2,500 messages/second.
> **Evidence**: "From the measures performed the round trip is performed at maximum of 20 changes per second without missing data. Which means 40 WS messages per second (change the lamp and change the slider)." (p. 10)

- **Rule**: Formal IoT Device Model Data Structure Registration Invariant
- **Mechanism**: Every incoming data message with multiple attributes must be registered as an IoT Device instance adhering to a formalized data model saved in the IoT Directory and Knowledge Base, allowing dynamic message instances to reference a single ServiceURI and optimize storage.
> **Evidence**: "The formal registration of the IoT Device data model is performed into the IoT Directory which saves the model into the KB. Once registered, the received IoT messages by an IoT App can be sent into the system via the IoT Broker which save them automatically into the Data Storage." (p. 7)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Uniform Node-RED MicroService Programming Pattern Across Edge and Cloud
- **Implication**: The system adopts Node-RED supplemented with specialized Snap4City MicroServices across field devices, edge gateways, and cloud nodes, establishing a single uniform visual programming paradigm for data ingestion, analytics, workflows, and UI logic.
> **Evidence**: "The adoption of a uniform programming model (at least on Edge and Cloud) provides more flexibility in moving the processes and reusing the code, thus reducing the maintenance costs and increasing reliability." (p. 2)

- **Constraint/Pattern**: Kafka-Distributed Secure WebSocket Architecture for Real-Time UI Synchronization
- **Implication**: Real-time UI widgets and SVG synoptics communicate bidirectionally with backend processes over WebSocket Secure (WSS), with Apache Kafka handling pub/sub distribution to maintain low latency across multiple client browsers and mobile apps.
> **Evidence**: "This implies that a large number of Web Sockets may be needed to connect all clients. To this end, Kafka has been adopted in Snap4Industry for distributing messages via those Web Sockets." (p. 7)

### 4. Context Assumptions

- **Assumption**: Continuous 24/7/365 Chemical Plant Operation with Batch Transportation Windows
> **Evidence**: "A typical chemical production plant presents a continuous production H24/7, 365 days/year, taking into account prime matter arriving at the plant and the delivering of the resulting products outside (the delivering is performed by big trucks/tanks 5 days a week, at the working hours)." (p. 5)

- **Assumption**: Unsuitability of Legacy SCADA/DCS for Granular GDPR-Compliant External Access
> **Evidence**: "This approach is presently very hard to be implemented with SCADA/DCS solutions, that in most cases are not web based and do not provide sophisticated access control." (p. 2)



