---
paper_id: "Koprov_et_al_2025"
query_id: "Q01"
title: "Industrial metaverse meets IIoT: low-code platforms for machine-to-machine and human-to-machine integration"
authors: "Koprov P.; Starly B."
year: 2025
doi: "10.1016/j.mfglet.2025.06.145"
keywords: ["Digital twin", "Industrial metaverse", "Low-code", "Machine communication", "MQTT Sparkplug B", "Node-RED", "Omniverse"]
source_pdf: "Industrial metaverse meets IIoT: low-code platforms for machine-to-machine and human-to-machine integration.pdf"
extraction_date: "2026-09-04"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Industrial Metaverse (IM)
- **Definition**: An advanced stage of digital transformation characterized by ultra-realistic, persistent, accessible, pervasive, and potentially decentralized virtual environments that blend real-world operations with virtual environments using technologies such as augmented reality and digital twins.
> **Evidence**: "The Industrial Metaverse (IM), which blends real-world operations with virtual environments through technologies such as digital twins (DTs), offers a promising solution" (p. 1254)

- **Term**: Digital Twins (DT)
- **Definition**: Real-time virtual replicas of physical systems that bridge the physical and digital realms to enable continuous remote monitoring, predictive maintenance, simulation, and process optimization.
> **Evidence**: "DTs serve as real-time digital replicas of physical systems, offering predictive maintenance, simulation capabilities, and remote monitoring—key components of the IM." (p. 1256)

- **Term**: Digital Shadow
- **Definition**: A unidirectional digital twin implementation designed for real-time monitoring of physical assets by continuously streaming operational variables without enabling direct upstream control or manipulation of the physical equipment.
> **Evidence**: "This DT, often referred to as a digital shadow, continuously streams operational data such as spindle speed and tool coordinates, enabling real-time observation without direct control over the machine." (p. 1255)

- **Term**: Universal Scene Description (USD)
- **Definition**: An extensible 3D scene description framework developed by Pixar that serves as the foundation for NVIDIA Omniverse by encapsulating asset geometry, visual properties, physics-driven behaviors, and relationships.
> **Evidence**: "Central to this integration is the Universal Scene Description (USD) framework, pioneered by Pixar, which enables the exchange of 3D data across diverse digital tools. USD forms the foundation for Omniverse, encapsulating an asset’s geometry, visual properties, behaviors, and relationships." (p. 1259)

### 2. Domain Rules and Invariants

- **Rule**: Haas VF-2 Unidirectional Monitoring Constraint
- **Mechanism**: The lack of native upstream control mechanisms over MQTT forces the Haas VF-2 CNC machine to operate exclusively as a one-way monitoring digital twin (digital shadow).
> **Evidence**: "The reason for this one-way approach is that there is no native control of the CNC machine from the MQTT application. While it is possible to develop an application that can change macro variables and select programs to run, our case study focuses solely on monitoring the CNC machine's state to represent it in the DT." (p. 1255)

- **Rule**: Inter-Asset Coordinated Trajectory Generation
- **Mechanism**: Commands for the robot's inverse kinematics are automatically computed using real-time coordinates published by the CNC machine, allowing coordinate synchronization without explicit waypoint programming.
> **Evidence**: "The state of the CNC machine, monitored by the one-way DT, is used by the bidirectional DT of the UR10e to generate commands for inverse kinematics." (p. 1255)

- **Rule**: Protocol-Payload Bandwidth Minimization Invariant
- **Mechanism**: Data streaming over the MQTT Sparkplug B interface must utilize Protocol Buffers (Protobuf) encoding to compress serialized data and decrease industrial network load.
> **Evidence**: "Data flows through MQTT SpB, ensuring structured exchange. Protobuf encoding minimizes network load, while SpB’s stateful messaging ensures operators are notified of unexpected disconnections." (p. 1258)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: ISO 23247 Four-Domain Reference Architecture
- **Implication**: The system partitions its architecture into the Observable Manufacturing Domain (physical machines), Device Communication Domain (MQTT SpB, ROS2, and RTDE-DDS protocols), Digital Twin Domain (Omniverse and Isaac Sim virtualizations), and User Domain (dashboards and custom apps) to achieve clean separation of concerns and system-wide interoperability.
> **Evidence**: "The system integrates four key domains: Observable Manufacturing Domain encompasses physical assets monitored and controlled in real-time... Device Communication Domain bridges the physical and digital environments, ensuring efficient data exchange... Digital Twin Domain... User Domain. Operators interact with the system through intuitive interfaces" (p. 1257)

- **Constraint/Pattern**: Hybrid Event-Based and Time-Based Synchronization Topology
- **Implication**: To balance latency and network overhead, the architecture uses asynchronous, event-driven updates for discrete CNC state triggers alongside time-based polling intervals via ROS2 for continuous robotic joint state tracking.
> **Evidence**: "Two synchronization mechanisms are implemented: Event-based synchronization for the Haas VF-2, where operational changes trigger updates. Time-based synchronization for the UR10e, polling status at intervals via ROS2." (p. 1259)

- **Constraint/Pattern**: Graph-Based Bidirectional ROS2 Bridge Pattern
- **Implication**: Connecting physical robots with their digital twins is done via graphical Action Graphs inside Isaac Sim that map ROS2 service request/client architectures directly to simulated articulations without custom backend code.
> **Evidence**: "Isaac Sim simplifies bi-directional communication through its built-in ROS and ROS2 bridges, enabling no-code DT integration. Figure 4 presents a sample Action Graph in Isaac Sim, demonstrating how developers can set up a bi-directional DT using a graph-based structure in minutes - eliminating the need for coding." (p. 1260)

### 4. Context Assumptions

- **Assumption**: Resource-constrained and low-expertise industrial contexts
> **Evidence**: "Small and medium-sized enterprises face challenges in adopting advanced manufacturing technologies due to limited resources and technical expertise." (p. 1254)

- **Assumption**: Low-latency and highly reliable local area industrial networks
> **Evidence**: "Network reliability is essential for real-time data exchange via MQTT and ROS2. Latency issues could affect synchronization in distributed manufacturing environments." (p. 1263)

