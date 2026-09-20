---
paper_id: "Guo_et_al_2022"
query_id: "Q02"
title: "Web-based IoT and Robot SCADA using MQTT protocol"
authors: "Guo J.-H.; Lin T.-Y.; Hsia K.-H."
year: 2022
doi: "10.57417/jrnal.9.2_202"
keywords: ["AES", "Internet of things (IoT)", "MQ telemetry transport (MQTT)", "Robot", "Supervisory control and data acquisition (SCADA)"]
source_pdf: "Web-based IoT and Robot SCADA using MQTT protocol.pdf"
extraction_date: "2026-09-20"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: MQTT Protocol
- **Definition**: A lightweight Publish/Subscribe messaging protocol designed for IoT environments with low power consumption and limited network bandwidth that routes messages through a central broker.
> **Evidence**: "MQTT is a lightweight protocol and a protocol designed for the Internet of Things. Therefore, the network bandwidth it requires is very low, and the hardware resources required are also low. It is very suitable for IoT environments with low power consumption and limited network bandwidth, such as smart home appliances or medical devices." (p. 204)

- **Term**: Four-Level MQTT Topic Structure
- **Definition**: A hierarchical topic taxonomy comprising MQTT serial number (device ID), Device name, Input/output direction, and Data type layers to organize multi-controller messages.
> **Evidence**: "Since this system will be connected to many controllers, sensors, and actuators, in the design principle of Topic, consider the use of a four-level design, the format is shown in Table 1." (p. 204)

- **Term**: WYSIWYG Web-based SCADA
- **Definition**: A web-based supervisory system where users construct application screens using drag-and-drop instrument icons and parameter configuration areas.
> **Evidence**: "This Web-based SCADA uses drag-and-drop operation, and users can quickly build a WYSIWYG (What You See Is What You Get) application system." (p. 202)

- **Term**: Grid Display Method
- **Definition**: A 2D grid visualization mode adopted for monitoring mobile robots and AGVs on web interfaces to minimize browser computing resource consumption compared to 3D virtual reality.
> **Evidence**: "In the mobile robot SCADA part of this research, we use the grid display method. The main reason is to consider that the entire SCADA will not use too many resources when operating on the web page." (p. 207)

### 2. Domain Rules and Invariants

- **Rule**: Four-Level Topic Layer Hierarchy Rule
- **Mechanism**: MQTT topic strings must strictly follow the four-layer structure `[MQTT ID]/[Device Name]/[Input or Output]/[Data Type]` (e.g., `01/stm32/data/sensor`) to route signals across mixed field controllers.
> **Evidence**: "The description of this structure is as follows. * MQTT serial number layer: The first layer is named after the device ID, called MQTT ID, starting from 01. * Device name layer: Since there are many IoTs devices, robot or data sources of other devices in the system, this layer can be used to distinguish different devices or data sources... * Input and output layer: This layer can be used to represent data output or input, and are named after control and data respectively. * Data type: The last layer refers to the format of the subscription data, including sensors, connection status, video streaming, etc., which are respectively sensor, connection, and stream." (p. 204-205)

- **Rule**: AES Data Payload Encryption Invariant
- **Mechanism**: To bypass complex SSL overhead on resource-constrained IoT hardware, all device-to-broker communications and data payloads are encrypted using Advanced Encryption Standard (AES) technology.
> **Evidence**: "At present, most brokers have SSL (Secure Sockets Layer) encryption mechanism when transmitting data. But SSL is too complicated for IoT devices. Therefore, this paper uses AES (Advanced Encryption Standard) technology to ensure the security of all communication and data in the communication of the IoT module and the communication of the relay station (Broker)." (p. 204)

- **Rule**: Dual Processing Modes for Raw vs. Parsed Messages
- **Mechanism**: If a device's data structure is clearly known, the system parses it into structured MQTT topics; if unknown, the raw unparsed device payload is stored directly in the database for post-hoc parsing.
> **Evidence**: "If the device data can be clearly distinguished and distinguished, these data will be processed into MQTT messages and used on the SCADA system we designed. If the content of the device's data cannot be clearly known, the SCADA system will still store it in the database and try to parse the content." (p. 207)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: WebSocket-Based Full-Duplex Web Pushing Pattern
- **Implication**: Real-time browser-to-server data exchange uses a single-handshake persistent WebSocket connection operating over standard TCP HTTP/HTTPS ports (80/443), allowing servers to push live updates to clients without HTTP polling overhead or firewall blockage.
> **Evidence**: "In this architecture, we use the WebSocket network transmission protocol, which is often used in Internet applications... In the WebSocket API, the browser and the server only need to complete a one-time handshake operation, and a sustainable connection can be established between the two, and two-way data transmission can be carried out... Communication can be done through TCP port 80 or 443. This is beneficial in an environment where a firewall prevents non-Web network connections, with better flexibility, higher security, and efficiency." (p. 204)

- **Constraint/Pattern**: IoT-Gateway Conversion Topology for Legacy Field Robots
- **Implication**: Industrial robots and AGVs lacking native network capabilities or AES hardware acceleration interface through an intermediate IoT module (e.g., STM32 board) that performs protocol translation and AES encryption before publishing to the MQTT broker.
> **Evidence**: "In the robot and AGV part, since there is not necessarily a network interface, the communication interface and use AES encryption function can be converted through the IoT module of this study. If the robot and AGV originally have a network communication interface and an AES encryption mechanism, they can be directly connected to the system of this study." (p. 204)

### 4. Context Assumptions

- **Assumption**: Heavy Computing Resource Consumption of 3D Virtual Reality in Web HMIs
> **Evidence**: "If the 3D virtual reality is used as the interface of the web page, it will consume more resources. And if many AGVs are monitored at the same time, there will be a problem of how to display the status of different AGVs." (p. 207)

- **Assumption**: Obstacle of Proprietary Robot Protocols in Industry 4.0 Integration
> **Evidence**: "The main reason is that each robot system is very different, so at present almost all the monitoring systems are provided by the original manufacturer. However, this will also cause great problems in the follow-up Industry 4.0 system integration." (p. 203)



