# Arduino Hardware Token & Deadman Switch

A security project that transforms an Arduino Uno into a physical hardware token. When plugged into your PC via USB, the system remains unlocked. The moment the Arduino is unplugged or stops responding, a background Python script instantly locks your computer.

The entire pipeline is built using **C++ (Arduino IDE)** for the hardware side and **Python** for the desktop side.

---

## 🗺️ Project Architecture

### 🛡️ Phase 1: The Hardware Beacon (C++)
Because the Arduino Uno cannot emulate a keyboard natively to send OS commands, it acts as a **security deadman switch**. 
* **Heartbeat Signal:** Continuously broadcasts a status pulse over the serial USB connection.
* **Non-Blocking Logic:** Uses `millis()` timing instead of `delay()`. This keeps the microprocessor highly responsive and prevents flooding your computer's CPU with data.
* **Interval:** Fires a heartbeat packet exactly every 1000ms (1 second).

📂 *Code location: Check the `.cpp` file (or the `.ino` file for direct Arduino IDE deployment).*

### 🐍 Phase 2: The Desktop Listener (Python)
The Python script runs continuously in the background on your PC as an active monitoring agent.
* **Serial Monitoring:** Utilizes `pyserial` to listen to the designated COM port for the Arduino's heartbeat.
* **Timeout Buffer:** Features a 3-second timeout window. Since the Arduino transmits every second, missing multiple consecutive pulses flags the device as missing or inactive.
* **OS Intercept:** Automatically executes a system command to instantly lock Windows upon signal loss.
* **Crash Protection (Extra Feature):** Built with a fail-safe mechanism—if the Python script crashes or is forcefully closed, it triggers an immediate system lock.

📂 *Code location: Check the `.py` file for the full listener source code.*

---

## 🚀 Setup & Installation

### 1. Identify the USB Port
1. Right-click the Windows Start button and select **Device Manager**.
2. Expand the **Ports (COM & LPT)** section.
3. Look for **Arduino Uno** (or your third-party driver name, e.g., `USB Serial CH340 (COM6)`). Note the COM port number.

### 2. Configure and Upload Code
1. Open the `.py` script in your editor and update the `PORT` variable to match your noted COM port:
   ```python
   PORT = 'COM6'  # Change this to your exact port
   ```
2. Open the `.ino` file in the Arduino IDE and upload it to your board.

### 3. Install Dependencies & Run
Open your command terminal and install the required library:
```bash
pip install pyserial
```
Run the listener script:
```bash
python communication.py
```

---

## 🛠️ Troubleshooting

* **`SerialException: PermissionError`**
  * **Fix:** Close the Serial Monitor inside the Arduino IDE. Only one application can access the COM port at a time.
* **The PC locks even when the Arduino is plugged in**
  * **Fix:** Double-check your COM port number in Device Manager and verify that the Arduino's on-board power LED remains lit.
* **The Python script crashes immediately on startup**
  * **Fix:** Ensure you have installed the requirements via `pip install pyserial`.

---

## ⚠️ Safety Warning
**Risk of Lockout Loop:** If the script runs automatically at startup with incorrect configurations, you could trigger a continuous system lockout loop. If this occurs, restart your computer or unplug the USB link to terminate the execution loop.
