---
title: "Lesson 12: WebSocket Streaming Mechanics vs. HTTP Polling"
difficulty: Advanced
prerequisites:
  - "[[07-Protobuf-vs-Text-Serialization|Lesson 07: Google Protocol Buffers vs. Text Serialization (JSON / XML)]]"
  - "[[10-OT-Cybersecurity-IEC-62443|Lesson 10: OT Cybersecurity & Network Architecture]]"
  - "[[11-Monolithic-vs-Web-SCADA|Lesson 11: Monolithic Desktop SCADA vs. Decoupled Web Architectures]]"
core_concepts:
  - "HTTP Polling Overhead vs. Persistent Full-Duplex Sockets"
  - "RFC 6455 Handshake, Frame Layout & Opcodes"
  - "Backpressure & Telemetry Conflation (Lossy vs. Lossless Tiers)"
  - "Report-by-Exception State Resynchronization"
  - "Stateful Firewall Keep-Alives (Ping/Pong)"
tags:
  - scada
  - iiot
  - web-scada
  - websockets
  - rfc6455
  - real-time-streaming
  - backpressure
  - purdue-model
  - idmz
---
# Lesson 12: WebSocket Streaming Mechanics vs. HTTP Polling

Industrial supervisory control and data acquisition (SCADA) platforms demand deterministic, sub-second latency between physical plant events and operator visual displays ([[Villamar_et_al_2025|Villamar et al., 2025]]; [[Bellini_et_al_2022|Bellini et al., 2022]]). Traditional web architectures grounded in the standard HTTP request-response cycle introduce severe structural bottlenecks when applied to real-time industrial telemetry. This lesson examines the cyber-physical network constraints of factory-floor communication, exposes the architectural failure modes of HTTP short and long polling, and details the binary framing and [[../Glossary#Telemetry Conflation|backpressure conflation mechanics]] of **RFC 6455 WebSockets**. WebSocket delivery and any state-resynchronization protocol are architectural candidates, not implemented features.

---

## 1. Physical Reality & Field Equipment (Prerequisites)

Real-time telemetry ingestion on the web cannot be analyzed as an abstract software problem. It is dictated by the physical characteristics of industrial communication media, network buffers, and operating environments:

### Physical Network Reality in Industrial Facilities
As illustrated in **Figure 12.1**, resilient field streaming relies on rugged physical communication hardware deployed across process units and network boundaries:

1. **Electrically Hostile Environments & Signal Attenuation:** In chemical plants, steel mills, and electrical substations, electromagnetic interference (EMI) from variable frequency drives (VFDs), large induction motors, and high-voltage switchgear induces packet jitter and transient bit errors.
2. **Wireless Edge Connectivity & Roaming Latency (Figure 12.1(a)):** Operators using mobile tablet HMIs navigate across hazardous process areas (ATEX Zone 2 / Class 1 Div 2). Handheld devices roam between industrial Wi-Fi access points (such as the Cisco Catalyst IW6300). Signal degradation around massive steel pressure vessels causes transient link drops, packet loss, and TCP congestion window collapse.
3. **Hardware Gateway Socket Buffers (Figure 12.1(b)):** In the IDMZ, an edge SCADA server (such as the modular fanless Advantech MIC-770 V2 IPC) terminates thousands of concurrent telemetry streams. If network buffers on intermediate switches or client transceivers overflow, unmanaged packet queueing leads to severe buffer bloat, multi-second telemetry lag, and stale process mimics.

The physical operational infrastructure enabling wireless fieldbus roaming and centralized IDMZ WebSocket termination is shown in **Figure 12.1**:

<figure align="center">
  <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <div style="flex: 1 1 340px; max-width: 48%; text-align: center; background: #16191F; border: 1px solid #30363D; border-radius: 8px; padding: 12px; box-sizing: border-box;">
      <!-- PHOTO SEARCH GUIDANCE: "Cisco Catalyst IW6300 heavy duty industrial access point" -->
      <img src="../photos/12-industrial-wifi-ap.avif" alt="IP67 Ruggedized Industrial Wi-Fi 6 Access Point (Cisco IW6300)" style="width: 100%; height: 260px; object-fit: contain; background: #0D1117; border-radius: 6px; border: 1px solid #21262D;" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" />
      <div style="display: none; height: 260px; background: #0D1117; border: 1px dashed #30363D; border-radius: 6px; padding: 16px; text-align: center; color: #8B949E; box-sizing: border-box; flex-direction: column; justify-content: center; align-items: center;">
        <span style="font-weight: 700; color: #58A6FF;">[Photo 12.1A: Industrial Heavy-Duty Wi-Fi Access Point]</span><br />
        <span style="font-size: 0.82em; display: block; margin-top: 6px;">Cisco Catalyst IW6300 IP67 heavy-duty access point delivering wireless fieldbus connectivity to mobile operator tablets in hazardous areas.</span>
        <span style="font-size: 0.72em; color: #6E7681; display: block; margin-top: 6px;">Search: "Cisco Catalyst IW6300 heavy duty industrial access point"</span>
      </div>
      <br>
      <small><strong>(a)</strong> IP67 Ruggedized Industrial Wi-Fi 6 Access Point (Cisco IW6300)</small>
    </div>
    <div style="flex: 1 1 340px; max-width: 48%; text-align: center; background: #16191F; border: 1px solid #30363D; border-radius: 8px; padding: 12px; box-sizing: border-box;">
      <!-- PHOTO SEARCH GUIDANCE: "Advantech MIC-770 fanless modular computer" -->
      <img src="../photos/12-edge-scada-gateway.jpg" alt="Modular Fanless Edge Server Terminating IDMZ WebSocket Sessions (Advantech MIC-770 V2)" style="width: 100%; height: 260px; object-fit: contain; background: #0D1117; border-radius: 6px; border: 1px solid #21262D;" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" />
      <div style="display: none; height: 260px; background: #0D1117; border: 1px dashed #30363D; border-radius: 6px; padding: 16px; text-align: center; color: #8B949E; box-sizing: border-box; flex-direction: column; justify-content: center; align-items: center;">
        <span style="font-weight: 700; color: #3FB950;">[Photo 12.1B: Modular Fanless Industrial Edge Server]</span><br />
        <span style="font-size: 0.82em; display: block; margin-top: 6px;">Advantech MIC-770 V2 modular fanless computer terminating thousands of concurrent full-duplex WebSocket telemetry streams in the Purdue IDMZ.</span>
        <span style="font-size: 0.72em; color: #6E7681; display: block; margin-top: 6px;">Search: "Advantech MIC-770 fanless modular computer"</span>
      </div>
      <br>
      <small><strong>(b)</strong> Fanless Industrial Server Terminating IDMZ WebSocket Sessions (Advantech MIC-770 V2)</small>
    </div>
  </div>
  <figcaption><em>Figure 12.1: Physical Streaming Infrastructure: (a) Industrial Wi-Fi Access Point delivering wireless fieldbus connectivity to mobile operator tablets; (b) Modular Fanless Edge Server terminating persistent WebSocket connections in the Purdue IDMZ.</em></figcaption>
</figure>

---

## 2. Architectural Pitfalls of HTTP Polling & Protocol Invariants

The fundamental architectural tension in web SCADA stems from attempting to force continuous physical processes into stateless client-pull paradigms ([[Villamar_et_al_2025|Villamar et al., 2025]]).

### The Inefficiencies of HTTP Short & Long Polling

When forcing continuous physical telemetry into periodic HTTP client-pull requests (e.g., issuing `GET /api/telemetry` every $100\text{ ms}$), the architecture degrades across three distinct operational layers.

First, protocol header bloat overwhelms the physical wire. Each HTTP request and response carries 500 to 1,500 bytes of repetitive metadata—including cookies, user-agents, cache directives, and authorization tokens. Transmitting a simple 4-byte IEEE 754 float measuring tank level requires moving over 1,500 bytes of raw framing data, reducing wire payload efficiency to less than 0.3%.

Second, rapid connection churn strains gateway resources. Constantly establishing, servicing, and tearing down short-lived TCP and TLS connections exhausts server ephemeral ports, inflates kernel socket tables, and consumes excessive CPU cycles in repeated handshake negotiations and thread allocation.

Finally, client-pull architectures impose an unavoidable polling dead-time gap. If an emergency pressure surge or safety interlock trip occurs immediately after a response completes, the operator display remains completely blind until the next scheduled poll fires ($100\text{–}500\text{ ms}$ later), directly violating the deterministic latency invariants required for supervisory control.

### Mathematical Wire Overhead Derivation

Consider an industrial scenario streaming an analog measurement at $N = 100\text{ samples/sec}$, where each record contains a single 4-byte IEEE 754 float payload ($P = 4\text{ bytes}$).

Under an **HTTP/1.1 short polling model**, every sample requires a distinct request-response transaction over the wire. The client transmits approximately $H_{\text{req}} \approx 850\text{ bytes}$ of headers (User-Agent, Cookie, Host, Accept), while the server replies with approximately $H_{\text{resp}} \approx 650\text{ bytes}$ of headers (Date, Content-Type, Cache-Control, Server):
$$\text{Bytes}_{\text{HTTP}} = H_{\text{req}} + H_{\text{resp}} + P = 850 + 650 + 4 = 1,504\text{ bytes/sample}$$

At a 100 Hz sampling cadence, continuous wire bandwidth totals:
$$\text{Bandwidth}_{\text{HTTP}} = 100 \times 1,504\text{ B/s} = 150,400\text{ B/s} \approx \mathbf{1.203\text{ Mbps (150.4 KB/s)}}$$
$$\eta_{\text{HTTP}} = \frac{4}{1,504} \approx \mathbf{0.26\%}$$
Over $99.7\%$ of aggregate network bandwidth is squandered on static, redundant header text.

In contrast, under the **WebSocket streaming model (RFC 6455)**, a single initial HTTP upgrade handshake establishes a persistent TCP stream. Subsequent server-to-client updates are unmasked binary frames requiring only a 2-byte header ($H_{\text{ws}} = 2\text{ bytes}$ for payloads $P \le 125\text{ bytes}$):
$$\text{Bytes}_{\text{WS}} = H_{\text{ws}} + P = 2 + 4 = 6\text{ bytes/sample}$$

For the identical 100 Hz stream, continuous wire bandwidth collapses to:
$$\text{Bandwidth}_{\text{WS}} = 100 \times 6\text{ B/s} = 600\text{ B/s} \approx \mathbf{4.8\text{ kbps (0.6 KB/s)}}$$
$$\eta_{\text{WS}} = \frac{4}{6} \approx \mathbf{66.7\%}$$

Comparing both models reveals a massive efficiency dividend:
$$\text{Bandwidth Reduction} = \left( 1 - \frac{\text{Bandwidth}_{\text{WS}}}{\text{Bandwidth}_{\text{HTTP}}} \right) \times 100\% = \left( 1 - \frac{600}{150,400} \right) \times 100\% = \mathbf{99.60\%}$$

As visualized in **Figure 12.2**, contrasting high-frequency wire traces for Reboiler Temperature Transmitter `TI-102` demonstrates this dramatic 99.6% reduction in packet churn and wire overhead. Furthermore, the trace highlights the critical $100\text{ ms}$ polling dead-time gap during which an emergency thermal excursion occurs unobserved, whereas WebSocket delivers the trip metric in $<1.2\text{ ms}$:

<figure align="center">
  <img src="../images/12-http-polling-vs-ws-streaming.svg" alt="Network Wire Traffic: HTTP/1.1 Short Polling vs. WebSocket Streaming" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure 12.2: Network Wire Traffic Comparison — High-Frequency Wire Trace for Reboiler Temperature Transmitter TI-102 (100 Hz Stream) under HTTP/1.1 Short Polling (1,504-Byte Header Tax, 100 ms Dead-Time Gap Missing Thermal Trip) vs. RFC 6455 WebSocket Streaming (2-Byte Framing, 66.7% Payload Efficiency, &lt;1.2 ms Instant Push).</em></figcaption>
</figure>

### Rejection of Server-Sent Events (SSE) in Industrial SCADA

Although Server-Sent Events (SSE) provide native server-push mechanics over standard HTTP, the protocol is systematically rejected for industrial supervisory control due to three structural deficiencies.

First, SSE is strictly unidirectional (`text/event-stream`), transporting events exclusively from server to client. Industrial SCADA, however, is fundamentally full-duplex: operators must dispatch setpoints, trigger interlocks, and issue emergency alarm acknowledgments. Adopting SSE forces control write-backs into separate out-of-band HTTP `POST` requests, bifurcating session state across distinct network channels, complicating telemetry correlation, and inflating round-trip command execution latency.

Second, the SSE specification enforces text-only framing. Transporting binary-encoded industrial protocols (such as Sparkplug B Protocol Buffers) over SSE necessitates Base64 transcoding. This immediately inflates payload wire footprint by 33% and incurs severe CPU overhead in the browser's JavaScript runtime for continuous string parsing and memory garbage collection.

Finally, HTTP/1.1 client connection pooling creates socket starvation. Web browsers enforce a hard ceiling of six concurrent TCP connections per origin domain. In multi-monitor control room environments where operators keep multiple synoptic views, alarm banners, and historical trends open across tabs, persistent SSE connections quickly exhaust the browser's socket pool, deadlocking subsequent REST API queries.

---

## 3. Decoupled Web-Native Component Architecture: RFC 6455 Framing & Conflation

The **WebSocket Protocol (RFC 6455)** upgrades a standard HTTP connection into a persistent, bidirectional, full-duplex TCP communication channel operating over standard ports (`80` / `443`), allowing seamless traversal of enterprise corporate and IDMZ firewalls ([[Guo_et_al_2022|Guo et al., 2022]]).

### Protocol Upgrade Handshake
The connection initiates as an HTTP/1.1 request containing specific upgrade headers:

```http
GET /telemetry/stream HTTP/1.1
Host: scada.meridiangrid.internal
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

The gateway validates client credentials and responds with an HTTP status `101 Switching Protocols`:
```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```
The `Sec-WebSocket-Accept` header is deterministically computed by concatenating `Sec-WebSocket-Key` with the standard RFC 6455 GUID (`258EAFA5-E914-47DA-95CA-C5AB0DC85B11`), computing the SHA-1 hash, and encoding the result in Base64. Immediately following this handshake, the underlying TCP socket bypasses HTTP parsers and enters raw WebSocket binary framing.

### RFC 6455 Frame Bit-Structure Breakdown

| Field | Bit Offset | Bit Width | Protocol Definition & Invariants |
| :--- | :--- | :--- | :--- |
| **FIN** | Bit 0 | 1 bit | `1` indicates final fragment of message; `0` indicates more fragments follow. |
| **RSV 1–3** | Bits 1–3 | 3 bits | Reserved for protocol extensions (e.g., `permessage-deflate`). Must be `0` unless negotiated. |
| **Opcode** | Bits 4–7 | 4 bits | Defines frame interpretation (`0x1` Text, `0x2` Binary Protobuf, `0x8` Close, `0x9` Ping, `0xA` Pong). |
| **MASK** | Bit 8 | 1 bit | `1` for client-to-server frames (mandates 4-byte key); `0` for server-to-client frames (unmasked). |
| **Payload Len** | Bits 9–15 | 7 bits | Base payload length: `0–125` bytes; `126` specifies 16-bit extension; `127` specifies 64-bit extension. |
| **Extended Len** | Bits 16–31 / 16–79 | 16 or 64 bits | Present only if base length is `126` (2 bytes) or `127` (8 bytes). Unsigned integer. |
| **Masking-Key** | Offset 16 / 32 / 80 | 32 bits (4 bytes) | Random XOR key (present if `MASK = 1`). Prevents cache poisoning in intermediate proxies. |
| **Payload Data** | Variable | N bytes | Application payload bytes (Sparkplug B Protobuf binary wire bytes or UTF-8 text string). |

- **Server-to-Client Frame Overhead:** Always unmasked (`MASK = 0`). For standard industrial telemetry updates ($\le 125\text{ bytes}$), framing overhead is strictly **2 bytes** (Byte 1: FIN + Opcode; Byte 2: 7-bit Payload Length).
- **Client-to-Server Frame Overhead:** Always masked (`MASK = 1`), appending the 4-byte random XOR masking key, totaling **6 bytes** overhead.

As diagrammed in **Figure 12.3**, RFC 6455 encodes this protocol efficiency into a compact 32-bit bitfield specification. Concrete hexadecimal wire dumps demonstrate that server-to-client telemetry pushes (Sparkplug B `DDATA` for Level Transmitter `LT-102`) require exactly 2 bytes of unmasked framing overhead (`0x82 0x14`), whereas client setpoint control commands (adjusting valve `FV-108`) include a 4-byte random XOR masking key totaling 6 bytes of overhead (`0x82 0x88 [4B XOR Mask]`), protecting intermediate proxy caches against cache poisoning attacks:

<figure align="center">
  <img src="../images/12-websocket-frame-layout.svg" alt="RFC 6455 WebSocket Frame Bit-Structure Breakdown" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure 12.3: RFC 6455 WebSocket Frame Bit-Structure Breakdown — 32-Bit Frame Architecture with Concrete Byte Dumps for Server Telemetry Push (Sparkplug B DDATA for LT-102, 2-Byte Overhead, Unmasked) vs. Client Setpoint Command (Valve FV-108 Adjust, 6-Byte Overhead, 4-Byte XOR Masking Key).</em></figcaption>
</figure>

### RFC 6455 Opcodes Reference
| Opcode (Hex) | Classification | Frame Type | Semantic Function in Industrial SCADA |
| :--- | :--- | :--- | :--- |
| `0x0` | Data | Continuation Frame | Streams fragmented chunks of large historical trend queries or synoptic schema downloads. |
| `0x1` | Data | Text Frame (UTF-8) | Transmits JSON payloads (configuration metadata, user settings, audit text). |
| `0x2` | Data | Binary Frame | Transmits raw byte buffers (**Sparkplug B Protocol Buffers**, compressed binary telemetry). |
| `0x8` | Control | Connection Close | Dispatches explicit socket termination status codes (e.g., `1000` Normal, `1008` Policy Violation). |
| `0x9` | Control | Ping | Out-of-band heartbeat frame sent by gateway to monitor client TCP health across firewalls. |
| `0xA` | Control | Pong | Automatic heartbeat response echoing the payload of a `Ping` frame to confirm liveness. |

### Payload Serialization: Binary Protobuf vs. Text JSON
As established in [[07-Protobuf-vs-Text-Serialization|Lesson 07]], in high-frequency SCADA streams selecting Opcode `0x2` (Binary Frame) paired with **Protocol Buffers (Protobuf)** delivers critical performance advantages over Opcode `0x1` (JSON):
- **Elimination of UTF-8 Validation:** RFC 6455 mandates that browser engines strictly validate every incoming byte of an Opcode `0x1` frame as valid UTF-8. Binary frames (`0x2`) bypass browser UTF-8 validation entirely.
- **Direct Typed Array Ingestion:** Binary payloads are mapped directly into JavaScript `ArrayBuffer` instances on the V8 heap, allowing zero-copy transfer into background **Web Workers** for off-main-thread decoding (see [[15-Multithreaded-Web-Performance|Lesson 15]]).
- **Payload Compaction:** Protobuf varint encoding and binary field tags reduce data volume by 60% to 80% compared to verbose JSON key-value pairs.

### Client Backpressure & Telemetry Conflation Engine
In industrial automation, high-speed field instruments can generate updates at 100 Hz to 1 kHz. However, browser display refresh rates are constrained to [[../Glossary#16.6 ms Frame Budget (60 FPS Execution Floor)|60 FPS (16.6 ms per frame)]] or 120 FPS, and mobile operator tablets may experience CPU throttling or transient Wi-Fi latency.

If a server transmits telemetry faster than a client browser can process and render, the browser's internal WebSocket socket buffer inflates exponentially. This unmanaged buffer bloat leads to severe UI thread freeze, catastrophic memory leaks, and stale synoptic displays.

#### Telemetry Conflation Mechanics (Server-Side Frame Coalescing)
To protect clients from buffer saturation without losing critical operational data, the SCADA WebSocket gateway implements an intelligent **Telemetry Conflation Engine** that segregates incoming plant events into two distinct processing tiers:

* **Tier 1: Continuous Analog Telemetry (Lossy Last-Value Caching).** For high-frequency continuous process variables (temperature, pressure, motor speed, flow rate), the gateway applies a Last-Value Caching (LVC) policy. Because human operators cannot visually perceive numeric changes faster than the display refresh ceiling (~30–60 Hz), intermediate analog samples can be dropped when client backpressure is detected (monitored via TCP window size or WebSocket buffer acknowledgments). For example, if five updates arrive during a single client rendering window ($v_1=24.1, v_2=24.2, v_3=24.5, v_4=24.8, v_5=25.3$), the gateway collapses the pending queue and transmits solely the latest measurement ($v_5=25.3$).

* **Tier 2: Discrete Alarms & Audit Events (Lossless FIFO Queueing).** In contrast to continuous analog metrics, safety interlocks, breaker trips, emergency stop signals, and operator control acknowledgments must never be conflated or dropped. The gateway routes all discrete state transitions into a strict FIFO queue. If an asset transitions through `RUNNING -> TRIPPED -> STOPPED`, every intermediate state is preserved in sequence to guarantee regulatory audit logging and deterministic alarm banner annunciation.

As illustrated in **Figure 12.4**, this dual-tier architecture resolves the client buffer saturation crisis. Rather than allowing unregulated 100 Hz bursts to flood browser memory buffers, the gateway conflation engine segregates high-frequency analog metrics into Tier 1 LVC hash map overwrites while queuing critical [[../Glossary#Sequence of Events (SOE)|sequence-of-events (SOE)]] alarms into lossless Tier 2 FIFO buffers, dispatching consolidated Protobuf frames at a stable 60 Hz display refresh cadence:

<figure align="center">
  <img src="../images/12-backpressure-frame-coalescing.svg" alt="Telemetry Conflation Engine &amp; Dual-Tier Backpressure Architecture" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure 12.4: Telemetry Conflation Engine &amp; Dual-Tier Backpressure Architecture — Unregulated Ingestion Buffer Overflow vs. Gateway Coalescing Segregating Continuous Analog Metrics (Tier 1 LVC Hash Map Overwrite) from Auditable SOE Discrete Events (Tier 2 Lossless FIFO Queue) Dispatched at 60 Hz Display Cadence.</em></figcaption>
</figure>

---

## 4. Enterprise Deployment Topology across Purdue & IDMZ

Deploying real-time streaming across the [[../Glossary#Purdue Enterprise Reference Architecture (PERA / Purdue Model)|Purdue Model]] requires strictly isolating client sockets behind the Level 3.5 [[../Glossary#Industrial Demilitarized Zone (IDMZ / Level 3.5)|Industrial Demilitarized Zone (IDMZ)]]. As established in [[11-Monolithic-vs-Web-SCADA|Lesson 11]], field controllers remain strictly air-gapped on private subnets, while the web tier terminates at the IDMZ reverse proxy boundary. However, maintaining persistent full-duplex TCP streaming through stateful enterprise middleboxes introduces two critical cyber-physical challenges: **Report-by-Exception state hydration** and **stateful firewall NAT connection tracking timeouts**.

### State Resynchronization & The Report-by-Exception (RBE) Dilemma
Because modern SCADA platforms operate on a **[[../Glossary#Report-by-Exception (RBE)|Report-by-Exception (RBE)]]** model (formalized in [[06-Sparkplug-B-Specification|Lesson 06]])—where field devices only publish data when an operational value changes beyond a configured deadband—a naive WebSocket reconnection creates severe operational blind spots.

Under RBE, static plant parameters (such as an emergency valve status that has remained closed for three months) never transmit updates. If a web client disconnects and simply reconnects to the live delta stream, its dashboard widgets for all static variables will remain blank, uninitialized, or frozen at pre-disconnect values until those physical values change.

### The 5-Stage Resynchronization Protocol
To guarantee deterministic, race-condition-free state recovery upon reconnection, the SCADA gateway and HMI client execute a 5-stage protocol implementing the unified data exchange subsystem pattern ([[Koltsova_et_al_2026|Koltsova et al., 2026]]):

1. **Disconnect Detection & Exponential Backoff with Jitter:** When a field tablet roams between industrial access points or encounters a transient TCP drop (`TCP RST`), the browser detects the closed socket. Rather than flooding the IDMZ gateway with immediate reconnection attempts—which would trigger a "thundering herd" saturation spike if hundreds of plant screens disconnect simultaneously—the browser delays its retry using an **exponential backoff algorithm with full jitter**:
   $$T_{\text{retry}} = \min\left(T_{\max}, \; T_{\text{base}} \times 2^{\text{attempt}}\right) \times \text{Uniform}(0.8, 1.2)$$
   This staggers re-connections across independent time windows, preventing reverse proxy CPU collapse.
2. **Authenticated HTTP Upgrade Handshake:** The browser initiates an HTTP `GET /telemetry/stream` request with `Connection: Upgrade` and `Upgrade: websocket` headers, accompanied by a fresh JWT bearer token. The IDMZ gateway terminates TLS, validates claims and role permissions against the enterprise IdP, and returns `HTTP 101 Switching Protocols`, establishing the full-duplex TCP stream.
3. **Scoped Topic Subscription Request:** Immediately upon socket establishment, the browser transmits a compact binary subscription frame (Opcode `0x2`) defining its active synoptic scope (e.g., `Enterprise/SiteA/Area1/*`). Scoping subscriptions to the operator's active screen prevents network saturation and stops unnecessary browser memory allocation for unviewed plant areas.
4. **Atomic State Snapshot Delivery (Resolving RBE Blindness):** To eliminate the RBE blind spot, the gateway queries its in-memory **Last-Value Cache (LVC)**, which continuously aggregates the latest Sparkplug B `NBIRTH` and `DBIRTH` retained metric values from the MQTT [[../Glossary#Unified Namespace (UNS)|Unified Namespace]] broker. The gateway bundles these metrics into a single atomic binary frame: `STATE_SNAPSHOT`. Upon receipt, the browser client hydrates its reactive state store (e.g., Zustand or Preact Signals) in a single atomic commit, instantly repainting all synoptic widgets with verified values and quality flags before any deltas are processed.
5. **Transition to Continuous Incremental RBE Streaming:** Once the initial snapshot is committed, the gateway transitions the socket into live streaming mode. Outgoing messages from the MQTT broker (`NDATA` and `DDATA` binary exception frames) are streamed directly to the browser, which performs [[../Glossary#Zero-Reflow Attribute Mutation|zero-reflow DOM updates]] without redrawing unmodified elements.

As visualized in the sequence diagram below, these five stages coordinate the complete lifecycle from socket termination to verified, race-condition-free live synchronization:

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'darkMode': true,
    'primaryColor': '#1E222B',
    'primaryTextColor': '#E6EDF3',
    'primaryBorderColor': '#388BFD',
    'lineColor': '#388BFD',
    'secondaryColor': '#16191F',
    'tertiaryColor': '#0D1117',
    'actorBkg': '#1E222B',
    'actorBorder': '#388BFD',
    'actorTextColor': '#E6EDF3',
    'actorLineColor': '#388BFD',
    'signalColor': '#388BFD',
    'signalTextColor': '#E6EDF3',
    'labelBoxBkgColor': '#1E222B',
    'labelBoxBorderColor': '#388BFD',
    'labelTextColor': '#E6EDF3',
    'loopTextColor': '#E6EDF3',
    'noteBorderColor': '#388BFD',
    'noteBkgColor': '#1E222B',
    'noteTextColor': '#E6EDF3',
    'activationBorderColor': '#388BFD',
    'activationBkgColor': '#1E222B',
    'sequenceNumberColor': '#FFFFFF'
  },
  'themeCSS': 'text.actor { fill: #E6EDF3 !important; } .messageText { fill: #E6EDF3 !important; } .noteText { fill: #E6EDF3 !important; } .loopText { fill: #E6EDF3 !important; } .loopText > tspan { fill: #E6EDF3 !important; }'
}}%%
sequenceDiagram
    autonumber
    actor HMI as Browser Client SPA (React / Zustand)
    participant GW as SCADA WebSocket Gateway (IDMZ Proxy)
    participant UNS as MQTT UNS Broker (Sparkplug B Hub)

    Note over HMI,GW: Transient Wi-Fi Disruption / TCP RST (Socket Closed)
    HMI->>HMI: (1) Exponential Backoff + Full Jitter Calculation
    HMI->>GW: (2) HTTP Upgrade Handshake (GET /telemetry/stream + Renewed JWT)
    GW-->>HMI: 101 Switching Protocols (Connection: Upgrade)
    HMI->>GW: (3) Session Scope Subscribe (Area / Cell Path Frame)
    GW->>UNS: Query Retained Birth State / Last-Value Cache (LVC)
    UNS-->>GW: Sparkplug NBIRTH / DBIRTH Payloads
    GW-->>HMI: (4) Binary Frame (Opcode 0x2): STATE_SNAPSHOT
    Note over HMI: Atomic Store Commit (Hydrate Zustand / Signals State)
    loop Continuous RBE Telemetry Streaming
        UNS->>GW: Sparkplug NDATA / DDATA (Exception Delta)
        GW-->>HMI: (5) Binary Frame: LIVE_DELTA (RBE)
        Note over HMI: Direct DOM Signal Update (Zero Full Re-render)
    end
```

### Stateful Firewall Keep-Alives (RFC 6455 Ping/Pong)
IDMZ firewalls (Firewall 1; see [[10-OT-Cybersecurity-IEC-62443|Lesson 10]]) and enterprise NAT routers aggressively prune idle TCP connections after 30 to 60 seconds of inactivity. In an RBE architecture where physical plant conditions are static, no application telemetry may flow for hours.

To prevent silent firewall socket termination, the SCADA gateway emits periodic RFC 6455 **Ping control frames (`Opcode 0x9`)** every 15 to 30 seconds. The browser's native networking stack automatically replies with an RFC 6455 **Pong frame (`Opcode 0xA`)** without interrupting the application thread. This guarantees continuous TCP session liveness through stateful network infrastructure.

As diagrammed in **Figure 12.5**, this heartbeat mechanism can prevent stateful firewall middleboxes from silently dropping connections. In quiescent RBE conditions without keep-alives, the Linux kernel `nf_conntrack` timer can count down to zero, evicting the NAT mapping and silently dropping subsequent emergency trip frames (`PUMP_P101A_TRIP`). A 20-second ping/pong heartbeat is an illustrative candidate; its interval and deployment require validation before being treated as an invariant:

<figure align="center">
  <img src="../images/12-firewall-keepalive-conntrack.svg" alt="Stateful Firewall NAT Connection Tracking vs. RFC 6455 Ping/Pong Keep-Alives" style="max-width: 100%; height: auto;" />
  <figcaption><em>Figure 12.5: Stateful Firewall NAT Connection Tracking (conntrack) vs. RFC 6455 Ping/Pong Keep-Alives — Silent Socket Pruning during Quiescent RBE (nf_conntrack Table Expiration &amp; Ingress Drop of PUMP_P101A_TRIP) vs. Deterministic 20s Keep-Alive Loop (2-Byte 0x89 0x00 Ping &amp; 6-Byte Auto-Pong in Browser C++ Stack).</em></figcaption>
</figure>

---

## 5. Structural Comparison: Real-Time Web Transports

| Architectural Dimension | HTTP Short Polling | HTTP Long Polling | Server-Sent Events (SSE) | WebSocket (RFC 6455) |
| :--- | :--- | :--- | :--- | :--- |
| **Underlying Protocol** | HTTP/1.1 (TCP) | HTTP/1.1 (TCP) | HTTP/1.1 or HTTP/2 | TCP Full-Duplex (RFC 6455; candidate) |
| **Communication Mode** | Half-Duplex (Client-Pull) | Simulated Push (Hanging GET) | Simplex (Server-to-Client) | **Full-Duplex (True Bi-Directional)** |
| **Framing Overhead** | $500\text{–}1,500\text{ B}$ per request | $500\text{–}1,500\text{ B}$ per message | $\sim 5\text{–}10\text{ B}$ per event | **2 Bytes (Server) / 6 Bytes (Client)** |
| **Data Encoding** | Text / JSON / Form | Text / JSON | Text (UTF-8 strings only) | **Native Binary (`ArrayBuffer`) & UTF-8** |
| **Control Commands** | Separate HTTP POST | Separate HTTP POST | Impossible (Requires HTTP POST) | **Sub-millisecond setpoints over same socket** |
| **Latency Profile** | High ($\ge$ polling interval) | Moderate (re-connection gap) | Sub-second push | **Low-latency; actual bounds require validation** |
| **Browser Concurrency** | 6 connections per origin | 6 connections per origin | 6 connections per origin (H1) | **Single multiplexed TCP socket** |
| **Backpressure Handling** | None (client controls rate) | Poor (buffer churn) | Limited (browser buffer) | **Server Conflation (LVC) + Web Workers** |
| **SCADA Suitability** | ❌ Unacceptable wire tax | ❌ High connection churn | ❌ Inadequate (no duplex / binary) | **Candidate for modern Web HMIs; not yet approved as the sole transport** |

---

## 6. Active-Recall Assessments

> [!FAQ]- Why is client-to-server WebSocket framing masked with a 4-byte random XOR key while server-to-client framing is unmasked?
> Client-to-server frames are masked to prevent malicious scripts inside a browser from executing **cache poisoning attacks** on intermediate HTTP proxies. If a browser script could send predictable byte sequences over an unmasked raw TCP connection, it could forge responses mimicking legitimate HTTP resources that intermediate caching proxies might store and serve to other clients. Random 4-byte XOR masking scrambles the byte stream on the wire, making it mathematically impossible for an attacker to predict the wire pattern. Server-to-client frames are unmasked because the server is an authenticated, trusted endpoint that cannot be coerced by untrusted browser scripts into forging proxy responses.

> [!FAQ]- Why is Server-Sent Events (SSE) rejected for bidirectional SCADA architectures despite supporting HTTP/2 multiplexing?
> SSE is strictly **simplex (unidirectional from server to client)** and restricted to UTF-8 text (`text/event-stream`). SCADA applications mandate low-latency bidirectional interaction: operators must dispatch setpoint modifications, valve controls, and emergency alarm acknowledgments over the same duplex session. Using SSE forces control actions into separate HTTP POST requests, introducing connection churn and breaking transport-level correlation. Furthermore, streaming binary payloads (such as Sparkplug B Protobuf) over SSE requires Base64 text encoding, which incurs a 33% wire size expansion and heavy CPU decoding penalties in the browser.

> [!FAQ]- How does a SCADA WebSocket gateway's backpressure conflation engine differentiate between continuous analog telemetry and discrete alarms?
> The conflation engine segregates traffic into two distinct tiers:
> 1. **Continuous Analog Telemetry (Lossy Last-Value Caching):** High-frequency process variables (temperatures, pressures, flow rates) are conflated during client buffer congestion. Intermediate samples are dropped, and only the most recent value is transmitted to match the operator screen's refresh capability (~30–60 Hz).
> 2. **Discrete Alarms & Safety Events (Lossless FIFO Queueing):** Critical plant events (breaker trips, safety interlocks, emergency stops, setpoint acknowledgments) are placed in a strictly prioritized, lossless FIFO queue where no messages are ever dropped or conflated, guaranteeing an auditable record of every state transition.

> [!FAQ]- Why is immediate live delta streaming insufficient following a client WebSocket reconnection in a Report-by-Exception (RBE) system?
> Under Report-by-Exception (RBE), edge nodes and PLCs only publish telemetry when a physical value changes. If an HMI client reconnects and immediately listens only to live deltas, any plant variable that remains unchanged (e.g., an inactive pump, a steady tank level, or an unasserted alarm) will never emit an update. The operator's synoptic screen would display blank or stale widgets for those tags indefinitely. Therefore, the gateway must deliver a consolidated **Full State Snapshot** (derived from its Last-Value Cache) to re-hydrate the client's store before resuming live RBE streaming.

> [!FAQ]- What is the operational function of RFC 6455 Opcode 0x9 (Ping) and Opcode 0xA (Pong) frames in an industrial IDMZ?
> Opcodes `0x9` (Ping) and `0xA` (Pong) are out-of-band control frames used to maintain TCP socket health across stateful IDMZ firewalls and NAT middleboxes. Stateful firewalls terminate idle TCP connections whose state tracking tables expire after short inactivity timeouts (e.g., 30–60 seconds). Because an RBE architecture may transmit no application data during quiescent plant conditions, periodic gateway Ping/Pong heartbeats keep firewall NAT states alive and detect broken client sessions without invoking application-layer message listeners.
