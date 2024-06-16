# Efficient Inventory Control Through RFID Technology

This project explores the integration of Ultra-High-Frequency (UHF) Radio Frequency Identification (RFID) technology in retail and warehousing environments to revolutionize inventory management. The system initially relies on manual handheld readers and evolves with the introduction of autonomous UHF-RFID robots.

## Table of Contents

- [Introduction](#introduction)
- [Problem Definition](#problem-definition)
- [Objective](#objective)
- [Methodology](#methodology)
- [System Design](#system-design)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Scope](#future-scope)


## Introduction

Efficient inventory management in retail shops and warehouses has long been a challenging and labor-intensive task. The adoption of UHF RFID technology offers a potential solution by enabling reader antennas to communicate with passive RFID tags via electromagnetic waves. This project introduces the UHF-RFID reader concept and outlines the development of an autonomous robot system leveraging this technology for inventory and localization tasks.

## Problem Definition

The existing inventory management systems are fraught with inefficiencies and security vulnerabilities due to their reliance on manual operations. This labor-intensive process demands significant human resources, is prone to errors, and lacks real-time information, which affects decision-making and productivity. 

## Objective

The primary objective is to design and develop an RFID-enabled robotic system with extended-range detection capability to efficiently identify and interact with RFID tags at considerable distances.

## Methodology

### Phase I: RFID Reader Integration
1. **Testing RFID Reader:** Initial testing of the RFID reader for functionality.
2. **Integration with Raspberry Pi 4:** Connecting the RFID reader to Raspberry Pi 4 using UART protocol.
3. **Data Transmission:** Transmitting tag information to Google Sheets via HTTP webhooks.

### Phase II: Design and Development of Line Following Robot
1. **Component Selection:** Selecting appropriate motors, batteries, and other components.
2. **Robot Fabrication:** Assembling the chassis and integrating selected components.
3. **Control Systems Integration:** Integrating RFID reader, Raspberry Pi, and display for GUI.

### Phase III: Calibration and Testing
1. **Calibration:** Ensuring accurate path tracking and smooth movement of the line-following robot.
2. **Simultaneous RFID Tag Detection:** Continuous detection of tags during robot movement and real-time data transmission to Google Sheets.

## System Design

The system includes the following components:
- **Raspberry Pi 4:** Controls the RFID reader, camera module, and display.
- **Arduino Nano:** Controls the IR sensor and motor.
- **12V Battery:** Supplies voltage to the RFID reader and motor driver.
- **Buck-Boost Converter:** Steps down 12V to 5V for Raspberry Pi and Arduino Nano.

The block diagram below represents the complete working of the project:

![Block Diagram](https://github.com/Dhanush-b/Efficient-Inventory-Control-Through-RFID-Technology/assets/83268895/ee8b3b75-04ce-4b61-93ae-e9a562f95667)


## Results

The autonomous robot successfully navigates indoor spaces, conducts inventory checks, and transmits data to Google Spreadsheets. The GUI on the 5-inch LCD display facilitates user control and monitoring.

## Conclusion

The implementation of UHF-RFID technology through autonomous robots has streamlined inventory processes, reduced errors, and enhanced productivity in retail and warehousing operations.

## Future Scope

Future enhancements could include:
- Advanced navigation algorithms for more complex environments.
- Integration with other IoT devices for broader smart inventory management solutions.
- Enhanced security features for better theft prevention.


