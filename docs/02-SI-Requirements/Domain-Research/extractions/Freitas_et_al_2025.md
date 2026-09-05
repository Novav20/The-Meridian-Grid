---
paper_id: "Freitas_et_al_2025"
query_id: "Q01"
title: "OPC UA and MQTT performance analysis within a unified namespace context"
authors: "Freitas L.; Silva M.; Vale G.; Avram C.; Lopes H.; Pereira F.; Leal N.; Machado J."
year: 2025
doi: "10.1016/j.iot.2025.101734"
keywords: ["Communication protocols", "Control architectures", "Cyber-physical production systems", "Industrial internet of things", "Interoperability", "MQTT", "OPC-UA", "UNS"]
source_pdf: "OPC UA and MQTT performance analysis within a unified namespace context.pdf"
extraction_date: "2026-09-04"
---

### 1. Ubiquitous Language

- **Term**: Unified Namespace (UNS)
- **Definition**: A data-centric architecture for organizing operational and business data, providing access to all data that clearly and systematically describe the system, using an agreed-upon naming convention and semantic hierarchy.
> **Evidence**: "A Unified Namespace (UNS) is a data-centric architecture for organizing operational and business data, providing access to all data that clearly and systematically describe the system. This structure makes data available to any device, software, or person who needs it to perform their tasks, using an agreed-upon naming convention and semantic hierarchy." (p. 5)

- **Term**: Cyber-Physical Systems (CPS)
- **Definition**: Engineered systems built from and dependent upon the seamless integration of computation and physical components, combining computing, storage, and communication properties of cyberspace to monitor and control physical features.
> **Evidence**: "The National Science Foundation defines CPS as engineered systems that are built from, and depend upon, the seamless integration of computation and physical components. In a CPS, it is combined the computing, storage and communication properties of the cyberspace to monitor and control the physical features." (p. 2)

- **Term**: Interoperability
- **Definition**: The ability to share and exchange information using a common syntax and semantics to meet an application-specific functional relationship across a common interface.
> **Evidence**: "Interoperability can be described by ISO16100, as “the ability to share and exchange information using a common syntax and semantics to meet an application-specific functional relationship across a common interface”." (p. 4)

- **Term**: Address Space Model
- **Definition**: The structural definition of the building blocks used to create Information Models, which are essential for constructing the Address Space of an OPC UA server.
> **Evidence**: "The Address Space Model defines the building blocks for creating Information Models, which are essential for constructing the Address Space of an OPC-UA server." (p. 4)

- **Term**: Round-Trip Time (RTT)
- **Definition**: The total time required to complete the entire sequence of sending and acknowledging a message between the client and the broker/server.
> **Evidence**: "This represents the total time required to complete the entire sequence of sending and acknowledging a message between the client and the broker." (p. 12)

### 2. Domain Rules and Invariants

- **Rule**: Outbound-Only Publisher Architecture Constraint
- **Mechanism**: Pure publishers (such as the Ewon Flexy 205 in this setup) only require outbound communication to send data to the broker, eliminating the need for inbound network firewall rules.
> **Evidence**: "Additionally, pure publishers—such as Flexy in this case study—only require outbound communication to send data to the broker without needing inbound rules. With OPC UA, however, a two-way channel must be established for communication between clients and servers." (p. 18)

- **Rule**: Non-Linear Performance Impact under QoS 0 Scaling
- **Mechanism**: Scaling the client count from two to three results in an approximate 95% increase in RTT for QoS 0 due to the lack of message delivery confirmation overhead, compared to smaller 35% and 45% increases for QoS 1 and QoS 2.
> **Evidence**: "Additionally, the impact of adding a client is more pronounced with QoS 0, resulting in approximately a 95% increase in RTT, compared to increases of around 35% and 45% for QoS 1 and QoS 2, respectively." (p. 13)

- **Rule**: Security Policy Influence on Packet Size vs. Count
- **Mechanism**: Applying security (TLS/SSL encryption in MQTT, or Basic256Sha256 in OPC UA) increases the byte size of transmitted packets but has zero impact on the total number of packets exchanged.
> **Evidence**: "Adding a security policy has no impact in the number of packets exchanged." (p. 15)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Unified Namespace (UNS) Hierarchical Organisation Pattern
- **Implication**: To structure industrial data semantically, a hierarchical organization based on the ISA-95 standard is deployed at the central broker, allowing any client or software to easily browse and locate data with full operational context.
> **Evidence**: "The UNS, deployed in the MQTT Broker, is based on ISA-95, where the information (topics) is semantically organized in a hierarchical manner, allowing any user/software to browse and find the data with as much context as possible." (p. 8)

- **Constraint/Pattern**: Hybrid Edge/Control Protocol Architecture
- **Implication**: Engineers deploy MQTT at the edge device level to handle lightweight data acquisition, low power, and low bandwidth, while using OPC UA at the control layer (PLCs, MES) for high-integrity, structured, and secure communication.
> **Evidence**: "These complementary strengths suggest that a hybrid architecture—using MQTT for distributed edge data collection and OPC UA for secure, structured control-level communication—can effectively address the requirements of modern industrial digitalization projects." (p. 20)

- **Constraint/Pattern**: Report by Exception (RBE) in OPC UA Subscription Model
- **Implication**: By configuring clients to monitor specific nodes on the server, updates are pushed only when value changes or predefined time thresholds are met, which reduces overall network traffic compared to traditional client/server polling.
> **Evidence**: "The OPC UA subscription model used in this case study supports the report by exception (RBE) feature, which is characteristic of pub/sub architectures. Thus, it reduces network traffic compared to traditional polling methods in client/server architectures." (p. 18)

### 4. Context Assumptions

- **Assumption**: High-efficiency QoS 0 operation assumes stable, error-free physical network conditions.
> **Evidence**: "The tests showed that in stable connections, as the one presented in this study where there is no packet loss, QoS0 is enough and comparing with OPC UA, the performance metrics were significantly lower..." (p. 18)

- **Assumption**: Heterogeneous brownfield environments where legacy PLCs lack native modern protocol support.
> **Evidence**: "A gateway was used, as is common practice in industrial applications when the PLC does not run natively the desired communication protocol, to recover the data from the FAS-200 into the chosen configuration." (p. 8)
