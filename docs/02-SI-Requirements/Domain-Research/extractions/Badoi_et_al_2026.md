---
paper_id: "Badoi_et_al_2026"
query_id: "Q01"
title: "A Hierarchical Framework Leveraging IIoT Networks, IoT Hub, and Device Twins for Intelligent Industrial Automation"
authors: "Bădoi C.I.; Kartal Çetin B.; Çetin K.; Karataş Ç.; Özbek M.E.; Şahin S."
year: 2026
doi: "10.3390/app16020645"
keywords: ["5G/6G", "Azure", "device twins", "digital twins", "edge computing", "edge-cloud integration", "IIoT", "industrial automation", "IoT Hub", "modular automation", "MQTT", "predictive maintenance", "scalable manufacturing", "ZigBee"]
source_pdf: "A Hierarchical Framework Leveraging IIoT Networks, IoT Hub, and Device Twins for Intelligent Industrial Automation.pdf"
extraction_date: "2026-09-04"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Device Twins (DvT)
- **Definition**: Digital models of individual hardware devices that facilitate remote monitoring, configuration, and life-cycle management, bringing granular visibility and state synchronization.
> **Evidence**: "DvT (i.e., digital models of individual hardware devices) facilitate remote monitoring, configuration, and life-cycle management, bringing granular visibility and synchronization of device states." (p. 5)

- **Term**: Digital Twins (DT)
- **Definition**: Comprehensive virtual replicas of physical assets, processes, or entire systems that continuously mirror their real-world counterparts by integrating live sensor data, engineering models, and historical records.
> **Evidence**: "DT (i.e., comprehensive virtual replicas of physical assets, processes, or entire systems that continuously mirror their real-world counterparts by integrating live sensor data, engineering models, and historical records), in contrast, extend these capabilities to system-wide or even enterprise-wide virtualisation, integrating multi-source data and physics-based models to enable predictive maintenance, process simulation, and real-time optimization" (p. 5)

### 2. Domain Rules and Invariants

- **Rule**: DvT state synchronization requires the mandatory selection of the Azure IoT Hub Standard tier.
- **Mechanism**: The Standard tier must be chosen because device twin state synchronization is a core architectural requirement and is completely unavailable in the Basic tier.
> **Evidence**: "Notably, the Standard tier is a mandatory selection in our case, since DvT synchronization is a core requirement for our IIoT framework and is unavailable in the Basic tier." (p. 14)

- **Rule**: Path-selection failover must route telemetry to the backup ZigBee mesh if primary MQTT connectivity is lost.
- **Mechanism**: If the MQTT broker becomes unavailable for more than 5 seconds, the Central Edge Gateway prioritizes the ZigBee backup feed to sustain analytics processing.
> **Evidence**: "upon detection of the unavailability of the MQTT broker (timeout greater than 5 s), the Central Edge Gateway seamlessly prioritizes the ZigBee feed to preserve predictive maintenance analytics (Figure 5)." (p. 10)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Redundant Dual-Mesh Network Topology.
- **Implication**: Telemetry and control traffic are split across a primary MQTT-over-Ethernet/WiFi mesh and an independent ZigBee-based backup mesh operating on a separate radio frequency layer to withstand local Ethernet switch, power, or WiFi interference faults.
> **Evidence**: "To ensure operational continuity during primary MQTT infrastructure failures, the architecture incorporates a redundant ZigBee mesh network (IEEE 802.15.4-2020) operating on an independent radio frequency layer. This dual-mesh strategy provides resilience against Ethernet switch failures, IEPC power loss, and WiFi interference, ensuring that critical telemetry remains accessible even during catastrophic network disruptions." (p. 10)

- **Constraint/Pattern**: Two-Tier Federated MQTT Broker Mesh.
- **Implication**: Local Mosquitto MQTT brokers hosted on individual IEPCs serve field assets within their cells and connect via TLS 1.3-secured bridges to a central MQTT broker on the Edge Controller, isolating local publish/subscribe operations from upstream network disconnections.
> **Evidence**: "the IIoT network on-premises implements a federated MQTT broker architecture based on Mosquitto broker bridging. Each of the nine IEPCs hosts a local MQTT broker instance serving sensors and actuators within its respective MA setup. These local brokers are interconnected through TLS-secured bridge configurations to a central MQTT broker hosted on the Edge Controller, forming a resilient mesh topology at the application layer." (p. 9)

### 4. Context Assumptions

- **Assumption**: Low-rate bandwidth restriction on the backup physical/MAC layer.
> **Evidence**: "as the 250 kbps bandwidth constraint of IEEE 802.15.4-2020 restricts backup operation to low-rate variables, leaving high-frequency vibration streams confined to the primary MQTT path." (p. 10)

- **Assumption**: Bounded buffering capacity and message retention limits during cloud connectivity outages.
> **Evidence**: "During cloud connectivity outages, the Central Edge Controller/Gateway relies on Azure IoT Hub’s cloud-to-device message retention, which can be configured with a time-to-live (TTL) of up to 48 h per device queue, together with the Azure IoT Edge store-and-forward mechanism for device-to-cloud messages." (p. 11)


