---
paper_id: "Uddin_et_al_2022"
query_id: "Q03"
title: "Design and Implementation of an Open-Source SCADA System for a Community Solar-Powered Reverse Osmosis System"
authors: "Uddin S.U.; Baig M.J.A.; Iqbal M.T."
year: 2022
doi: "10.3390/s22249631"
keywords: ["Grafana", "Node-Red", "open-source", "reverse osmosis", "SCADA", "solar energy"]
source_pdf: "Design and Implementation of an Open-Source SCADA System for a Community Solar-Powered Reverse Osmosis System.pdf"
extraction_date: "2026-09-20"
stage2_status: "Excluded_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Remote Terminal Unit (RTU)
- **Definition**: A microcontroller board (Arduino Mega 2560) that interface-connects with field instrument devices and redirects collected sensor data to the main terminal unit via serial communication.
> **Evidence**: "Data is transmitted from the FIDs to the RTU, which then redirects it to the MTU via serial communication." (p. 1)

- **Term**: Main Terminal Unit (MTU)
- **Definition**: The central computing hardware running a Debian-based operating system responsible for data acquisition, visual programming logic, local time-series data storage, data analytics, and HMI dashboard rendering.
> **Evidence**: "This system relies heavily on the main terminal unit. That is responsible for data acquisition, programming, data visualization, and data storage." (p. 10)

- **Term**: Field Instrument Devices (FIDs)
- **Definition**: The physical hardware devices—comprising electrical/process sensors, relay actuators, and compressor simulators—capable of measuring physical stimuli and executing control actions on the ground.
> **Evidence**: "The field instrument devices are capable of measuring what is occurring on the ground. The values are taken from the FIDs, fed to RTU, and eventually sent to the open-source programming terminal." (p. 5)

- **Term**: Firmata Protocol
- **Definition**: A standardized communication protocol loaded onto microcontroller firmware that enables computer-based software to directly manipulate input and output pins over a serial connection.
> **Evidence**: "The RTU is programmed with the firmata protocol to make communication easier and faster. Firmata is a protocol for communicating with microcontrollers from software based on a computer." (p. 12)

### 2. Domain Rules and Invariants

- **Rule**: Isolated Signal Measurement Invariant
- **Mechanism**: Electrical DC voltage and current transducers feature galvanic isolation between input and output terminals, preventing high voltages or current spikes from reaching and damaging the RTU.
> **Evidence**: "These sensors have a very important feature of isolation from the input side to the output side, which will make sure that the RTU is not damaged in case of an overvoltage or current situation." (p. 6)

- **Rule**: Threshold-Triggered Community Alert Rule
- **Mechanism**: Process parameter changes—such as water levels violating high/low setpoints or system maintenance events—automatically trigger GSM SMS notification messages sent directly to community members.
> **Evidence**: "The important alerts sent information about the low and high water levels in clean tanks, started and stopped the system and pumps, and scheduled maintenance and restoration of the system etc." (p. 13)

- **Rule**: Local Data-Storage Security Invariant
- **Mechanism**: System operational data and historical logs are written exclusively to a local InfluxDB database instance executed on the MTU, restricting external access and preventing remote transmission over unauthorized networks.
> **Evidence**: "Thus, in order to ensure the security of the system, InfluxDB is used as the database and is executed locally on the same MTU, storing the data on the local server so that only authorized personnel will be able to access it." (p. 19)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Co-Located Multi-Stack MTU Software Architecture
- **Implication**: Node-RED, InfluxDB, and Grafana execute concurrently on a single local MTU host running Debian, uniting visual flow programming, time-series storage, and analytical dashboards without multi-server overhead.
> **Evidence**: "The Node-Red programming and dashboard tool, Grafana for data analytics, and InfluxDB for database management run on the main terminal unit having Debian operating system." (p. 1)

- **Constraint/Pattern**: Serial Firmata RTU-MTU Decoupling Pattern
- **Implication**: Low-level signal pin acquisition and relay control are offloaded to a dedicated microcontroller (RTU), freeing the MTU to focus on higher-level supervisory control, flow execution, and analytics.
> **Evidence**: "Field devices are integrated with RTUs to acquire data, which is then transmitted to the MTUs for processing and control." (p. 19)

- **Constraint/Pattern**: Complete Open-Source Technology Stack Constraint
- **Implication**: Software components are chosen strictly from open-source technologies, eliminating initial licensing costs, recurring subscription fees, and vendor lock-in.
> **Evidence**: "A major advantage of all these applications is that they are free of charge and do not require a license or an annual fee, as well as being open source with easy access to updates." (p. 19)

### 4. Context Assumptions

- **Assumption**: Manual System Restart Dependency Following Power Loss
> **Evidence**: "after a power interruption SCADA server needs to be restarted by switching on the computer and running node-Red and Grafana manually." (p. 19)

- **Assumption**: Unidirectional Outbound Community Communication Assumption
> **Evidence**: "Another system limit is that it lacks RO system user feedback. The system will send an alert, but it cannot determine whether users received that alert or not." (p. 19)
```

