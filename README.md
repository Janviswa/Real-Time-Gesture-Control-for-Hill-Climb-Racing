# 🚗 Gesture Control for Hill Climb Racing

This repository contains code and documentation for controlling the game *Hill Climb Racing* using real-time hand gesture recognition. Using Python, OpenCV, and MediaPipe, the system translates user gestures captured via webcam into in-game actions such as acceleration, braking, and nitro boost.

---

## 🎥 Demo: Gesture Controlled Gameplay

Watch the demo of the gesture-based control in action:

[![Gesture Control Demo](https://img.youtube.com/vi/ql5nlbrLgQU/0.jpg)](https://youtu.be/ql5nlbrLgQU)


---

## ✨ Features

* **Real-Time Gesture Detection:** Seamless hand gesture recognition using webcam and MediaPipe.
* **Game Control Integration:** Map gestures to in-game key presses (accelerate, brake, nitro).
* **OpenCV Visualization:** Display live webcam feed with gesture detection overlays.
* **Lightweight Setup:** No external hardware or controllers required.

---

## 📚 Table of Contents

* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Gesture Mapping](#gesture-mapping)
* [Project Structure](#project-structure)
* [Topics](#topics)
* [Contributing](#contributing)
* [Contact Information](#contact-information)

---

## 🚀 Getting Started

Follow the steps below to set up and run the gesture control system for *Hill Climb Racing*.

---

## 📦 Prerequisites

* Python 3.8+
* Webcam

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/gesture-hillclimb.git
cd gesture-hillclimb
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🕹️ Usage

1. Launch the script:

```bash
python main.py
```

2. Start *Hill Climb Racing* and control it using gestures.

---

## ✋ Gesture Mapping

| Gesture     | Action     |
| ----------- | ---------- |
| ✋ Open Hand | Accelerate |
| ✊ Fist      | Brake      |
| ☝️ 1 Finger | Nitro      |

---

## 📂 Project Structure

```
├── main.py             # Main gesture detection and control script
├── directkeys.py       # Simulated key press logic using ctypes
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## 📌 Topics

`python` `opencv` `mediapipe` `computer-vision` `gesture-control` `game-automation` `hill-climb-racing` `real-time-detection` `hand-tracking`

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request

---

## 📬 Contact Information

📧 Email: [jananiviswa05@gmail.com](mailto:jananiviswa05@gmail.com)
🔗 LinkedIn: [Janani V](https://www.linkedin.com/in/jananiv05)

