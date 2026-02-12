# 🦷 MedTech Precision Wax Station

A specialized IoT medical device designed for dentistry and laboratory applications. This system ensures high-precision melting of dental waxes through PID-inspired thermal control and cloud-based quality assurance logging.

## 🚀 Features
- **Precision Heating:** Maintains temperature within ±0.5°C tolerance.
- **Safety Interlocks:** Automated shut-off mechanism for thermal runaway protection.
- **QA Logging:** Generates digital logs of temperature stability for medical auditing.
- **LCD Interface:** Dual-display support (Physical OLED + Cloud Dashboard).

## ⚙️ Engineering Logic
- **Hardware:** ESP32 utilizes a high-sensitivity K-Type Thermocouple or NTC Thermistor for medical-grade accuracy.
- **Software:** Python monitors the "Thermal Steady State" to ensure the wax properties are preserved during the procedure.
