---
paper_id: "Jaloudi_2019"
query_id: "Q01"
title: "Communication protocols of an industrial internet of things environment: A comparative study"
authors: "Jaloudi S."
year: 2019
doi: "10.3390/fi11030066"
keywords: ["Automation", "IIoT", "MODBUS", "MQTT", "Publish-subscribe", "Request-response", "SCADA"]
source_pdf: "Communication protocols of an industrial internet of things environment: A comparative study.pdf"
extraction_date: "2026-09-04"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: MODBUS TCP
- **Definition**: A byte-oriented, open de facto standard industrial communication protocol used for data exchange between embedded systems, devices, and industrial applications via a polling request–response mechanism.
> **Evidence**: "The MODBUS TCP is a byte-oriented, industrial communication protocol, open de facto standard, used for data exchange between embedded systems, devices, and industrial applications. Devices, reacting as clients, may benefit from the inexpensive implementation of such a lightweight protocol for polling industrial devices that react as servers. Polling communications follow the request–response mechanism" (p. 3)

- **Term**: Message Queuing Telemetry Transport (MQTT)
- **Definition**: An event-based, message-oriented, asynchronous publish–subscribe protocol designed for reliable one-to-many machine-to-machine (M2M) communications.
> **Evidence**: "whereas MQTT uses the publish–subscribe model and is message-oriented. Thus, MQTT is one-to-many" (p. 6)

- **Term**: Constrained Application Protocol (CoAP)
- **Definition**: An application-layer, document-oriented protocol dedicated to communications with constrained devices in IPv6-based Internet of Things (IoT) infrastructures, operating asynchronously over connectionless UDP.
> **Evidence**: "CoAP is an application layer protocol, dedicated to communication with constrained devices in IPv6-based IoT infrastructures. Two communication patterns are used by CoAP, i.e., publish–subscribe and request–response." (p. 7)

### 2. Domain Rules and Invariants

- **Rule**: Linear Overhead Invariant for MODBUS Read Operations
- **Mechanism**: The total byte size consumed by a "read input registers" (0x04) transaction (combining the client request and server response frames) scales linearly with the number of registers ($N$) being queried, defined exactly by the formula $2 \times N + 21$.
> **Evidence**: "Size = request_bytes + response_bytes = (7 + 5) + (9 + 2 × N) = 2 × N + 21" (p. 4)

- **Rule**: Linear Overhead Invariant for Concurrent MODBUS Read/Write Operations
- **Mechanism**: Executing both read and write operations concurrently within a single application-layer query using function code 0x17 requires a total frame size of $26 + 2 \times (N_{Read} + N_{Write})$ bytes, optimizing performance compared to separate queries.
> **Evidence**: "If the client application requires the execution of both operations—read and write—within the same message for a remote device, the function code “read/write multiple registers” (0x17) shows higher performance than both the “read input registers” (0x04) and the “write multiple registers” (0x10) function codes if used separately. Equation (2) illustrates two linear formulae for the function code “read/write multiple registers” (0x17), which sends both commands within the same message: ... Total_size = 26 + 2 × (NRead + NWrite)" (p. 5)

- **Rule**: UTF-8 Encoded Interoperability Overhead Doubling
- **Mechanism**: Translating binary MODBUS frames into UTF-8 representation to achieve interoperability in MQTT payloads replaces each individual byte of the MODBUS message with two UTF-8 hexadecimal characters, which exactly doubles the payload size of the MQTT publish message.
> **Evidence**: "Each byte of the MODBUS message is represented by two bytes, as shown in Figure 13. For example, the ID part of the MODBUS message is “00 01”, which leads to “30 30 30 31” representation, and doubles the payload of the MQTT publish message." (p. 13)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Parallel Dual-Protocol Coexistence
- **Implication**: Telecontrol, automation, and critical feedback loops run synchronously on-premises over MODBUS TCP while an event-driven MQTT gateway runs in parallel on the same platform to stream non-disruptive telemetry data to internet-based analytics without degrading local SCADA operations.
> **Evidence**: "While industrial requirements of control and monitoring can be met via the MODBUS TCP using the request–response model, the MQTT protocol complements its operation by fulfilling the IoT requirements, using the publish–subscribe pattern for M2M communications. The IoT protocol works in parallel with the MODBUS TCP and relays industrial data to an Internet-based server for remote monitoring, analysis, and archiving." (p. 2)

- **Constraint/Pattern**: Homogeneous Message Structure
- **Implication**: Applying the structural frame format of MODBUS messages directly inside the UTF-8-encoded payload of MQTT messages creates a single, unified message format that is maintained across both control and monitoring domains, solving the interoperability problem.
> **Evidence**: "To maintain a homogeneous message for the entire environment, industrial data are organized using the structure of MODBUS messages, formatted in the UTF-8 and then transferred in the payload of an MQTT publish message ... Using the arrangement of Figure 13a, the message structure, which is the MODBUS TCP, was maintained throughout the entire IIoT environment for both the control part and the monitoring part. This led to a unified message structure, unified data processing, and hence the interoperability problem was solved." (p. 13-14)

### 4. Context Assumptions

- **Assumption**: Infrastructure and Protocol Selection Dependencies
- **Implication**: Selection of communication channels and application protocols is tightly bounded by the application's physical environment, latency targets, and data transmission capabilities.
> **Evidence**: "The employment of a communication infrastructure and protocol depends on the field of application, the timing requirements, and the data transmission rates." (p. 2)

- **Assumption**: Low-Volume Small-Payload Domain
- **Implication**: The comparative evaluation of protocol efficiency is framed under the context that industrial and SCADA payload structures are strictly small and constrained.
> **Evidence**: "The figure shows values for fewer than 106 bytes because the message size in industrial applications and SCADA-like systems is small." (p. 11)
