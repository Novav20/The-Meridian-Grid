---
paper_id: "Senk_et_al_2026"
query_id: "Q01"
title: "ESP32-Based Sparkplug B Gateway Framework for Brownfield PLC Integration into an IIoT Unified Namespace: A Data Foundation for Intelligent Industrial Systems"
authors: "Šenk I.; Tegeltija S.; Tarjan L."
year: 2026
doi: "10.3390/electronics15153441"
keywords: ["brownfield integration", "edge gateway", "ESP32", "IIoT", "intelligent industrial systems", "legacy PLC", "mechatronics", "MQTT", "Sparkplug B", "Unified Namespace"]
source_pdf: "ESP32-Based Sparkplug B Gateway Framework for Brownfield PLC Integration into an IIoT Unified Namespace: A Data Foundation for Intelligent Industrial Systems.pdf"
extraction_date: "2026-09-04"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Unified Namespace (UNS)
- **Definition**: An architectural pattern for organizing industrial data in a unified, hierarchically structured, and event-driven information space, with the goal of providing a Single Source of Truth (SSOT) for all data in the system.
> **Evidence**: "The Unified Namespace (UNS) is an architectural pattern for organizing industrial data in a unified, hierarchically structured, and event-driven information space, with the goal of providing a Single Source of Truth (SSOT) for all data in the system." (p. 4)

- **Term**: Sparkplug B
- **Definition**: A specification extending MQTT that introduces a standardized topic namespace, defined birth and death messages, structured payload data using the Protocol Buffers (Protobuf) format, and state management mechanisms for edge nodes and devices.
> **Evidence**: "The Sparkplug B specification extends MQTT with a standardized topic namespace, defined birth and death messages, structured payload data based on the Protocol Buffers (Protobuf) format, and state management mechanisms for edge nodes and devices." (p. 4)

### 2. Domain Rules and Invariants

- **Rule**: Functional Fault Isolation Invariant
- **Mechanism**: Placing a dedicated gateway as a protocol-termination and network-segmentation point ensures that any physical link failure or controller fault remains isolated to that specific node and does not propagate to or degrade the operation of other gateways on the network.
> **Evidence**: "Within the proposed architecture, each gateway supports functional fault isolation at the gateway-node level and acts as a protocol-termination and segmentation point between the PLC-facing industrial protocol and the MQTT-facing network. Consequently, a failure of one gateway or its PLC communication link does not directly affect the operation of the remaining gateway nodes." (p. 7)

- **Rule**: Dual-Level Node and Device Lifecycle State Signaling
- **Mechanism**: If connection to a PLC is lost while its gateway remains connected, the gateway publishes a DDEATH message; if the gateway itself disconnects ungracefully, the MQTT broker publishes an NDEATH message via the Last Will mechanism to maintain exact status awareness.
> **Evidence**: "Loss of communication with a PLC while the corresponding ESP32 Edge Node remains connected to the MQTT broker triggers a DDEATH message, indicating that the PLC device is unavailable. In contrast, loss of the gateway or its MQTT connection is reported by an NDEATH message published through the MQTT Last Will mechanism." (p. 7)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: ISA-95-Aligned Hierarchical Tag Schema
- **Implication**: All process and diagnostic data are structured as a Site/Area/Edge Node/Device/Tag hierarchy, giving higher-level applications a consistent, unified equipment topology that abstracts away native PLC communication details.
> **Evidence**: "The tag hierarchy implemented in Ignition follows an ISA-95-oriented structure organized as Site/Area/Edge Node/Device/Tag." (p. 8)

- **Constraint/Pattern**: Protocol-Termination and Network-Segmentation Gateway Topology
- **Implication**: Non-secure legacy industrial protocols are fully isolated on their local physical Ethernet segments, terminating at the gateway which bridges the data to a TLS 1.2-encrypted Wi-Fi path, preventing exposure of the PLCs to the broader IT network.
> **Evidence**: "In the proposed architecture, each gateway acts as a protocol-termination and network-segmentation point, preventing direct exposure of the PLC-facing protocols to the MQTT-facing network. TLS 1.2 and broker authentication protect the gateway-to-broker communication path." (p. 22)

- **Constraint/Pattern**: Distributed One-Gateway-per-PLC Node Pattern
- **Implication**: System scaling is achieved by horizontally adding independent microcontrollers for each additional PLC type, allowing gradual brownfield integration without modifying any existing gateway configurations.
> **Evidence**: "The one-gateway-per-PLC architecture supports horizontal expansion by adding an independent ESP32 gateway node and the corresponding protocol adapter for each additional PLC type, without modifying the already deployed gateways." (p. 21)

### 4. Context Assumptions

- **Assumption**: Low-Latency Non-Deterministic Supervisory Context
- **Evidence**: "the framework is primarily intended for monitoring and supervisory control applications in controlled industrial environments rather than for safety-critical or hard real-time control systems." (p. 7)

- **Assumption**: Shared Infrastructure Single Points of Failure
- **Evidence**: "However, shared infrastructure components, including the Wi-Fi access point, MQTT broker, common power supply, and Ignition server, remain potential common points of failure." (p. 7)

