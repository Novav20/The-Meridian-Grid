---
paper_id: "Narayanan_et_al_2026"
query_id: "Q01"
title: "Encryption for Industrial Control Systems: A Survey of Application-Level and Network-Level Approaches in Smart Grids"
authors: "Narayanan M.; Hafeez M.A.; Munir A."
year: 2026
doi: "10.3390/jcp6010011"
keywords: ["DNP3", "encryption", "IEC 61850", "IEC 62351", "Industrial Control Systems (ICS)", "IPsec", "MACsec", "smart grid", "TLS", "Virtual Private Networks (VPN)"]
source_pdf: "Encryption for Industrial Control Systems: A Survey of Application-Level and Network-Level Approaches in Smart Grids.pdf"
extraction_date: "2026-09-04"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Media Access Control Security (MACsec)
- **Definition**: A Layer 2 data link layer protocol that encrypts Ethernet frames and protects against tampering and replay on local area networks without altering higher-layer protocols.
> **Evidence**: "In contrast, MACsec operates on Layer 2 (data link layer), securing Ethernet frames on local area networks. It encrypts traffic and protects against tampering and replay without altering higher-layer protocols, using IEEE 802.1AE with key agreement via 802.1X MKA." (p. 7)

- **Term**: DNP3 Secure Authentication (SA)
- **Definition**: A standard-based security overlay for the Distributed Network Protocol version 3 that adds a challenge–response mechanism for origin authentication and message integrity using symmetric or public keys, but does not encrypt telemetry data.
> **Evidence**: "SA adds a challenge–response mechanism that provides origin authentication and message integrity for selected operations using symmetric keys (e.g., HMAC) and, in later profiles, optional public-key credentials for entity authentication." (p. 10)

- **Term**: Application-Level Encryption
- **Definition**: Cybersecurity protections integrated directly into specific industrial control protocols, terminating at the communicating endpoints and configured per individual application.
> **Evidence**: "Application-level encryption, in this survey, refers to security mechanisms that are integrated directly into the specific ICS communication protocols. This is a functional definition: the underlying primitive may reside at the application or transport layer in the OSI/TCP/IP stack." (p. 8)

### 2. Domain Rules and Invariants

- **Rule**: Payload plaintext exposure under DNP3-SA
- **Mechanism**: Because DNP3 Secure Authentication only authenticates command origins and validates integrity without encrypting telemetry or control payloads, transport security overlays (such as TLS or IPsec) are required to achieve payload confidentiality.
> **Evidence**: "SA mitigates spoofing and replay through counters and freshness checks; it does not encrypt telemetry or control payloads. Because payloads remain in plaintext, SA should be combined with transport protection (e.g., TLS or IPsec) when confidentiality is required." (p. 10)

- **Rule**: Low-latency optimization partition for IEC 61850 profiles
- **Mechanism**: Time-sensitive multicast signaling (GOOSE/SV) is constrained to Layer 2 MACsec or IEC 62351-6 to meet tight substation latency budgets, whereas client-server MMS messages use transport-layer TLS.
> **Evidence**: "MMS over TCP/IP is commonly protected with TLS (per IEC 62351-3). GOOSE and Sampled Values operate at Layer 2; their protection is specified in IEC 62351-6 (message authentication and integrity), and many deployments use MACsec to secure the underlying Ethernet segments." (p. 11)

- **Rule**: Computational latency inflation on embedded Modbus/TCP TLS
- **Mechanism**: Forcing TLS encryption on resource-constrained embedded controllers increases the average per-request transaction latency from approximately 1 ms to 1.6–1.8 ms.
> **Evidence**: "Recent measurements of Sun-Spec Modbus/TCP over TLS on embedded controllers report that enforcing TLS increases average per-request latency from around 1 ms to approximately 1.6–1.8 ms, depending on the cipher suite." (p. 9)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Micro-segmentation on Substation Local Area Networks
- **Implication**: Isolating critical protection and control Intelligent Electronic Devices (IEDs) from maintenance/monitoring devices prevents lateral compromise and ensures a localized breach does not disable primary grid protection elements.
> **Evidence**: "Micro-segmentation is applied within a substation to isolate protection and control IEDs from maintenance or monitoring devices, ensuring that a compromised device in one part of the network cannot impact critical protection functions." (p. 7)

- **Constraint/Pattern**: DMZ Separation and Network Segmentation
- **Implication**: Splitting industrial control networks from administrative IT zones isolates operational technology systems, restricting communication paths to explicitly authorized interfaces.
> **Evidence**: "These zones, such as the control center, substation LANs, and field area networks, have restricted access and clear boundaries, often using Demilitarized Zones (DMZs) to isolate OT from corporate IT systems." (p. 7)

- **Constraint/Pattern**: Protocol-Agnostic Network-Layer Encryption Retrofit
- **Implication**: Deploying broad-scope VPNs, IPsec, or MACsec tunnels at gateways and switches secures legacy, heterogeneous systems without requiring software re-engineering or firmware modifications at the constrained endpoints.
> **Evidence**: "These solutions are often easier to deploy across heterogeneous systems because they do not require modification of application code or devices. It provides a significant advantage, as retrofitting security into legacy ICS environments is much easier." (p. 16)

### 4. Context Assumptions

- **Assumption**: Omnipresent active and passive network-level threat actor
- **Evidence**: "In the remainder of this survey, we assume an attacker who can passively eavesdrop on, and actively inject or modify traffic on untrusted or shared networks that interconnect control centers, substations, AMI head-ends, DER sites, and external users." (p. 5)

- **Assumption**: Extended longevity and operational lifecycles of deployed hardware assets
- **Evidence**: "Given the long life cycles of ICS equipment, systems deployed today may still be in operation when quantum computers become practical." (p. 17)

