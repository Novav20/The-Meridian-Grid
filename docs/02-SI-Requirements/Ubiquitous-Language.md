# Ubiquitous Language

---
## Bounded Context: Data Transport & Semantics (Sub-RQ 1)

This document defines the ubiquitous language for the **Data Transport & Semantics** (Sub-RQ 1) bounded context of The Meridian Grid (TMG). All definitions are synthesized directly from domain research extractions.

### Core Architectural Patterns

- **Unified Namespace (UNS)**
  - *Definition:* A data-centric architecture and structured model for organizing industrial, operational, and business data into a unified, hierarchically structured, and event-driven information space. It serves as a Single Source of Truth (SSOT) allowing seamless enterprise-wide data flow using an agreed-upon semantic hierarchy. While raw MQTT UNS relies on manual topic governance, Sparkplug B enforces strict payload contracts and lifecycle states within the namespace.
  - *Aliases / Related:* SSOT
  - *Traceability:* [[Freitas_et_al_2025]], [[Pillai_et_al_2026]], [[Senk_et_al_2026]]

- **Digital Twins (DT)**
  - *Definition:* Comprehensive, real-time virtual replicas of physical assets, processes, or entire systems (often built with photogrammetry and 3D scanning) that continuously mirror their real-world counterparts by integrating live sensor data, engineering models, and historical records to enable remote monitoring, simulation, predictive maintenance, and optimization.
  - *Aliases / Related:* DT
  - *Traceability:* [[Badoi_et_al_2026]], [[Koprov_et_al_2025]], [[Pillai_et_al_2026]]

- **Device Twins (DvT)**
  - *Definition:* Digital models of individual hardware devices that facilitate remote monitoring, configuration, and life-cycle management, providing granular visibility and synchronization of device states governed by Desired, Reported, and Tag metadata properties.
  - *Aliases / Related:* DvT
  - *Traceability:* [[Badoi_et_al_2026]]

- **Digital Shadow**
  - *Definition:* A strictly unidirectional (read-only) data stream from physical assets to supervisory systems designed for real-time monitoring by continuously streaming operational variables without enabling direct upstream control or manipulation of the physical equipment.
  - *Aliases / Related:* Unidirectional Digital Twin
  - *Traceability:* [[Koprov_et_al_2025]], [[Pillai_et_al_2026]]

- **Cyber-Physical Systems (CPS)**
  - *Definition:* Engineered systems built from and dependent upon the seamless integration of computation and physical components, combining computing, storage, and communication properties of cyberspace to monitor and control physical features.
  - *Aliases / Related:* CPS
  - *Traceability:* [[Freitas_et_al_2025]]

- **Industrial Metaverse (IM)**
  - *Definition:* An advanced stage of digital transformation characterized by ultra-realistic, persistent, accessible, pervasive, and potentially decentralized virtual environments that blend real-world operations with virtual environments using technologies such as augmented reality and digital twins.
  - *Aliases / Related:* IM
  - *Traceability:* [[Koprov_et_al_2025]]

- **Universal Scene Description (USD)**
  - *Definition:* An extensible 3D scene description framework developed by Pixar that serves as the foundation for NVIDIA Omniverse by encapsulating asset geometry, visual properties, physics-driven behaviors, and relationships.
  - *Aliases / Related:* USD
  - *Traceability:* [[Koprov_et_al_2025]]

- **Profiles**
  - *Definition:* Reusable, object-oriented semantic models that contextually describe sensors, equipment, and processes while defining how variables relate to one another to eliminate custom middleware configuration.
  - *Aliases / Related:* Semantic Models
  - *Traceability:* [[Koprov_et_al_2022]]

- **Address Space Model**
  - *Definition:* The structural definition of the building blocks used to create Information Models, which are essential for constructing the Address Space of an OPC UA server.
  - *Aliases / Related:* Information Models
  - *Traceability:* [[Freitas_et_al_2025]]

- **Predictive and Preventive Maintenance (PPM)**
  - *Definition:* A core operational efficiency strategy in Industry 4.0 that leverages real-time sensor measurements, analytics, and virtual modeling to anticipate failures, minimize unplanned stoppages, and optimize maintenance responsiveness.
  - *Aliases / Related:* PPM
  - *Traceability:* [[Pillai_et_al_2026]]

- **Interoperability**
  - *Definition:* The ability to share and exchange information using a common syntax and semantics to meet an application-specific functional relationship across a common interface.
  - *Aliases / Related:* 
  - *Traceability:* [[Freitas_et_al_2025]]


### Protocols & Telemetry Models

- **Message Queuing Telemetry Transport (MQTT)**
  - *Definition:* An event-based, message-oriented, asynchronous publish–subscribe protocol designed for reliable one-to-many machine-to-machine (M2M) communications.
  - *Aliases / Related:* MQTT
  - *Traceability:* [[Jaloudi_2019]]

- **Sparkplug B**
  - *Definition:* A specification extending MQTT that introduces a standardized topic namespace, defined birth and death messages, structured payload data using the Protocol Buffers (Protobuf) format, and state management mechanisms for edge nodes and devices.
  - *Aliases / Related:* MQTT SpB
  - *Traceability:* [[Senk_et_al_2026]]

- **MODBUS TCP**
  - *Definition:* A byte-oriented, open de facto standard industrial communication protocol used for data exchange between embedded systems, devices, and industrial applications via a polling request–response mechanism.
  - *Aliases / Related:* 
  - *Traceability:* [[Jaloudi_2019]]

- **Constrained Application Protocol (CoAP)**
  - *Definition:* An application-layer, document-oriented protocol dedicated to communications with constrained devices in IPv6-based Internet of Things (IoT) infrastructures, operating asynchronously over connectionless UDP.
  - *Aliases / Related:* CoAP
  - *Traceability:* [[Jaloudi_2019]]

- **CloudConnects (CC)**
  - *Definition:* Hardware communication processors installed directly in control boxes to translate diverse local PLC protocols into unified OPC UA interfaces.
  - *Aliases / Related:* CC
  - *Traceability:* [[Huusom_et_al_2025]]

- **vNode**
  - *Definition:* A central real-time data hub and industrial gateway that acts as a middleware bridge to compile, organize, and redistribute process data while managing access permissions.
  - *Aliases / Related:* IIoT gateway
  - *Traceability:* [[Huusom_et_al_2025]]

- **Edge of Network Node (EoN)**
  - *Definition:* Devices that convert proprietary industrial protocol data and analog signals into the standardized MQTT Sparkplug data format to enable legacy or non-communicative machinery.
  - *Aliases / Related:* EoN, Edge of Nodes
  - *Traceability:* [[Koprov_et_al_2022]]

- **Relational Historian**
  - *Definition:* An SQL-based persistence store (e.g., PostgreSQL) coupled with an intermediate message broker to ingest and archive operational telemetry without altering database schemas.
  - *Aliases / Related:* 
  - *Traceability:* [[Huusom_et_al_2025]]

- **Round-Trip Time (RTT)**
  - *Definition:* The total time required to complete the entire sequence of sending and acknowledging a message between the client and the broker/server.
  - *Aliases / Related:* RTT
  - *Traceability:* [[Freitas_et_al_2025]]


### Network Topologies, Resilience & Security

- **Slow Subscribers**
  - *Definition:* A denial-of-service attack in the MQTT protocol that occurs on a single compromised node with minimal subscription permissions and overwhelms an MQTT broker with unsolicited subscription requests, causing it to become a single point of failure.
  - *Aliases / Related:* 
  - *Traceability:* [[Liu_et_al_2023]]

- **Remistry**
  - *Definition:* A Resilient Middleware for Message Queue Telemetry Transport framework that detects misconfigurations and provides granular handling of resource commitment errors, especially out-of-memory problems, to mitigate Slow Subscribers attacks.
  - *Aliases / Related:* Resilient Middleware for MQTT
  - *Traceability:* [[Liu_et_al_2023]]

- **Multi-processing (MP)**
  - *Definition:* An operating system task scheduling approach defined as the execution of isolated, concurrent code instances, distinguished from multi-threading by its adherence to the isolation principle.
  - *Aliases / Related:* MP
  - *Traceability:* [[Liu_et_al_2023]]

- **Media Access Control Security (MACsec)**
  - *Definition:* A Layer 2 data link layer protocol that encrypts Ethernet frames and protects against tampering and replay on local area networks without altering higher-layer protocols.
  - *Aliases / Related:* MACsec, IEEE 802.1AE
  - *Traceability:* [[Narayanan_et_al_2026]]

- **DNP3 Secure Authentication (SA)**
  - *Definition:* A standard-based security overlay for the Distributed Network Protocol version 3 that adds a challenge–response mechanism for origin authentication and message integrity using symmetric or public keys, but does not encrypt telemetry data.
  - *Aliases / Related:* DNP3-SA
  - *Traceability:* [[Narayanan_et_al_2026]]

- **Application-Level Encryption**
  - *Definition:* Cybersecurity protections integrated directly into specific industrial control protocols, terminating at the communicating endpoints and configured per individual application.
  - *Aliases / Related:* 
  - *Traceability:* [[Narayanan_et_al_2026]]

---
## Bounded Context: Visualization & Low-Code HMI (Sub-RQ 2) 
### Rendering & Visual Models 
### Dynamic Layout & Declarative Schemas
---

## Bounded Context: Visualization & Low-Code HMI (Sub-RQ 2)

### Rendering & Vector Graphics Models

- **Custom Widget Template**
  - *Definition:* An SVG-based graphic design created using an editor that can be uploaded to the platform and instantiated into interactive, event-driven dashboard widgets or complex synoptics by connecting reading and writing variables to WebSockets.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Bellini_et_al_2022]]

- **Grid Display Method**
  - *Definition:* A 2D grid visualization mode adopted for monitoring mobile robots and AGVs on web interfaces to minimize browser computing resource consumption compared to 3D virtual reality.
  - *Aliases / Related:* 2D Grid
  - *Traceability:* [[Guo_et_al_2022]]

- **Conventional Graphical Symbols (CGS)**
  - *Definition:* Graphical representations of equipment connected according to the main electrical diagram, whose visual properties change based on input signals from associated equipment.
  - *Aliases / Related:* CGS
  - *Traceability:* [[Dobrokhotov_et_al_2025]]

- **Mnemonic Diagram**
  - *Definition:* Main elements of automated workstations that display the primary equipment and operating conditions of an electrical installation.
  - *Aliases / Related:* Synoptic
  - *Traceability:* [[Dobrokhotov_et_al_2025]]

- **Protocol-Coupling Map Symbol**
  - *Definition:* A map symbol model integrating vector graphic data, metadata of sensor data, and a mapping profile to enable a single symbol to visually express multiple internal states of a remote geo-device.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Jiao_et_al_2018]]

### Declarative UI & Low-Code Composition

- **Snap4Industry**
  - *Definition:* An IoT development environment and framework extending Snap4City for implementing the control and supervision of complex industrial plants with multiple DCS/SCADA systems and supply chains under the Industry 4.0 paradigm.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Bellini_et_al_2022]]

- **Optimized Production Planner**
  - *Definition:* A Python-based optimization algorithm implementing mathematical and chemical formulas to compute feasible production settings, predictions, and plans for 24 to 48 hours in advance.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Bellini_et_al_2022]]

- **WYSIWYG Web-based SCADA**
  - *Definition:* A web-based supervisory system where users construct application screens using drag-and-drop instrument icons and parameter configuration areas.
  - *Aliases / Related:* Drag-and-drop interface
  - *Traceability:* [[Guo_et_al_2022]]

- **Substation Configuration Description (SCD) File**
  - *Definition:* A text file created using substation configuration language (SCL) in XML format that contains the description of primary equipment, its location, connections, control and protection functions, and signals.
  - *Aliases / Related:* SCD File
  - *Traceability:* [[Dobrokhotov_et_al_2025]]

- **SyTrack SCADA System**
  - *Definition:* A SCADA system utilizing SVG format for describing mnemonic diagrams and dynamicizing their elements based on signal connections.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Dobrokhotov_et_al_2025]]

- **Pipeline**
  - *Definition:* A continuous processing and automation graph executed in a dedicated thread to evaluate alarms, convert raw values into physical quantities, and execute control logic on sensor streams.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Grigat_et_al_2026]]

- **Doberview**
  - *Definition:* A web-based graphical user interface built on Node.js and Bootstrap providing live visualization, historical data inspection, and interactive configuration tools.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Grigat_et_al_2026]]

- **IMetaData Interface**
  - *Definition:* An object-oriented interface declared in the symbol system that extracts metadata information from protocol driver classes during symbol construction.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Jiao_et_al_2018]]

- **IDataParser Interface**
  - *Definition:* An object-oriented interface executing on the server side that deserializes incoming raw geo-sensor data frames into lightweight JSON format for real-time processing and visualization.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Jiao_et_al_2018]]

- **Local HMI**
  - *Definition:* A supervisory interface developed to provide direct read access to PLC memory and animated process visualizations.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Villamar_et_al_2025]]

- **Remote HMI**
  - *Definition:* A web-based supervisory interface that mirrors local monitoring by retrieving process state from a database via REST APIs.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Villamar_et_al_2025]]

### Situational Awareness & Cognitive Ergonomics

- **Information Presentation Speed**
  - *Definition:* The movement velocity (measured in degrees of visual angle per second, °/s) of dynamic visual elements and graphics across a supervisory control and data acquisition interface display.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Tong_et_al_2026]]

- **Situation Awareness Rating Technique (SART)**
  - *Definition:* A subjective self-assessment rating scale that evaluates an operator's situational awareness across attentional demand, attentional supply, and understanding dimensions.
  - *Aliases / Related:* SART
  - *Traceability:* [[Tong_et_al_2026]]

- **Blink Rate**
  - *Definition:* An ocular metric calculating the number of eye blinks per minute to assess operator visual fatigue and attentional strain during dynamic visual monitoring.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Tong_et_al_2026]]

- **Critical Flicker Fusion (CFF)**
  - *Definition:* A physiological threshold measuring the temporal resolution of the visual system that decreases as visual fatigue accumulates during display tasks.
  - *Aliases / Related:* CFF
  - *Traceability:* [[Tong_et_al_2026]]

- **ALARMS**
  - *Definition:* A modular multi-agent framework mapping Endsley’s Situational Awareness levels and IDA macrocognition to specialized cognitive agents drawing on Signal Detection Theory and vigilance research.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Verdejo_et_al_2026]]

- **Cognitive Mirror**
  - *Definition:* An AI agent paradigm designed to explicitly support human metacognition, reflect and challenge operator reasoning, and maintain human oversight to prevent deskilling and automation bias.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Verdejo_et_al_2026]]

- **Analysis Agent**
  - *Definition:* An agent implementing Level 1 and lower-Level 2 situation awareness by transforming heterogeneous sensor and log data into a machine- and human-consumable 5W+H situation model.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Verdejo_et_al_2026]]

- **Locutor Agent**
  - *Definition:* The primary human-AI interface operating as a cognitive mirror, combining LLM-based natural language understanding/generation and XAI to generate situation reports and challenge operator assumptions.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Verdejo_et_al_2026]]

- **Anticipation Agent**
  - *Definition:* An agent implementing Level 3 situation awareness and weak-signal analysis by learning baselines of normal behavior and detecting explicit anomalies as well as absences of expected events.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Verdejo_et_al_2026]]

- **Risk Manager Agent**
  - *Definition:* An agent embodying decision support by mapping events and anomalies onto critical assets, computing probabilistic risk, and generating structured mitigation recommendations.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Verdejo_et_al_2026]]

- **Simulation Agent**
  - *Definition:* An agent operationalizing operational testing, what-if analysis, and operator training using discrete-event, agent-based, or digital-twin simulation.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Verdejo_et_al_2026]]

### Web Runtime & Communication Architecture

- **IoT App**
  - *Definition:* Node.js processes developed in Node-RED using Snap4City MicroServices that run on IoT Edge, Cloud, or mobile devices to execute data ingestion, workflows, data analytics, and user interface business logic.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Bellini_et_al_2022]]

- **MQTT Protocol**
  - *Definition:* A lightweight Publish/Subscribe messaging protocol designed for IoT environments with low power consumption and limited network bandwidth that routes messages through a central broker.
  - *Aliases / Related:* MQ telemetry transport
  - *Traceability:* [[Guo_et_al_2022]]

- **Four-Level MQTT Topic Structure**
  - *Definition:* A hierarchical topic taxonomy comprising MQTT serial number, Device name, Input/output direction, and Data type layers to organize multi-controller messages.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Guo_et_al_2022]]

- **Doberman**
  - *Definition:* A lightweight, modular, and open-source slow control system designed for small- to medium-scale physics experiments.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Grigat_et_al_2026]]

- **Monitor**
  - *Definition:* The fundamental software building block in Doberman that manages multiple threads executing tasks independently and sleeping for configurable intervals.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Grigat_et_al_2026]]

- **Hypervisor**
  - *Definition:* The central coordinating Monitor process that supervises component health, routes inter-component commands via publish-subscribe messaging, and mediates sensor data distribution.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Grigat_et_al_2026]]

- **Geo-Sensor Message Broker**
  - *Definition:* A server-side communication middleware providing data acquisition and transfer services to bridge remote geo-sensors and map clients for real-time data visualization.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Jiao_et_al_2018]]

- **Spatial-Communication Protocol**
  - *Definition:* A full-duplex JSON-based communication protocol operating over Socket or WebSocket that synchronizes map clients and the message broker through bounding box updates and filtered sensor data pushes.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Jiao_et_al_2018]]

- **Digital Twin (DT)**
  - *Definition:* An up-to-date virtual representation of a physical object or process with two-way data communication used for monitoring, simulation, and optimization.
  - *Aliases / Related:* DT
  - *Traceability:* [[Koltsova_et_al_2026]]

- **Composite Architecture**
  - *Definition:* A software architecture constructed from a set of loosely coupled, independently developed, deployed, and scalable components that interact exclusively through clearly defined interfaces.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Koltsova_et_al_2026]]

- **Unified Data Exchange Subsystem**
  - *Definition:* An architectural component serving as an API gateway that abstracts disparate systems, introduces persistent versioned contracts, and ensures a consistent interaction environment without taking ownership of subject data.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Koltsova_et_al_2026]]

- **High Internal Cohesion and Loose External Coupling**
  - *Definition:* Architectural principles where a component internally groups functions sharing a common responsibility and lifecycle, while externally interacting through a limited set of explicit contracts independent of internal implementations.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Koltsova_et_al_2026]]

- **Cyber-Physical Production Systems (CPPS)**
  - *Definition:* Smart manufacturing environments where digital technologies integrate to enable autonomous decision-making and adaptive control.
  - *Aliases / Related:* CPPS
  - *Traceability:* [[Villamar_et_al_2025]]

- **Hybrid IIoT Architecture**
  - *Definition:* An architecture coupling a virtual process simulation with physical industrial equipment driven by a PLC to enable modular monitoring and control.
  - *Aliases / Related:* N/A
  - *Traceability:* [[Villamar_et_al_2025]]

