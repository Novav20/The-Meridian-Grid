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