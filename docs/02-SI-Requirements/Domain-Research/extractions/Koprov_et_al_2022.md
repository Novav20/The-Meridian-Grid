---
paper_id: "Koprov_et_al_2022"
query_id: "Q01"
title: "Streaming Machine Generated Data via the MQTT Sparkplug B Protocol for Smart Factory Operations"
authors: "Koprov P.; Ramachandran A.; Lee Y.-S.; Cohen P.; Starly B."
year: 2022
doi: "10.1016/j.mfglet.2022.07.016"
keywords: ["Digital Factory", "Digital Twin", "IIoT", "Industrial Internet of Things", "IT/OT integration", "Legacy Machines"]
source_pdf: "Streaming Machine Generated Data via the MQTT Sparkplug B Protocol for Smart Factory Operations.pdf"
extraction_date: "2026-09-04"
---

### 1. Ubiquitous Language

- **Term**: Profiles
- **Definition**: Reusable, object-oriented semantic models that contextually describe sensors, equipment, and processes while defining how variables relate to one another to eliminate custom middleware configuration.
> **Evidence**: "The key technology in the platform is the concept of Profiles, that CESMII is creating to contextually describe sensors, equipment, and processes and generate semantics for data, showing how variables relate to each other." (p. 67)

- **Term**: EoN (edge of nodes)
- **Definition**: Devices that convert proprietary industrial protocol data and analog signals into the standardized MQTT Sparkplug data format to enable legacy or non-communicative machinery.
> **Evidence**: "Some of the devices available at the production floor exploit proprietary protocols or even send analog signals. This necessitates the need for EoN (edge of nodes) – devices that convert proprietary protocol data and analog signals to MQTT Sparkplug data type." (p. 69)

### 2. Domain Rules and Invariants

- **Rule**: Report-by-Exception Transmission
- **Mechanism**: To prevent shop floor network congestion, the publisher node polls the machining asset parameters continuously but only transmits messages to the central broker if a value change is detected.
> **Evidence**: "The publisher runs in an infinite loop, polling the list of Q-codes as necessary. Data is published to the broker only if there are changes in any of the machine parameters that must be reported." (p. 70)

- **Rule**: Connection Degradation Fallback (STALE State)
- **Mechanism**: If the Edge of Node (EoN) device loses telnet connectivity with its target CNC controller, it must immediately publish a DDEATH certificate and label the last known parameters with a "STALE" flag to preserve data integrity.
> **Evidence**: "if telnet connection fails or there are any other reasons RPI loses connectivity with CNC machine, it publishes last known data with flag 'STALE' and device death certificate" (p. 70)

- **Rule**: Keep-Alive Disconnection Timeout (Last Will and Testament)
- **Mechanism**: If a publisher node fails to communicate or ping the broker within 1.5 times its set keep-alive duration, the broker forcibly disconnects the client and publishes the Last Will and Testament (LWT) packet to the NDEATH topic.
> **Evidence**: "MQTT uses a 1.5 times period to reconnect the client. If the client does not respond within this period broker disconnect client and publishes the LWT message." (p. 71)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Localized Gateway Isolation Topology
- **Implication**: Each machining asset is physically coupled to a dedicated Raspberry Pi 4B microcontroller via a point-to-point Ethernet link, restricting insecure machine telnet interfaces to a single host while bridging telemetry wirelessly to the secure local area network.
> **Evidence**: "Each machine asset was connected via Ethernet to a Raspberry PI 4B (RPI) that runs an MQTT Publisher node. Arrows between RPI and CNC machines represent 2-way communication between EoN and the asset. RPIs are connected to the local area network (LAN) through a wireless connection. LAN makes sure that no one can externally access the network, and Ethernet connection assures that only one device is connected to the CNC." (p. 69)

- **Constraint/Pattern**: Collapsed Purdue Model (Node-to-Node Communication)
- **Implication**: Structuring data paths horizontally via pub/sub mechanisms removes traditional hierarchical gateways (Levels 0-5), establishing a flat, event-driven unified namespace where field edge nodes publish directly to enterprise/cloud subscribers.
> **Evidence**: "This type of communication architecture collapses the Purdue Model by removing structured layers to enable a more node-to-node communication of assets." (p. 72)

- **Constraint/Pattern**: Broker-Centric Unified Namespace Pattern
- **Implication**: Publisher and subscriber nodes are strictly decoupled and do not communicate directly; all real-time state and telemetry data are organized under standard Sparkplug B topic hierarchies at the central broker, which serves as the single source of truth.
> **Evidence**: "The subscriber nodes themselves are not directly communicating with the publisher nodes. The communication happens only through the MQTT Broker topic channels." (p. 69)

### 4. Context Assumptions

- **Assumption**: Insecure, Open Native CNC Interfaces
- **Evidence**: "These machines were not connected to the broader university-wide infrastructure due to the insecure Telnet protocol." (p. 69)

- **Assumption**: Network Port Inbound Restrictions
- **Evidence**: "IIoT enabled by MQTT utilizes the pub/sub architecture that secures devices from accessing through network ports. Any authenticated device can subscribe and publish to a topic." (p. 67)
