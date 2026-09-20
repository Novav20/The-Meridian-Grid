---
paper_id: "Jiao_et_al_2018"
query_id: "Q03"
title: "Real-time visualization of geo-sensor data based on the protocol-coupling symbol construction method"
authors: "Jiao D.; Sun J."
year: 2018
doi: "10.3390/ijgi7120460"
keywords: ["Geo-sensor", "Internet of Things", "Map symbol", "Protocol parsing", "Real-time visualization"]
source_pdf: "Real-time visualization of geo-sensor data based on the protocol-coupling symbol construction method.pdf"
extraction_date: "2026-09-20"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Protocol-Coupling Map Symbol
- **Definition**: A map symbol model integrating vector graphic data, metadata of sensor data, and a mapping profile to enable a single symbol to visually express multiple internal states of a remote geo-device.
> **Evidence**: "The protocol-coupling map symbol model includes three parts: graphic data, metadata of the sensor data, and the mapping profile (Figure 2)." (p. 6)

- **Term**: Geo-Sensor Message Broker
- **Definition**: A server-side communication middleware providing data acquisition and transfer services to bridge remote geo-sensors and map clients for real-time data visualization.
> **Evidence**: "To ensure that sensor data can be transferred from the device to the map client in real time, it was necessary to establish a geo-sensor message broker for real-time sensor data communication on the server side, where the broker can act as a bridge between the map client and remote geo-sensors." (p. 8)

- **Term**: IMetaData Interface
- **Definition**: An object-oriented interface declared in the symbol system that extracts metadata information—such as sensor data item names and types—from protocol driver classes during symbol construction.
> **Evidence**: "The metadata interface obtains the name and type of the item in the geo-sensor data which are used to the construct the map symbol." (p. 5)

- **Term**: IDataParser Interface
- **Definition**: An object-oriented interface executing on the server side that deserializes incoming raw geo-sensor data frames into lightweight JSON format for real-time processing and visualization.
> **Evidence**: "In the class that implements the data-parsing interface, the data stream is transformed from a private format into a public format. JavaScript Object Notation (JSON) is a lightweight text data exchange format independent of programming languages that is often used for data transmission in the IoT. Thus, JSON is suitable for describing the sensor data after geo-sensor data stream parsing." (p. 5)

- **Term**: Spatial-Communication Protocol
- **Definition**: A full-duplex JSON-based communication protocol operating over Socket or WebSocket that synchronizes map clients and the message broker through bounding box updates and filtered sensor data pushes.
> **Evidence**: "In order to ensure the synchronization between the map client and the service, the spatial-communication protocol was defined. This protocol defines a full duplex communication: the map client sends boundbox messages to the geo-sensor data transfer service, then the service updates the corresponding spatial filter and responds back." (p. 9)

### 2. Domain Rules and Invariants

- **Rule**: Production Rule-Based Visual Mapping Rule
- **Mechanism**: Sensor data value intervals are bound to graphic element visual variables (such as fill color, shape, or visibility) through logical IF-THEN conditions; evaluating these rules at runtime dynamically updates the symbol's appearance.
> **Evidence**: "The relationship between geo-sensor data and visual variable is antecedent-consequent, so this research examined methods for expressing the mapping as a succinct collection of production rules in the form IF conditions THEN outcomes." (p. 5)

- **Rule**: Bounding-Box Spatial Filter Push Rule
- **Mechanism**: The data transfer service maintains a dedicated spatial filter per client session; when sensor values change, data is pushed exclusively to clients whose current map view bounding box (BBox) contains the sensor's geographic location.
> **Evidence**: "When the client map view changes, the map client upload the spatial information (BBox, srs) to the server with FunctionCode 1. The geo-sensor data transfer service receives the information and updates the spatial filter instance for the current map view... If the sensor data with spatial information meets the filter condition in the spatial filter instance and geo-sensor data item has changed compared to the previous, the filter instance will send a copy of the data to corresponding map client with FunctionCode 2." (p. 9)

- **Rule**: Global Unique Identifier Disambiguation Rule
- **Mechanism**: In SVG-rendered maps, every graphical shape within a sensor's `<g>` group element receives a unique ID combining the sensor ID and graphic element ID, enabling client scripts to manipulate specific DOM elements without cross-sensor collision.
> **Evidence**: "In order to distinguish the graphic elements of each sensor on the SVG map so that the system could change the visual effect of the SVG according to the mapping profile, each SVG shape in <g> element was identified by its global unique ID, which is a combination of sensor ID and graphic element ID in the symbol." (p. 12)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Decoupled Driver-Interface Symbol Construction Pattern
- **Implication**: Symbol builders and protocol designers operate independently because transmission protocols are abstracted behind IMetaData and IDataParser interfaces, allowing private and open protocols to be registered via DriverRegister without altering core symbol software.
> **Evidence**: "Based on the protocol parsing interface, the map symbol builders and the communication protocols designers are independent. Any protocol parsing class that implements the parsing interface can be integrated into the map symbol construction process, where both the private format protocol and the open format protocol can be integrated into the symbol building process." (p. 14)

- **Constraint/Pattern**: Dual-Service Broker Architecture
- **Implication**: Server-side real-time data handling is divided into an acquisition service (connecting via long-polling, parsing via IDataParser, and writing to a JSON pool) and a transfer service (managing per-session spatial filters and WebSocket pipelines).
> **Evidence**: "The geo-sensor message broker includes two services: the geo-sensor data acquisition service and the transfer service." (p. 8)

- **Constraint/Pattern**: Client-Side SVG-DOM Dynamic Manipulation Pattern
- **Implication**: In browser-server GIS, the WMS server embeds the mapping profile as a JavaScript block within a generated SVG document; the client browser receives real-time JSON pushes over WebSocket and updates the SVG DOM elements directly without re-fetching map images.
> **Evidence**: "Differ nt with the way of map symbol rendering in Client-Server architecture, the map server converts spatial data and map symbol data into one SVG document according to the map request parameters via SensorLayer, and the mapping profile in the symbol is converted into JavaScript block that exists in the script area of the SVG document." (p. 12)

### 4. Context Assumptions

- **Assumption**: Discrete Periodic Geo-Sensor Data Transmission
> **Evidence**: "The data collected by the geo-sensor were periodic, so the sensor data in the system are presented as discrete data." (p. 4)

- **Assumption**: Inefficiency of Periodic Full-Map Refresh Methods
> **Evidence**: "Periodically refreshing the map using the UniqueValueRenderer method enables visualizing changing sensor data; however, a frequent refresh rate increases the burden on the system. In addition, an infrequent refresh rate means some changes in the sensor data are ignored. Therefore, refreshing the map periodically is not suitable for real-time visualization." (p. 2)

- **Assumption**: Unsuitability of Raster Bitmap Formats for Real-Time Vector Rendering
> **Evidence**: "Bitmap images, for example, do not change well. Therefore, bitmap format maps are not suitable for real-time sensor data visualization." (p. 11)
```

