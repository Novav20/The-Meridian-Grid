---
paper_id: "Liu_et_al_2023"
query_id: "Q01"
title: "Slow Subscribers: a novel IoT-MQTT based denial of service attack"
authors: "Liu Y.; Al-Masri E."
year: 2023
doi: "10.1007/s10586-022-03788-9"
keywords: ["Fault tolerance", "Industrial Internet of Things", "MQTT", "Publish-subscribe", "Quality of service", "SCADA"]
source_pdf: "Slow Subscribers: a novel IoT-MQTT based denial of service attack.pdf"
extraction_date: "2026-09-04"
---

### 1. Ubiquitous Language

- **Term**: Slow Subscribers
- **Definition**: A denial-of-service attack in the MQTT protocol that occurs on a single compromised node with minimal subscription permissions and overwhelms an MQTT broker with unsolicited subscription requests, causing it to become a single point of failure.
> **Evidence**: "We define Slow Subscribers, a DoS attack that overwhelms a MQTT broker device with unsolicited subscription requests." (p. 3974)

- **Term**: Remistry
- **Definition**: A Resilient Middleware for Message Queue Telemetry Transport framework that detects misconfigurations and provides granular handling of resource commitment errors, especially out-of-memory problems, to mitigate Slow Subscribers attacks.
> **Evidence**: "propose a Resilient Middleware for Message Queue Telemetry Transport (Remistry) framework that is capable of detecting misconfigurations while providing granular support of resource commitment errors, in particular the out-of-memory (OOM) problems for effectively mitigating the impact of Slow Subscribers attacks on MQTT brokers." (p. 3973)

- **Term**: Multi-processing (MP)
- **Definition**: An operating system task scheduling approach defined as the execution of isolated, concurrent code instances, distinguished from multi-threading by its adherence to the isolation principle.
> **Evidence**: "Multi-processing is an important aspect of task scheduling in operating systems, which can be defined as the execution of code in isolated, concurrent instances. It is distinguished from multi-threading by the isolation principle." (p. 3974)

### 2. Domain Rules and Invariants

- **Rule**: Slow Subscribers Traffic Amplification Rule
- **Mechanism**: Because a slow subscriber attacker only needs to transmit a single announcement packet for each subscription request, the attack results in traffic amplification, leading to network congestion and extreme memory usage on edge devices.
> **Evidence**: "Because the attacker only needs to send a single announcement for each subscription request, unlike SlowTT, this novel MQTT attack results in amplification." (p. 3977)

- **Rule**: Linux Out-of-Memory (OOM) Manager Action Rule
- **Mechanism**: Under severe memory pressure caused by the attack, the operating system's OOM manager is triggered to terminate the process that frees the largest volume of system resources.
> **Evidence**: "When the OOM manager is activated, it terminates any process that could potentially free a substantial amount of system resources." (p. 3975)

- **Rule**: Performance Score T Reduction Rule
- **Mechanism**: The execution of the Slow Subscribers attack causes severe variance and standard deviation increases in message response times, dropping the overall performance score T by 25 to 40 times compared to the baseline at 128 publishers.
> **Evidence**: "Moreover, as a result of Slow Subscribers, MQTT brokers may experience a performance score reduction that is approximately 25–40 times greater than the original baseline at 128 publishers." (p. 3982)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Copy-on-Write (COW) Worker Prototype Pattern
- **Implication**: Spawning new worker processes from a partially initialized worker prototype allows shared library memory pages to remain identical after initialization, eliminating the need to reload libraries and optimizing memory usage.
> **Evidence**: "A worker prototype is a process manager-created, partially initialized subprocess (or child). It preloads dynamic libraries in order to implement process spawning taking advantage of Linux’s copy-on-write (COW) feature, which is also referred to as implicit sharing or shadowing. Assuming the shared libraries’ memory pages remain identical after initialization, worker clones do not need to reload the libraries. This dramatically enhances Remistry’s performance and resource management." (p. 3976)

- **Constraint/Pattern**: Multi-Process Self-Recovery Architecture
- **Implication**: If individual worker clones are terminated by an OOM daemon or crash, they can be immediately recreated via fork operations from the prototype, while a prototype crash is recovered by the process manager.
> **Evidence**: "Assuming one or more of the worker sub-processes (or children) had been terminated, a self-recovery will be possible. If one of the worker clones has failed, it can be recreated by performing a fork operation at the worker prototype. If the worker prototype crashes, it can then be re-spawned from the process manager." (p. 3976)

- **Constraint/Pattern**: Bidirectional IPC Sub-process Topology
- **Implication**: The architecture is split into a control daemon, process manager, and worker processes that communicate over bidirectional channels, allowing the control daemon to detect child failures when reading closed channels.
> **Evidence**: "To this end, we designed the architecture of Remistry so that it consists of numerous sub-processes (or children) that rely on bidirectional IPC channels to function." (p. 3975)

### 4. Context Assumptions

- **Assumption**: Pair-based Inter-Process Communication (IPC) Availability
> **Evidence**: "Hence, the availability of pair-based IPC is assumed thereafter." (p. 3975)

- **Assumption**: Single Client Device Spoofing due to Lack of Granular Access Control
> **Evidence**: "Because the access control lacks granularity, Mosquitto and NanoMQ allow a single client with ‘‘subscribe access’’ to create an unbounded number of spoofed devices." (p. 3977)