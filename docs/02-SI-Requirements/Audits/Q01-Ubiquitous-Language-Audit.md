---
audit_date: "2026-09-19"
target_artifact: "docs/02-SI-Requirements/Ubiquitous-Language.md"
query_id: "Q01"
prompt_used: "Artifact Grounding and Traceability Audit"
---
### Evidence-Based Research Audit: `Ubiquitous-Language`

#### Summary of Audit Findings

1. **Source Attribution**: 18 of 19 terms are correctly attributed to their respective primary source documents. 1 term (**TimescaleDB**) is misattributed; the linked source (`Huusom_et_al_2025`) discusses a structured SQL database (PostgreSQL) but does not mention or evaluate "TimescaleDB" in the active text.
2. **Conceptual Accuracy & Grounding**: 18 terms are grounded in the active source texts. **TimescaleDB** represents an unsupported technological extrapolation. Minor phrasing variations exist (e.g., **Edge of Nodes** vs. standard Sparkplug B "Edge of Network Node").
3. **Semantic & Architectural Conflicts**:
    - **Digital Twin vs. Digital Shadow vs. Device Twin**: Severe cross-paper divergence exists. Bădoi et al. (2026) distinguish Device Twins (DvT) from system-level Digital Twins (DT, ISO 23247-1:2021 requiring physics-based co-simulation). Koprov et al. (2025) define a Digital Shadow strictly by its one-way data flow (monitoring only). Pillai et al. (2026) conflate Digital Twin and Digital Shadow as identical photogrammetric 3D replicas.
    - **UNS Implementation Models**: Architectural conflict between pure publish/subscribe broker UNS with user-defined topics (Freitas et al., 2025), Sparkplug B ISA-95-structured UNS (Šenk et al., 2026; Koprov et al., 2022), and on-premises middleware/SQL data-hub UNS (`vNode` in Huusom et al., 2025).
    - **Empirical Maintenance Metrics**: Pillai et al. (2026) report empirical field trial results (**42.25% downtime reduction**, **36% MTTR reduction**), whereas Bădoi et al. (2026) report simulation-based target projections (**25–40% downtime reduction**, **30–50% MTTI reduction**).

---

### Master Audit Table

|Item / Term|Attribution Status|Grounding Status|Issues / Discrepancies Found|
|:--|:--|:--|:--|
|**Unified Namespace (UNS)**|Verified|Supported|Architectural conflict across sources regarding schema enforcement (schema-less flexible MQTT strings vs. Sparkplug B Protobuf/ISA-95 vs. OPC UA Address Space vs. SQL relational hub).|
|**Digital Twin (DT)**|Verified|Supported|Conceptual boundary conflict: Bădoi et al. (2026) restrict DT to system-level ISO 23247 co-simulation (delegated offline), Koprov et al. (2025) require two-way control, while Pillai et al. (2026) equate DT with static photogrammetric models.|
|**Device Twin (DvT)**|Verified|Supported|None. Tripartite JSON schema (Desired, Reported, Tags) in Azure IoT Hub is strictly supported.|
|**Digital Shadow**|Verified|Supported|Semantic definition conflict: Koprov et al. (2025) define it by unidirectional data flow (monitoring only), whereas Pillai et al. (2026) treat it as a synonym for photogrammetric 3D scans.|
|**Cyber-Physical Systems (CPS)**|Verified|Supported|None. Verbatim alignment with NSF definition cited in source text.|
|**Industrial Metaverse (IM)**|Verified|Supported|None. Grounded in USD/NVIDIA Omniverse virtual environment integration.|
|**Machine Profiles**|Verified|Supported|None. Grounded in CESMII SMIP profile specifications.|
|**Address Space Model**|Verified|Supported|None. Grounded in OPC UA IEC 62541 building blocks definition.|
|**Predictive & Preventive Maintenance (PPM)**|Verified|Supported|Empirical metric discrepancy: Pillai et al. (2026) report 42.25% downtime / 36% MTTR field reductions; Bădoi et al. (2026) project 25–40% downtime / 30–50% MTTI simulated reductions.|
|**Interoperability**|Verified|Supported|None. Grounded in ISO 16100 definition cited in source.|
|**Message Queuing Telemetry Transport (MQTT)**|Verified|Supported|Payload overhead discrepancy: Jaloudi (2019) notes UTF-8 wrapping doubles payload size for MODBUS frames, while Freitas et al. (2025) demonstrate QoS 2 significantly degrades RTT/throughput.|
|**Sparkplug B**|Verified|Supported|None. Grounded in Topic Namespace (`spBv1.0`), state management (birth/death certificates), and Protobuf payload structures.|
|**MODBUS TCP**|Verified|Supported|None. Grounded in byte-oriented polling request–response specification.|
|**Constrained Application Protocol (CoAP)**|Verified|Supported|None. Grounded in UDP/6LoWPAN document-oriented messaging specification.|
|**CloudConnects (CC)**|Verified|Supported|None. Grounded in hardware communication processors for local PLC-to-OPC UA translation.|
|**vNode**|Verified|Supported|None. Grounded in middleware data-hub and IIoT gateway specification.|
|**Edge of Nodes (EoN)**|Verified|Supported|Terminology variance: Koprov et al. (2022) write "edge of nodes (EoN)", whereas standard Sparkplug B specification and Šenk et al. (2026) use "Edge of Network Node".|
|**TimescaleDB**|**Incorrect**|**Hallucinated**|**Not addressed in the active source(s).** `Huusom_et_al_2025` discusses an SQL database (PostgreSQL) but does not mention or evaluate "TimescaleDB".|
|**Round-Trip Time (RTT)**|Verified|Supported|Measurement methodology variation across papers (application-level RTT vs. gateway request-to-publication vs. socket lifecycle).|

---

### Detailed Verification & Traceability Evidence

#### 1. Core Architectural Patterns

##### Unified Namespace (UNS)

- **Attribution Status**: Verified (`Šenk et al., 2026`; `Freitas et al., 2025`; `Pillai et al., 2026`; `Koprov et al., 2022`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "The Unified Namespace (UNS) is an architectural pattern for organizing industrial data in a unified, hierarchically structured, and event-driven information space, with the goal of providing a Single Source of Truth (SSOT) for all data in the system." (Šenk et al., 2026, p. 4) "A Unified Namespace (UNS) is a data-centric architecture for organizing operational and business data, providing access to all data that clearly and systematically describe the system." (Freitas et al., 2025, p. 5) "UNS provides a unified, structured data model where information from sensors, cameras, actuators, controllers, and enterprise systems is aggregated into a single real-time stream..." (Pillai et al., 2026, p. 2)
    
- **Semantic Discrepancies**:
    
    > "In the context of a Unified Namespace (UNS), MQTT structures data through flexible topic strings... lacks native mechanisms for enforcing a standardized structure or data schema. Consequently, maintaining consistency within the UNS relies heavily on careful governance... By contrast, OPC UA provides a formal, standardized address space in which data is represented as nodes within a well-defined namespace." (Freitas et al., 2025, p. 5)
    

##### Digital Twin (DT)

- **Attribution Status**: Verified (`Bădoi et al., 2026`; `Koprov et al., 2025`; `Pillai et al., 2026`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "DT (i.e., comprehensive virtual replicas of physical assets, processes, or entire systems that continuously mirror their real-world counterparts by integrating live sensor data, engineering models, and historical records)... in line with emerging DT framework guidance for manufacturing such as ISO 23247-1:2021" (Bădoi et al., 2026, p. 5) "DTs are real-time digital replicas of physical systems. They bridge the physical and digital realms, enabling real-time monitoring, predictive maintenance, and process optimization..." (Koprov et al., 2025, p. 1255)
    
- **Semantic Discrepancies**:
    
    > "...the present implementation deliberately stops at the DvT level and does not yet realize full DT of the modular cells... functionalities typically associated with full DTs (in the sense of ISO 23247-1:2021), such as physics-based co-simulation of the entire cell... remain outside the scope of the current deployment and are delegated to the CoppeliaSim-based environment as an offline analysis tool." (Bădoi et al., 2026, p. 13)
    

##### Device Twin (DvT)

- **Attribution Status**: Verified (`Bădoi et al., 2026`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "In Azure IoT Hub, a DvT is a JavaScript Object Notation (JSON) document storing device state information, including metadata, configurations, and operational conditions... A DvT model comprises three principal components: Desired properties... Reported properties... Tags..." (Bădoi et al., 2026, p. 12–13)
    

##### Digital Shadow

- **Attribution Status**: Verified (`Koprov et al., 2025`; `Pillai et al., 2026`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "The first case, a one-way DT, is designed for real-time monitoring of the Haas VF-2 CNC machine. This DT, often referred to as a digital shadow, continuously streams operational data... enabling real-time observation without direct control..." (Koprov et al., 2025, p. 1255) "Within the UNS framework, photogrammetry and three-dimensional scanning technologies enable the creation of accurate digital replicas, commonly referred to as digital twins or Digital Shadows..." (Pillai et al., 2026, p. 2)
    
- **Semantic Discrepancies**: Koprov et al. (2025) define Digital Shadow strictly as a **unidirectional monitoring state stream** (no control write-back), while Pillai et al. (2026) treat it as a synonym for photogrammetric 3D visual models.

##### Cyber-Physical Systems (CPS)

- **Attribution Status**: Verified (`Freitas et al., 2025`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "The National Science Foundation defines CPS as engineered systems that are built from, and depend upon, the seamless integration of computation and physical components. In a CPS, it is combined the computing, storage and communication properties of the cyberspace to monitor and control the physical features" (Freitas et al., 2025, p. 2)
    

##### Industrial Metaverse (IM)

- **Attribution Status**: Verified (`Koprov et al., 2025`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "The IM is an advanced stage and long-term vision of digital transformation, characterized by ultra-realistic, accessible, pervasive, and potentially decentralized virtual environments." (Koprov et al., 2025, p. 1255)
    

##### Machine Profiles

- **Attribution Status**: Verified (`Koprov et al., 2022`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "Machine profiles provide a semantic taxonomy of tags that help define the characteristic features of physical machine assets. These profiles enable a unified format of type definitions that multiple users can reuse." (Koprov et al., 2022, p. 70)
    

##### Address Space Model

- **Attribution Status**: Verified (`Freitas et al., 2025`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "The Address Space Model defines the building blocks for creating Information Models, which are essential for constructing the Address Space of an OPC-UA server." (Freitas et al., 2025, p. 4)
    

##### Predictive and Preventive Maintenance (PPM)

- **Attribution Status**: Verified (`Pillai et al., 2026`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "This study aims to enhance Predictive and Preventive Maintenance (PPM) through the implementation of a Unified Namespace (UNS) framework in industrial systems." (Pillai et al., 2026, p. 3) "The system achieved a 42.25% reduction in machine downtime and a 36% reduction in Mean Time to Repair (MTTR)..." (Pillai et al., 2026, p. 14)
    
- **Empirical Discrepancies**:
    
    > "Estimated downtime reduction: Relative reduction in unplanned downtime compared to baseline (simulation-based assessment) 25–40%... MTTI: Reduction in MTTI versus schedule-based maintenance strategies 30–50%" (Bădoi et al., 2026, p. 24)
    

##### Interoperability

- **Attribution Status**: Verified (`Freitas et al., 2025`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "Interoperability can be described by ISO16100, as 'the ability to share and exchange information using a common syntax and semantics to meet an application-specific functional relationship across a common interface'." (Freitas et al., 2025, p. 3)
    

---

#### 2. Protocols & Telemetry Models

##### Message Queuing Telemetry Transport (MQTT)

- **Attribution Status**: Verified (`Jaloudi, 2019`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "...message queuing telemetry transport (MQTT) is chosen as the event-based, publish–subscribe protocol." (Jaloudi, 2019, p. 1) "The Message Queuing Telemetry Transport (MQTT) protocol is a simple, lightweight messaging protocol developed by IBM in 1999." (Freitas et al., 2025, p. 5)
    

##### Sparkplug B

- **Attribution Status**: Verified (`Šenk et al., 2026`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "The Sparkplug B specification extends MQTT with a standardized topic namespace, defined birth and death messages, structured payload data based on the Protocol Buffers (Protobuf) format, and state management mechanisms for edge nodes and devices." (Šenk et al., 2026, p. 4)
    

##### MODBUS TCP

- **Attribution Status**: Verified (`Jaloudi, 2019`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "...MODBUS TCP is an open de facto standard... It is based on a polling mechanism and follows the synchronous request–response pattern..." (Jaloudi, 2019, p. 1)
    

##### Constrained Application Protocol (CoAP)

- **Attribution Status**: Verified (`Jaloudi, 2019`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "CoAP is an application layer protocol, dedicated to communication with constrained devices in IPv6-based IoT infrastructures... runs over the connectionless UDP in the transport layer..." (Jaloudi, 2019, p. 7)
    

##### CloudConnects (CC)

- **Attribution Status**: Verified (`Huusom et al., 2025`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "...GitLab wiki pages were used to document various aspects of the digital infrastructure, including CloudConnect configuration, vNode setup, and Kubernetes-specific configurations..." (Huusom et al., 2025, p. 4)
    

##### vNode

- **Attribution Status**: Verified (`Huusom et al., 2025`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "vNode serves as this central real-time data hub... a commercial software platform originally designed as an Industrial Internet of Things (IIoT) gateway, capable of bridging various industrial protocols and cloud environments... gather, structure, and redistribute live data from all unit operations and SCADA..." (Huusom et al., 2025, p. 3)
    

##### Edge of Nodes (EoN)

- **Attribution Status**: Verified (`Koprov et al., 2022`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "This necessitates the need for EoN (edge of nodes) – devices that convert proprietary protocol data and analog signals to MQTT Sparkplug data type." (Koprov et al., 2022, p. 69)
    

##### TimescaleDB

- **Attribution Status**: **Incorrect** (`Huusom et al., 2025`).
- **Grounding Status**: **Hallucinated**.
- **Traceability Quote**:
    
    > "Not addressed in the active source(s)."
    
- **Audit Detail**: Huusom et al. (2025, p. 3–4) discuss containerized Python applications writing real-time data to a structured **SQL database (PostgreSQL)**, but do _not_ explicitly state, define, or evaluate "TimescaleDB" anywhere in the active source text.

##### Round-Trip Time (RTT)

- **Attribution Status**: Verified (`Freitas et al., 2025`).
- **Grounding Status**: Supported.
- **Traceability Quotes**:
    
    > "Round Trip-Time (RTT): Average time to send and receive a complete message [unit: seconds]" (Freitas et al., 2025, Table 3, p. 11)