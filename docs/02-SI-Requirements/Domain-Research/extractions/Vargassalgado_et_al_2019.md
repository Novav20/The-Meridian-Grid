---
paper_id: "Vargassalgado_et_al_2019"
query_id: "Q03"
title: "Low-cost web-based Supervisory Control and Data Acquisition system for a microgrid testbed: A case study in design and implementation for academic and research applications"
authors: "Vargas-Salgado C.; Aguila-Leon J.; Chiñas-Palacios C.; Hurtado-Perez E."
year: 2019
doi: "10.1016/j.heliyon.2019.e02474"
keywords: ["Arduino", "Cloud computing", "Control system design", "Data analysis", "Data analytics", "Data visualization", "Electrical engineering", "Electrical system", "Energy", "Hybrid renewable energy system", "Power control system", "Raspberry", "Remote control and wireless monitoring", "Renewable energy resources", "Web-based SCADA"]
source_pdf: "Low-cost web-based Supervisory Control and Data Acquisition system for a microgrid testbed: A case study in design and implementation for academic and research applications.pdf"
extraction_date: "2026-09-20"
stage2_status: "Excluded_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Arduino Wireless Power Meter (AWPM)
- **Definition**: An Arduino-based measurement unit designed to sample electrical parameters such as voltage, current, power factor, active, reactive, and apparent power from microgrid energy sources.
> **Evidence**: "To collect weather data and measure the electrical parameters of the microgrid, detailed at Tables 3 and 4, an Arduino wireless power meter (AWPM) is designed and built." (p. 3)

- **Term**: Arduino Wireless Switch Controller (AWSC)
- **Definition**: An embedded hardware component consisting of an Arduino Mega, an NRF24L01 radiofrequency transceiver, and a relay module that connects or disconnects renewable energy sources according to control commands.
> **Evidence**: "The operation of the microgrid requires connecting and disconnecting the different renewable sources according to the preprogrammed load and the amount of energy coming from those sources. The Arduino wireless switch controller (AWSC) accomplishes this task." (p. 4)

- **Term**: Arduino-Raspberry Pi 3 Wireless Base Station (ARWBS)
- **Definition**: A central master station combining a Raspberry Pi board and an Arduino interface connected via I2C serial protocol to log data locally and remotely while routing commands to microgrid devices.
> **Evidence**: "ARWBS is based on the integration of an Arduino board and a Raspberry Pi, allowing the system to log data and store it into a local DB, as well as in a cloud DB. The communications of the Arduino and Raspberry Pi 3 use the I2C serial protocol. With this structure, the Arduino is acting as an interface between the Raspberry Pi and all the other Arduino-based data collectors." (p. 4)

- **Term**: Arduino Wireless Meteorological Data Collector (AWMDC)
- **Definition**: An Arduino development board integrated with sensors and an NRF24L01 transceiver responsible for compiling wind speed, solar radiation, environmental temperature, and relative humidity.
> **Evidence**: "Fig. 7b displays the Arduino board responsible for the meteorological data collector (AWMDC) that compiles wind speed, solar radiation, environmental temperature and humidity with a DHT22 sensor." (p. 4)

### 2. Domain Rules and Invariants

- **Rule**: ADC Intermediate-Range Zero-Crossing Frequency Detection Rule
- **Mechanism**: Grid frequency is derived by identifying AC waveform zero-crossings whenever 10-bit ADC readings fall within the intermediate value range between 512 and 520.
> **Evidence**: "Given the 10-bit resolution range of the analog to digital converter (ADC), if a value is between 512 and 520 (intermediate range of the 210 = 1024 possible values) means that the signal has crossed the zero reference of the AC voltage." (p. 4)

- **Rule**: Dual-Database Redundant Data Logging Invariant
- **Mechanism**: Measurement data is transmitted continuously to a cloud-hosted MySQL database while simultaneously logged to a local database backup on the Raspberry Pi to prevent data loss during wireless or internet connectivity failures.
> **Evidence**: "Cloud DB reads and writes data, updating continuously at specific sample rates, for each variable following the data refresh and operation commands sent by the ARWBS to each microgrid device. Besides, a local DB records the information as a backup for preventing data losses due to wireless communication or internet connection failures." (p. 5)

- **Rule**: Calibration Coefficient Precision Rule
- **Mechanism**: Raw voltage and current readings from non-intrusive current transformers and voltage transformers are scaled using calibration coefficients adjusted against a commercial power meter to maintain measurement precision within 5% on average.
> **Evidence**: "Calibration of the current and voltage measurements is an essential issue for the AWPM implementation; this task is carried out by adjusting calibration coefficients included in the code. These coefficients are deduced by the calibration of the AWPM with a commercial Sentron PAC3200 Power Meter up to reach a precision of +-5% on average." (p. 4)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Master-Slave Hybrid Hardware-Software Top-Level Topology
- **Implication**: Arduino-based slave devices handle low-level sensor sampling, electrical parameter calculation, and wireless RF transmission, offloading master coordination, local/cloud DB persistence, and web hosting to a Raspberry Pi base station.
> **Evidence**: "A master device on a Raspberry-PI board was set up to send all this information to a local database (DB), and a MySQL Web-DB linked to a Web SCADA interface, programmed in HTML5." (p. 1)

- **Constraint/Pattern**: Decoupled NRF24L01 Wireless RF Fieldbus Communication Pattern
- **Implication**: Distributed measurement nodes communicate with the central base station via 2.4 GHz NRF24L01 radio frequency modules over the SPI synchronous protocol, eliminating physical fieldbus cabling between microgrid assets.
> **Evidence**: "An integrated Arduino-based base station broadcasted these data via wireless, using the radio frequency transceiver module NRF24L01 through the SPI (Serial Peripheral Interface) synchronous protocol." (p. 3)

- **Constraint/Pattern**: Two-Port Separation of Web Interface and Cloud Database Communication
- **Implication**: Client web browser GUI interactions communicate with the web server via encrypted HTTPS on port 443, whereas the base station executes PHP-driven data queries directly against the cloud MySQL database over port 3306 via TCP/IP.
> **Evidence**: "the user operates the microgrid through an own-developed Web SCADA interface that makes PHP queries to the PLESK server via port 443 and to the cloud DB using port 3306 through the ARWBS using TCP/IP." (p. 5)

### 4. Context Assumptions

- **Assumption**: Memory Capacity Threshold Constraints for High-Frequency Cloud Logging
> **Evidence**: "As time progresses, more data will be recorded, increasing the size of the table and, therefore, the space memory could reach the maximum storage permitted by a Plesk regular account (6 GB)." (p. 5)

- **Assumption**: Higher AC Bus Frequency Instability under Off-Grid / Stand-Alone Operation Mode
> **Evidence**: "It is also noticeable how the microgrid has a better bus frequency performance when it is working in the grid-tied mode because when the microgrid operates in the off-grid mode, the frequency depends on the backup generator or the gasification plant, in which it is more complicated to have a stable frequency." (p. 8)
```

