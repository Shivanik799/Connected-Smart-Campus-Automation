# Connected Smart Campus Automation – Raspberry Pi & IoT Project

An IoT-enabled smart campus infrastructure automation system built using **Raspberry Pi**, sensors, actuators, and cloud connectivity. This system enables **real-time monitoring and control** of campus facilities such as lighting, environmental conditions, and surveillance systems.

---

## 🚀 Project Overview

This project demonstrates the implementation of a **Connected Smart Campus** environment using embedded hardware, sensor networks, and cloud integration. The system collects environmental data, detects anomalies, and automates campus resources, contributing to **energy efficiency, security, and smart infrastructure management**.

---

## 🌐 Tech Stack & Tools Used
- **Hardware:** Raspberry Pi, DHT11 Sensor, Ultrasonic Sensor (HC-SR04), Flame Sensor, Relay Module, Webcam
- **Software:** Python, GPIO, Adafruit DHT Library, ThingSpeak Cloud API
- **Protocols:** HTTP API, Real-time Sensor Data Acquisition
- **Other Tools:** VS Code, ThingSpeak Dashboard

---

## 🎯 Key Features
- Real-time monitoring of **Temperature, Humidity, Distance, and Flame Detection**
- Automated relay-based control system for facility automation
- Cloud data logging and visualization using **ThingSpeak API**
- Live sensor data monitoring and remote alerts
- Modular and scalable system architecture for smart campus applications

---

## 🖥️ Project Architecture


---

## 🔥 Hardware Components
| Component            | Quantity |
|---------------------|:--------:|
| Raspberry Pi (3/4)   |    1     |
| DHT11 Temperature & Humidity Sensor | 1 |
| Ultrasonic Sensor (HC-SR04) | 1 |
| Flame Sensor        |    1     |
| 4-Channel Relay Module | 1 |
| Webcam (Zebronics)  |    1     |
| Connecting Wires    |   Many   |

---


---

## ⚙️ How to Run

1. Clone this repository:
   git clone https://github.com/Shivanik799/Connected-Smart-Campus-Automation-Raspberry-Pi-.git

2.Setup hardware connections as per circuit diagram.

3.Install required Python libraries:
  pip install adafruit-circuitpython-dht

4. Run the main code:
   python smart_campus_monitor.py

5. Monitor live sensor data on ThingSpeak Cloud Dashboard.
