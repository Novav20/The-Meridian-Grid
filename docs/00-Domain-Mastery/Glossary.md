---
title: "The Meridian Grid: Domain Mastery Glossary & Ubiquitous Language Index"
description: "Authoritative technical dictionary, ubiquitous language specifications, and cross-context invariants for The Meridian Grid SCADA & IIoT platform."
tags:
  - glossary
  - ubiquitous-language
  - domain-driven-design
  - scada
  - iiot
  - isa101
  - sparkplug-b
  - iec61850
  - iec62443
---

# Domain Mastery Glossary & Ubiquitous Language Index

This glossary serves as the **Single Source of Truth (SSOT)** for domain terminology, architectural invariants, and ubiquitous language across **The Meridian Grid (TMG)**. It bridges physical industrial automation, message transport, web graphics engines, cognitive human factors, and strategic software design.

Every entry provides the canonical definition, operational invariants, primary curriculum lessons, and literature traceability citations conforming to ISO/IEC 29110.

---

## Table of Contents
1. [[#1. Fieldbus Automation & Hardware Invariants]]
2. [[#2. Edge Ingestion, Security & Gateway Architecture]]
3. [[#3. Messaging Fabric, Transport & Protocols]]
4. [[#4. Serialization, Historians & Persistence]]
5. [[#5. Web Rendering Engines & Browser Performance]]
6. [[#6. High-Performance HMI & Visual Ergonomics]]
7. [[#7. Situational Awareness, AI Symbiosis & Ocular Ergonomics]]
8. [[#8. Strategic Domain-Driven Design & Enterprise Architecture]]

---

## 1. Fieldbus Automation & Hardware Invariants

### Application Data Unit (ADU)
The complete protocol frame transmitted across physical media, wrapping the protocol-independent Protocol Data Unit (PDU) with bus-specific routing headers and error checksums. In Modbus TCP, the ADU consists of the 7-byte MBAP header prepended to the PDU.
* **Primary Reference:** [[02-Modbus-TCP-Mechanics|Lesson 02: Modbus TCP Mechanics]]
* **Standard:** Modbus Application Protocol Specification v1.1b3

### Arc Flash Boundary (NFPA 70E)
The minimum approach boundary around energized electrical switchgear or open bus conductors where incident energy from a catastrophic electrical arcing fault drops to $1.2\text{ cal/cm}^2$ (the threshold for second-degree curable epidermal burns). Personnel crossing this boundary must don rated Arc-Rated (AR) Personal Protective Equipment.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Standard:** NFPA 70E / IEEE 1584

### Auxiliary Contacts (52a / 52b)
Electromechanical limit switches mechanically linked to the primary shaft of a high-voltage circuit breaker. Contact $52a$ is normally open (tracking main contact closure), while $52b$ is normally closed (tracking main contact separation). Both contacts are read simultaneously to determine double-point status.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Standard:** IEEE C37.2 / IEC 61850-7-2

### Conventional Graphical Symbols (CGS)
Standardized vector glyphs defined by IEC 61850-7-4 representing primary substation apparatus (circuit breakers `XCBR`, disconnectors `XSWI`, power transformers `YPTR`) on single-line diagrams.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Citation:** [[Dobrokhotov_et_al_2025|Dobrokhotov et al., 2025]]

### Double-Point Status (Dbpos)
A deterministic 2-bit state vector mandated by IEC 61850-7-2 for switchgear position monitoring: `00` (intermediate/transit), `01` (open/off), `10` (closed/on), and `11` (bad-state/hardware discrepancy). Prevents operational accidents caused by single-bit sensor ambiguities.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Standard:** IEC 61850-7-2 Clause 6.1.2.5

### Endianness (Endian Inversion)
The byte ordering sequence of multi-byte numbers in memory and on the wire. Big-Endian (network byte order, Modbus) places the most significant byte at the lowest address; Little-Endian (Protobuf, x86/ARM memory) places the least significant byte first. Failing to handle endianness inversion converts valid floating-point telemetry into corrupted subnormal values.
* **Primary Reference:** [[07-Protobuf-vs-Text-Serialization|Lesson 07: Protobuf vs. Text Serialization]]
* **Standard:** IEEE 754-2019

### Generic Object Oriented Substation Events (GOOSE)
An Ethernet Layer 2 multicast protocol defined in IEC 61850-8-1 for fast, deterministic inter-relay communications (sub-4 ms transfer time) that bypasses network IP stacks for critical trip commands.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Standard:** IEC 61850-8-1

### Hard Real-Time vs. Soft Real-Time
* **Hard Real-Time:** System execution where missing a deterministic task deadline ($\Delta t$) constitutes a total physical system failure or safety catastrophe (e.g., generator trip interlocks, protective relaying).
* **Soft Real-Time:** System execution where meeting deadlines is desirable and missing a deadline degrades service quality but does not cause physical damage (e.g., operator display refresh, historical logging).
* **Primary Reference:** [[01-Purdue-vs-UNS|Lesson 01: Purdue Model vs. Unified Namespace]], [[11-Monolithic-vs-Web-SCADA|Lesson 11: Monolithic vs. Web SCADA]]

### Hardware Watchdog Timer (WDT)
A dedicated electromechanical or microprocessor timing circuit that requires software firmware to periodically clear ("kick") a hardware counter. If software execution hangs, deadlocks, or loops infinitely, the timer expires and forces an immediate hardware CPU reset or de-energizes fail-safe output relays to safe state.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]]

### HART Protocol (Highway Addressable Remote Transducer)
A bi-directional industrial communications standard that superimposes digital Frequency Shift Keying (FSK) signals (Bell 202 standard at $1200\text{ bps}$) directly on top of continuous 4–20 mA analog instrument loop currents without disrupting the primary analog signal.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** FieldComm Group HART 7

### IEEE 754 Single-Precision Floating-Point
The standard 32-bit analog representation partitioning bits into 1 sign bit ($s$), 8 biased exponent bits ($e$, bias 127), and 23 mantissa fraction bits ($m$), providing $\approx 7.22$ decimal digits of precision.
* **Primary Reference:** [[07-Protobuf-vs-Text-Serialization|Lesson 07: Protobuf vs. Text Serialization]]
* **Standard:** IEEE 754-2019

### Manufacturing Message Specification (MMS)
An ISO 9506 client/server protocol running over TCP port 102, used in IEC 61850 architectures for supervisory SCADA acquisition of complex data objects from substation IEDs.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Standard:** ISO 9506 / IEC 61850-8-1

### Modbus Application Protocol (MBAP) Header
A 7-byte header prepended to Modbus TCP frames consisting of Transaction ID (2 bytes), Protocol ID (2 bytes: `0x0000`), Length (2 bytes), and Unit Identifier (1 byte), replacing the serial slave address and CRC.
* **Primary Reference:** [[02-Modbus-TCP-Mechanics|Lesson 02: Modbus TCP Mechanics]]
* **Standard:** Modbus TCP/IP Specification

### NAMUR NE43
An international instrumentation recommendation standardizing diagnostic signaling boundaries on 4–20 mA current loops:
* **Nominal Operating Range:** $3.8\text{ mA} \le I \le 20.5\text{ mA}$.
* **Underflow / Wire Break Fault:** $I < 3.6\text{ mA}$ (signals loop open circuit or sensor loss).
* **Overflow / Short-Circuit Fault:** $I > 21.0\text{ mA}$ (signals electrical short or sensor damage).
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** NAMUR NE 43 Recommendation

### PLC Hardware Scan Cycle
The deterministic four-stage loop executed by programmable logic controllers: (1) Read Physical Inputs, (2) Execute Control Logic, (3) Write Physical Outputs, and (4) Service Communications. Communication requests are constrained to a strict millisecond time slice ($10\text{--}20\text{ ms}$).
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]]

### Purdue Enterprise Reference Architecture (PERA / Purdue Model)
The classical hierarchical model (ISA-95) partitioning industrial automation into discrete physical and functional levels: Level 0 (Process), Level 1 (Control), Level 2 (Supervisory), Level 3 (Operations/MES), and Level 4/5 (Enterprise/Cloud).
* **Primary Reference:** [[01-Purdue-vs-UNS|Lesson 01: Purdue Model vs. Unified Namespace]]
* **Standard:** ANSI/ISA-95.00.01-2010

### Sequence of Events (SOE)
High-resolution chronologically indexed digital state change logs recorded directly in field I/O slice hardware buffers with hardware-timestamped accuracy down to $1\text{ ms}$ or microsecond precision. Enables exact chronological reconstruction of cascading physical trips across power grids and chemical facilities.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Standard:** IEEE Std 1815 (DNP3) / IEC 60870-5-104

### Substation Configuration Language (SCL)
An XML-based schema defined in IEC 61850-6 used to formally specify electrical single-line topology, communication networks, and IED logical nodes. Formats include System Specification Description (SSD), IED Capability Description (ICD), and Substation Configuration Description (SCD).
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Citation:** [[Dobrokhotov_et_al_2025|Dobrokhotov et al., 2025]]

---

## 2. Edge Ingestion, Security & Gateway Architecture

### Anti-Corruption Layer (ACL)
A Domain-Driven Design integration pattern implemented by a downstream consumer to translate non-cooperative, legacy, or proprietary models (e.g., Modbus registers) into a clean domain model (e.g., Sparkplug B objects) without polluting core domain logic.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic Domain-Driven Design]]
* **Citation:** Khononov (2022); [[Koltsova_et_al_2026|Koltsova et al., 2026]]

### Anti-Routing Invariant (`ip_forward = 0`)
The strict security rule requiring kernel IP forwarding to be permanently disabled on dual-homed edge gateways (`sysctl net.ipv4.ip_forward = 0`). Completely prevents Layer 3 packet routing between corporate IT subnets and OT machine networks.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]], [[10-OT-Cybersecurity-IEC-62443|Lesson 10: OT Cybersecurity]]
* **Citation:** [[Narayanan_et_al_2026|Narayanan et al., 2026]]

### Drop-SYN Firewall Policy
A host firewall rule on an edge gateway's upstream IT network interface that drops all incoming TCP `SYN` packets. The gateway exposes zero listening sockets to the network, communicating strictly via outbound client-initiated TLS sessions.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]], [[10-OT-Cybersecurity-IEC-62443|Lesson 10: OT Cybersecurity]]
* **Standard:** IEC 62443-3-3

### Dual-Homing
The architectural practice of equipping an edge gateway appliance with two physically discrete Network Interface Cards (NICs) connected to independent switches: NIC 1 dedicated to the isolated OT fieldbus, and NIC 2 dedicated to the enterprise/IDMZ network.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]]
* **Citation:** [[Narayanan_et_al_2026|Narayanan et al., 2026]]

### Edge-of-Network Node (EoN Node)
An intelligent industrial computing gateway that terminates legacy fieldbuses (Modbus, EtherNet/IP, serial), manages physical device state, and acts as the authorized publisher to the central Unified Namespace on behalf of physical controllers.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]], [[06-Sparkplug-B-Specification|Lesson 06: Sparkplug B]]
* **Standard:** Eclipse Sparkplug B Specification v3.0

### Industrial Demilitarized Zone (IDMZ / Level 3.5)
A perimeter security zone positioned between the industrial control network (Level 3) and the corporate enterprise network (Level 4). Contains message brokers, reverse proxies, and historians; no direct traffic is permitted to traverse between OT and IT without terminating in the IDMZ.
* **Primary Reference:** [[10-OT-Cybersecurity-IEC-62443|Lesson 10: OT Cybersecurity]]
* **Standard:** IEC 62443-3-2 / ANSI/ISA-95

### Protocol Encapsulation vs. Protocol Termination
* **Protocol Encapsulation (Tunneling):** Wrapping raw legacy frames (e.g., Modbus bytes) inside modern transport packets (e.g., MQTT or WebSocket), requiring upstream clients to parse legacy memory offsets.
* **Protocol Termination:** The edge gateway fully unpacks legacy frames, extracts raw values, applies engineering calibration, and publishes normalized semantic metrics.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]]
* **Citation:** [[Jiao_et_al_2018|Jiao & Sun, 2018]]

### Store-and-Forward (SaF)
A local buffering mechanism in edge gateways that spools polled process metrics to non-volatile local storage during wide-area network outages, preserving exact local acquisition timestamps for replay upon link restoration.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]]

### Timestamp Preservation Invariant
The immutable rule that edge-buffered telemetry records must retain their original fieldbus acquisition timestamp during network disconnection and store-and-forward playback, rather than receiving the transmission timestamp.
* **Primary Reference:** [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]], [[09-Time-Series-Historians|Lesson 09: Time-Series Historians]]

---

## 3. Messaging Fabric, Transport & Protocols

### Birth and Death Certificates (Sparkplug B)
Protocol payloads that establish and tear down state in the Unified Namespace:
* `NBIRTH` / `NDEATH`: Published by the Edge-of-Network gateway declaring its online metric inventory or ungraceful disconnection.
* `DBIRTH` / `DDEATH`: Published for specific physical end devices connected behind the EoN node.
* **Primary Reference:** [[06-Sparkplug-B-Specification|Lesson 06: Sparkplug B Specification]]
* **Standard:** Eclipse Sparkplug B Specification v3.0

### Birth-Death Sequence Counter (`bdSeq`)
An unsigned 64-bit integer monotonically incremented by an EoN node each time it publishes a new `NBIRTH` payload. Paired with the MQTT Last Will and Testament (LWT) `NDEATH` message to prevent stale death certificates from invalidating active sessions.
* **Primary Reference:** [[06-Sparkplug-B-Specification|Lesson 06: Sparkplug B Specification]]

### Drop-Oldest (FIFO Head Eviction)
The mandated queue overflow policy in SCADA brokers where newly arriving real-time telemetry displaces the oldest unconsumed messages from a congested subscriber queue, ensuring operators always receive live process state.
* **Primary Reference:** [[04-Broker-Failure-Modes-Backpressure|Lesson 04: Broker Failure Modes & Backpressure]]
* **Citation:** [[Liu_et_al_2023|Liu & Al-Masri, 2023]]

### MQTT 5.0
An OASIS standard binary publish/subscribe messaging protocol operating over TCP. Introduces User Properties, Reason Codes, Message Expiry Intervals, Topic Aliases, and Clean Start session handling.
* **Primary Reference:** [[03-MQTT-Protocol-Internals|Lesson 03: MQTT Protocol Internals]]
* **Standard:** OASIS MQTT Version 5.0

### OPC Unified Architecture (OPC UA)
An IEC 62541 cross-platform, service-oriented industrial communications standard providing complex information modeling, semantic object hierarchies, and built-in PKI security profiles. Operates primarily via client-server TCP binary connections (port 4840) and Pub/Sub extensions (UDP/MQTT).
* **Primary Reference:** [[01-Purdue-vs-UNS|Lesson 01: Purdue Model vs. Unified Namespace]], [[05-EoN-Nodes-Brownfield-Gateways|Lesson 05: EoN Nodes & Brownfield Gateways]]
* **Standard:** IEC 62541 (Parts 1–14)

### Quality of Service (QoS)
Delivery guarantees defined by the MQTT protocol:
* **QoS 0 (At most once):** Best-effort fire-and-forget; zero acknowledgment frames.
* **QoS 1 (At least once):** Handshake verified via `PUBACK`; messages may be duplicated.
* **QoS 2 (Exactly once):** Four-step handshake (`PUBLISH`, `PUBREC`, `PUBREL`, `PUBCOMP`); guaranteed single delivery.
* **Primary Reference:** [[03-MQTT-Protocol-Internals|Lesson 03: MQTT Protocol Internals]]

### Remistry Multiprocessing Pattern
An architectural design for MQTT brokers that isolates client connection queues across independent operating system worker processes via Copy-on-Write (`fork()`), ensuring a slow subscriber crash or OOM kill isolates to that worker without taking down the global broker daemon.
* **Primary Reference:** [[04-Broker-Failure-Modes-Backpressure|Lesson 04: Broker Failure Modes & Backpressure]]
* **Citation:** [[Liu_et_al_2023|Liu & Al-Masri, 2023]]

### Report-by-Exception (RBE)
A communication policy where field nodes transmit telemetry updates strictly when a process value changes beyond a configured deadband or its operational state toggles, reducing network bandwidth utilization by $80\text{--}95\%$.
* **Primary Reference:** [[03-MQTT-Protocol-Internals|Lesson 03: MQTT Protocol Internals]], [[06-Sparkplug-B-Specification|Lesson 06: Sparkplug B]]

### Sparkplug B
An industrial open specification developed by the Eclipse Foundation standardizing topic naming conventions (`spBv1.0/group_id/message_type/edge_node_id/[device_id]`), state management (birth/death certificates), metric aliases, and Google Protocol Buffer payload schemas over MQTT.
* **Primary Reference:** [[06-Sparkplug-B-Specification|Lesson 06: Sparkplug B Specification]]
* **Standard:** Eclipse Sparkplug B Specification v3.0

### TCP ZeroWindow
A TCP flow-control mechanism where a receiving node advertises a window size of zero (`Win=0`) in its TCP header, signaling to the sender that its operating system receive buffer (`SO_RCVBUF`) is completely full. Forces the sending socket into an un-drained stalled state.
* **Primary Reference:** [[04-Broker-Failure-Modes-Backpressure|Lesson 04: Broker Failure Modes & Backpressure]]

### Telemetry Conflation
The client-side buffering strategy that reconciles high-frequency telemetry streams with display refresh limits:
* **Tier 1 (Lossy Last-Value):** High-frequency analog trends overwrite previous un-rendered values in memory; only the latest value is rendered per frame.
* **Tier 2 (Lossless FIFO):** Critical state changes, discrete trip signals, and sequence-of-events alarms are preserved in a strict FIFO queue without dropping.
* **Primary Reference:** [[12-WebSocket-Streaming-Mechanics|Lesson 12: WebSocket Streaming Mechanics]]

### Unified Namespace (UNS)
A unified, event-driven software architecture where all industrial operational data, business context, and asset metrics are organized into a standardized, hierarchical topic tree (grounded in ISA-95) functioning as the enterprise Single Source of Truth (SSOT).
* **Primary Reference:** [[01-Purdue-vs-UNS|Lesson 01: Purdue Model vs. Unified Namespace]], [[08-ISA-95-Object-Models-Taxonomy|Lesson 08: ISA-95 Object Models]]

---

## 4. Serialization, Historians & Persistence

### Base-128 Varint
A variable-length integer encoding method used by Protocol Buffers. Uses the 7 least significant bits of each byte for numerical data and the Most Significant Bit (MSB, Bit 7) as a continuation flag (`1` = more bytes follow, `0` = terminating byte).
* **Primary Reference:** [[07-Protobuf-vs-Text-Serialization|Lesson 07: Protobuf vs. Text Serialization]]

### Batch Accumulator Worker
An in-memory ingestion service that pools incoming real-time telemetry records into bounded ring buffers, committing them to persistent disk storage using bulk SQL `COPY` statements to amortize transaction log overhead and eliminate WAL contention.
* **Primary Reference:** [[19-Hot-Path-vs-Cold-Path-Pipelines|Lesson 19: Dual-Path Processing]]
* **Citation:** [[Villamar_et_al_2025|Villamar et al., 2025]]

### Continuous Aggregates
Materialized, incrementally refreshed downsampling views in TimescaleDB that automatically precompute time-bucketed rollups (averages, minimums, maximums, standard deviations), accelerating multi-day trend queries.
* **Primary Reference:** [[09-Time-Series-Historians|Lesson 09: Time-Series Historians]]

### Delta-of-Delta Compression
A lossless integer compression algorithm optimized for monotonically increasing timestamps. Encodes the difference between successive sample time intervals ($\Delta^2 = (t_i - t_{i-1}) - (t_{i-1} - t_{i-2})$), yielding variable-bit lengths as small as 1 bit for steady periodic samples.
* **Primary Reference:** [[09-Time-Series-Historians|Lesson 09: Time-Series Historians]]
* **Citation:** Pelkonen et al. (2015, Facebook Gorilla)

### Dual-Path Telemetry Bifurcation
The architectural separation of industrial telemetry pipelines into:
* **Hot Path:** In-memory, non-blocking streaming (< 25–50 ms) to operator HMIs via WebSockets without disk dependencies.
* **Cold Path:** Batch-buffered, append-only persistence (150–300 ms) into relational hypertables for historical trending and analytics.
* **Primary Reference:** [[19-Hot-Path-vs-Cold-Path-Pipelines|Lesson 19: Dual-Path Processing]]
* **Citation:** [[Grigat_et_al_2026|Grigat et al., 2026]]; [[Villamar_et_al_2025|Villamar et al., 2025]]

### Gorilla XOR Compression
A lossless floating-point compression algorithm that computes the XOR bitwise difference between consecutive IEEE 754 floating-point values ($v_i \oplus v_{i-1}$). Exploits identical leading and trailing zero bits to achieve up to a 12:1 storage footprint reduction on slowly changing analog signals.
* **Primary Reference:** [[09-Time-Series-Historians|Lesson 09: Time-Series Historians]]
* **Citation:** Pelkonen et al. (2015, Facebook Gorilla)

### Hypertables & Chunks (TimescaleDB)
An abstraction over relational database tables that automatically partitions data across chronological time intervals into discrete underlying PostgreSQL tables called chunks. Ensures active write transactions interact only with chunks pinned in RAM, avoiding B-tree index thrashing.
* **Primary Reference:** [[09-Time-Series-Historians|Lesson 09: Time-Series Historians]]

### Largest Triangle Three Buckets (LTTB)
A downsampling algorithm designed for time-series visualization that decimates $N$ data points down to $K$ pixels while strictly preserving visual extrema, perceptual trends, and peak amplitudes through triangular area maximization.
* **Primary Reference:** [[09-Time-Series-Historians|Lesson 09: Time-Series Historians]]
* **Citation:** Steinarsson (2013)

### Protocol Buffers (Protobuf)
A compact, language-neutral binary serialization format developed by Google utilizing compiled `.proto` schemas, Tag-Length-Value (TLV) field packing, and Base-128 varints. Eliminates string field names from over-the-wire payloads.
* **Primary Reference:** [[07-Protobuf-vs-Text-Serialization|Lesson 07: Protobuf vs. Text Serialization]]
* **Citation:** [[Senk_et_al_2026|Šenk et al., 2026]]

### Write-Ahead Log (WAL)
A persistent append-only log on disk where database engines record state modifications before updating data pages in memory, guaranteeing ACID durability via synchronous `fsync()` barriers.
* **Primary Reference:** [[19-Hot-Path-vs-Cold-Path-Pipelines|Lesson 19: Dual-Path Processing]]

### ZigZag Encoding
A mapping algorithm in Protocol Buffers that converts signed integers into positive unsigned integers by interleaving negative and positive numbers ($2n$ for $n \ge 0$, and $-2n - 1$ for $n < 0$), preventing small negative numbers from serializing as 10-byte 64-bit varints.
* **Primary Reference:** [[07-Protobuf-vs-Text-Serialization|Lesson 07: Protobuf vs. Text Serialization]]

---

## 5. Web Rendering Engines & Browser Performance

### 16.6 ms Frame Budget (60 FPS Execution Floor)
The maximum execution time allocated to the browser rendering engine to process incoming telemetry, execute scripts, calculate styles, compute layout geometry, and composite a single visual frame:
$$\text{Frame Budget} = \frac{1{,}000\text{ ms}}{60\text{ frames}} \approx 16.67\text{ ms / frame}$$
Exceeding this budget causes dropped frames perceived by operators as visual jank.
* **Primary Reference:** [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]]

### Critical Rendering Path
The sequential pipeline executed by browser engines to render a frame: (1) JavaScript execution, (2) Style Recalculation, (3) Layout (Reflow), (4) Paint (Rasterization), and (5) GPU Compositing.
* **Primary Reference:** [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]]

### Cross-Origin Isolation (COOP / COEP)
A high-security browser environment activated by serving top-level HTTP response headers: `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp`. Mandatory requirement for enabling `SharedArrayBuffer` in modern browsers.
* **Primary Reference:** [[15-Multithreaded-Web-Performance|Lesson 15: Multithreaded Web Performance]]

### Hybrid Viewport Stacking Strategy
The multi-layer graphics architecture in The Meridian Grid that stacks:
* **Layer 1 (Bottom, `z-index: 100`):** Retained-mode SVG synoptics with reusable `<defs>` symbols.
* **Layer 2 (Middle, `z-index: 200`):** Immediate-mode Canvas 2D/WebGL surface (`pointer-events: none`) for high-frequency 100 Hz curves.
* **Layer 3 (Top, `z-index: 300`):** HTML5 DOM HUD for accessible alarm lists, tabular modals, and control buttons.
* **Primary Reference:** [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]]
* **Citation:** [[Bellini_et_al_2022|Bellini et al., 2022]]; [[Jiao_et_al_2018|Jiao et al., 2018]]

### Layout Reflow Cliff
The performance degradation point in retained-mode DOM/SVG trees where exceeding $3{,}000\text{--}5{,}000$ active dynamic nodes causes CPU-bound geometric box recalculations, exceeding the $16.6\text{ ms}$ frame budget and freezing the UI thread.
* **Primary Reference:** [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]]

### Master Definition (`<defs>`) & Shadow Instantiation (`<use>`)
The SVG template pattern where complex vector geometry is declared once in the `<defs>` section and referenced across the canvas via `<use href="#id">`, cutting V8 DOM heap allocation by over $85\%$.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]]
* **Citation:** [[Dobrokhotov_et_al_2025|Dobrokhotov et al., 2025]]

### OffscreenCanvas API
A browser API that transfers rendering control of a `<canvas>` element from the main UI thread to a background Web Worker, isolating high-frequency drawing loops from operator input handling.
* **Primary Reference:** [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]], [[15-Multithreaded-Web-Performance|Lesson 15: Multithreaded Web Performance]]

### Retained-Mode vs. Immediate-Mode Graphics
* **Retained-Mode (HTML DOM / SVG):** The browser maintains an in-memory hierarchical object tree of every visual element, tracking bounds, hit-testing, and CSS styles automatically.
* **Immediate-Mode (Canvas 2D / WebGL):** Commands issue direct drawing calls to a flat pixel bitmap buffer without creating or persisting DOM nodes.
* **Primary Reference:** [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]]

### Single-Producer / Single-Consumer (SPSC) Ring Buffer
A lock-free circular memory structure allocated inside a `SharedArrayBuffer` where a single writer thread (Ingestion Worker) appends data and publishes via `Atomics.store()`, and a single reader thread (Render Worker) reads via `Atomics.load()`, eliminating mutex overhead and heap allocations.
* **Primary Reference:** [[15-Multithreaded-Web-Performance|Lesson 15: Multithreaded Web Performance]]

### Zero-Reflow Attribute Mutation
The practice of updating dynamic visual states exclusively via CSS classes or `data-*` attributes mapped to hardware-accelerated compositor properties (`transform`, `opacity`), skipping the browser's CPU Layout (Reflow) stage entirely.
* **Primary Reference:** [[13-Declarative-SVG-Synthesis|Lesson 13: Declarative SVG Synthesis]], [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]]

---

## 6. High-Performance HMI & Visual Ergonomics

### "Christmas Tree" HMI Anti-Pattern
The legacy design flaw of applying bright, saturated rainbow colors (neon green for running pumps, bright red for stopped equipment, yellow for gas pipes) across normal, steady-state process screens. Saturates foveal attention and obscures actual alarms.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** ANSI/ISA-101.01-2015

### 4-Tier Supervisory Display Hierarchy
The progressive disclosure display model mandated by ANSI/ISA-101.01:
* **Level 1 (Overview):** Entire facility macro KPIs; zero direct command execution.
* **Level 2 (Unit Control):** Primary operating screen for specific process units (where operators spend $>90\%$ of shifts).
* **Level 3 (Detail / Trend):** Specific equipment faceplates, interlock permissive matrices, and micro-trends.
* **Level 4 (Diagnostic):** Raw instrument loop currents, PLC registers, and calibration blocks.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** ANSI/ISA-101.01-2015

### Alarm Shelving & Suppression (ISA-18.2)
A formal alarm management state mechanism defined in ANSI/ISA-18.2:
* **Shelving:** A temporary, operator-initiated silencing of a nuisance, chattering, or repeating alarm with an automatic expiration timer.
* **Suppression:** An engineering or logic-driven bypass of an alarm during specific operating modes (e.g., suppressing low-pressure alarms while a compressor is stopped for maintenance).
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** ANSI/ISA-18.2 Clause 11

### Color Vision Deficiency (CVD) Dual-Encoding
The life-safety design rule under ANSI/ISA-18.2 requiring alarm indicators to redundant-encode priority through **Color + Geometric Shape + Numeric Digit + Annunciation State** (e.g., Priority 1 = Coral Red + Square + "1" + Flashing), ensuring legibility for operators with congenital color blindness.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** ANSI/ISA-18.2 / ANSI/ISA-101.01

### Grayscale Canvas Baseline
The visual discipline mandating that $85\text{--}90\%$ of screen elements reside in neutral gray or slate tones. Saturated colors are strictly reserved for abnormal conditions and active alarms.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** ANSI/ISA-101.01-2015

### Invariant Neutral Pointer
The Moving Analog Indicator requirement that the process variable value pointer remain neutral white or dark slate across all operating states, never recoloring in alarm. Value magnitude is communicated purely by spatial position.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]

### Management of Change (MOC)
A formal regulatory and engineering procedure (mandated under OSHA 1910.119 Process Safety Management) that evaluates the safety, operational, and instrumentation impacts of modifying equipment, alarm setpoints, or control software before changes are deployed to live production.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]], [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Standard:** OSHA 1910.119(l) / ANSI/ISA-18.2

### Method 3 Separate Alarm Indicator Placement
The ISA-18.2 standard alarm display approach where operating limits are marked as thin neutral notches on a gauge, and active alarms appear as a separate, distinct geometric badge immediately adjacent to the breached notch, rejecting the anti-patterns of recoloring the pointer (Method 1) or painting colored background bands (Method 2).
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** ANSI/ISA-18.2 / ANSI/ISA-101.01

### Moving Analog Indicator (MAI)
An analog moving-bar indicator widget projecting process measurements onto a spatial axis showing the normal target operating band, regulatory setpoint chevron, deviation bracket, and Method 3 alarm notches. Eliminates the cognitive friction of reading raw numerical floating-point numbers.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Standard:** ANSI/ISA-101.01-2015

### Polar Radar Profile (Spider Chart)
A multi-variable graphic plotting $6\text{--}12$ normalized process parameters along radial axes. In nominal steady state, the profile forms a symmetrical regular polygon; process upsets deform the geometry, triggering preattentive peripheral detection in $< 200\text{ ms}$ under Gestalt visual perception rules.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]

### Saccadic Search Time
The time required for an operator's foveal vision to perform serial jumps across cluttered screen elements to locate an anomaly ($15\text{--}30\text{ seconds}$ in legacy HMIs vs. $< 2\text{ seconds}$ in High-Performance HMIs).
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]]
* **Citation:** [[Verdejo_et_al_2026|Verdejo et al., 2026]]

### Two-Stage "Arm-and-Execute" Confirmation Barrier
A safety mechanism for control dispatches: Stage 1 arms the command buffer and starts a countdown window; Stage 2 requires an explicit confirmation action on a spatially distant target, preventing accidental touch triggers on industrial kiosks.
* **Primary Reference:** [[16-ISA-101-High-Performance-HMI|Lesson 16: ANSI/ISA-101 High-Performance HMI]], [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]

---

## 7. Situational Awareness, AI Symbiosis & Ocular Ergonomics

### 5W+H Situation Model
The structured semantic representation instantiated on the ALARMS shared blackboard: **Who** (affected equipment), **What** (physical anomaly pattern), **When** (onset and elapsed time), **Where** (ISA-95 location path), **Why** (upstream root cause), and **How** (physical propagation mechanism).
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Citation:** [[Verdejo_et_al_2026|Verdejo et al., 2026]]

### ALARMS Multi-Agent Cognitive Framework
A decoupled multi-agent architecture composed of five specialized agents: **Analysis**, **Locutor**, **Anticipation**, **Risk Manager**, and **Simulation**, cooperating via an in-memory 5W+H blackboard to support operator situational awareness without overriding human control authority.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Citation:** [[Verdejo_et_al_2026|Verdejo et al., 2026]]

### Automation Complacency & Bias
The psychological failure mode where human operators cultivate uncalibrated trust in automated algorithms, ceasing active verification of underlying physical sensor values and deferring to automated outputs during design edge cases.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Citation:** [[Verdejo_et_al_2026|Verdejo et al., 2026]]

### Critical Flicker Fusion (CFF)
The temporal threshold frequency (in Hz) at which an intermittent light flash appears continuous. Serves as a clinical physiological biomarker of central nervous system retinocortical exhaustion; drops significantly under visual presentation velocities $\ge 16^\circ/\text{s}$.
* **Primary Reference:** [[18-Human-Visual-Fatigue-Limits|Lesson 18: Human Visual Fatigue Limits]]
* **Citation:** [[Tong_et_al_2026|Tong et al., 2026]]

### Decision Reaction Fallacy
The empirical discovery by Tong et al. (2026) proving that when presentation speed exceeds $8^\circ/\text{s}$, the surge in operator error is driven almost exclusively by **incorrect operational decisions** ($p < 0.001$), while raw target omission rates remain statistically flat.
* **Primary Reference:** [[18-Human-Visual-Fatigue-Limits|Lesson 18: Human Visual Fatigue Limits]]
* **Citation:** [[Tong_et_al_2026|Tong et al., 2026]]

### Dynamic Presentation Velocity Invariant
The non-negotiable architectural rule that dynamic graphical motion across an HMI display must be constrained within **$4^\circ/\text{s} \le \omega \le 12^\circ/\text{s}$ of visual angle**, and must **strictly never exceed $16^\circ/\text{s}$**.
* **Primary Reference:** [[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]], [[18-Human-Visual-Fatigue-Limits|Lesson 18: Human Visual Fatigue Limits]], [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** [[Tong_et_al_2026|Tong et al., 2026]]

### Dynamic Pupil Diameter Fallacy
The established finding that average pupil diameter is an invalid, ungrounded metric for detecting operator fatigue in dynamic supervisory tasks, because parasympathetic fatigue constriction (miosis) and sympathetic motion-tracking dilation (mydriasis) act in equal and opposite push-pull cancellation ($p > 0.05$).
* **Primary Reference:** [[18-Human-Visual-Fatigue-Limits|Lesson 18: Human Visual Fatigue Limits]]
* **Citation:** [[Tong_et_al_2026|Tong et al., 2026]]

### Endsley’s 3-Level Situational Awareness Model
The foundational cognitive framework stratifying operational awareness:
* **Level 1 (Perception):** Perceiving raw telemetry, states, and annunciator badges.
* **Level 2 (Comprehension):** Synthesizing multivariable data into a holistic mental model of *why* the process is behaving in that manner.
* **Level 3 (Projection):** Extrapolating dynamic states forward in time to anticipate future interlock trips and available intervention time.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Citation:** Endsley (1995); [[Verdejo_et_al_2026|Verdejo et al., 2026]]

### Epistemic Uncertainty Envelope ($\pm 2\sigma$)
The statistical confidence fan displayed during predictive trajectory forecasting, communicating potential physical outcomes and bounds rather than plotting a single misleading deterministic forecast.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]

### Locutor Agent (Socratic Cognitive Mirror)
The orthogonal conversational agent in the ALARMS framework that interfaces with the human operator. Rejects prescriptive direct commands in favor of Socratic dialectic inquiries (*"You are observing X; have you verified variable Y?"*), reframing operator focus and breaking cognitive tunneling.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Citation:** [[Verdejo_et_al_2026|Verdejo et al., 2026]]

### Out-of-the-Loop Unawareness (OOTLU)
The state of disorientation that occurs when an automated system operates silently in the background and suddenly trips or drops control back to the human operator, who lacks the real-time mental model required to intervene safely within critical decision margins.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Citation:** Endsley (1995); [[Verdejo_et_al_2026|Verdejo et al., 2026]]

### Situation Awareness Rating Technique (SART)
A standardized subjective assessment measuring three cognitive dimensions: Attentional Demand ($D$), Attentional Supply ($S$), and Understanding ($U$). At visual velocities $\ge 14\text{--}16^\circ/\text{s}$, demand surpasses supply ($D > S$), triggering acute loss of situational awareness.
* **Primary Reference:** [[18-Human-Visual-Fatigue-Limits|Lesson 18: Human Visual Fatigue Limits]]
* **Citation:** [[Tong_et_al_2026|Tong et al., 2026]]

### Smooth Pursuit Blink Suppression
The neurological reflex where the central nervous system suppresses the spontaneous eye blink reflex to avoid losing visual lock during fast smooth-pursuit tracking ($\ge 16^\circ/\text{s}$), reducing blink frequency from $15\text{--}22$ down to $< 4\text{--}6\text{ blinks/min}$ and causing corneal tear film desiccation (TBUT failure).
* **Primary Reference:** [[18-Human-Visual-Fatigue-Limits|Lesson 18: Human Visual Fatigue Limits]]
* **Citation:** [[Tong_et_al_2026|Tong et al., 2026]]

### Visual Angle Velocity ($\omega$)
The biophysical rate at which a moving image traverses the human retina, expressed in degrees of visual angle per second ($^\circ/\text{s}$):
$$\omega \approx \frac{180}{\pi D} \cdot \left( v_{\text{px}} \cdot p_{\text{pitch}} \right)$$
Accounts for physical viewing distance $D$, screen resolution, and pixel pitch $p_{\text{pitch}}$, replacing ungrounded pixels-per-second measurements.
* **Primary Reference:** [[18-Human-Visual-Fatigue-Limits|Lesson 18: Human Visual Fatigue Limits]]
* **Citation:** [[Tong_et_al_2026|Tong et al., 2026]]

### Weak-Signal Anomaly Detection
The statistical detection of subtle divergences between multivariable process telemetry and dynamic physical observer models (e.g., via CUSUM or Sequential Probability Ratio Testing) occurring well within static alarm trip limits, providing up to $+114\text{ seconds}$ of lead time before threshold breach.
* **Primary Reference:** [[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness]]
* **Citation:** [[Verdejo_et_al_2026|Verdejo et al., 2026]]

---

## 8. Strategic Domain-Driven Design & Enterprise Architecture

### Bounded Context
An explicit architectural perimeter within which a specific Ubiquitous Language is consistently and unambiguously defined. Prevents domain models from polluting adjacent subsystems with conflicting semantic meanings.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022); [[Koltsova_et_al_2026|Koltsova et al., 2026]]

### Context Map
A high-level architectural diagram defining the integration relationships, communication protocols, published languages, and organizational boundaries between Bounded Contexts.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)

### Core Subdomain
A high-complexity, high-volatility domain capability that provides direct competitive advantage and proprietary differentiation (e.g., in-memory UNS routing, dynamic SVG scene graphs, symbiotic cognitive mirroring). Must be engineered in-house with paramount architectural rigor.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)

### Customer-Supplier Relationship
An integration pattern where a downstream context (Customer) depends on an upstream context (Supplier). The upstream team accounts for downstream requirements in its published interfaces.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)

### Data Ownership Preservation Invariant
The non-negotiable architectural invariant stating that message brokers, data exchange fabrics, and HMI renderers provide transit and presentation capabilities but are **strictly prohibited from assuming data ownership**. The physical emitting device (sensor, PLC, or RTU) remains the sole authoritative source of truth.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** [[Koltsova_et_al_2026|Koltsova et al., 2026]]

### Generic Subdomain
A high-complexity but standardized commodity domain capability common across industries that provides zero business differentiation (e.g., relational time-series storage, MQTT broker daemons, cryptographic TLS libraries). Must be adopted off-the-shelf.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)

### Open-Host Service (OHS) & Published Language (PL)
An integration pattern where an upstream context provides a versioned, standardized public contract (Published Language) that any number of downstream consumers can integrate with without custom protocol adapters.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)

### RESTful Client Isolation Invariant
The security invariant restricting remote HMI web clients from issuing direct fieldbus register queries to physical PLCs. Clients must query telemetry exclusively through intermediate Open-Host Service gateways or WebSocket proxies, shielding controllers from external network loads.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** [[Villamar_et_al_2025|Villamar et al., 2025]]

### Strategic Domain-Driven Design (Strategic DDD)
The discipline of analyzing business domains, partitioning problem spaces into Core, Generic, and Supporting Subdomains, and isolating solutions within explicit Bounded Contexts connected via formal integration patterns.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)

### Supporting Subdomain
A low-complexity, low-volatility auxiliary capability required to support system operations but offering no competitive differentiation (e.g., IEC 61850 SCL XML parsers, CSV export utilities).
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)

### Ubiquitous Language
A rigorous, unambiguous vocabulary shared by domain experts and software engineers, strictly scoped and enforced within the perimeter of a specific Bounded Context.
* **Primary Reference:** [[20-Strategic-Domain-Driven-Design|Lesson 20: Strategic DDD]]
* **Citation:** Khononov (2022)
