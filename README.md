# 🔴 Sign Language Recognition

<p align="center">
  <strong>REAL-TIME HAND TRACKING & LETTER CLASSIFICATION</strong>
</p>

<p align="center">
  A computer vision application that recognizes hand gestures and predicts letters of the English alphabet using MediaPipe and a Random Forest classifier.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
</p>

---

## 01. Overview

This project demonstrates real-time hand landmark detection and letter classification using computer vision and machine learning.

The application captures frames from a webcam, detects hand landmarks using MediaPipe, and uses a trained Random Forest classifier to predict a corresponding letter from A to Z.

A Flask web application streams the processed video and provides the latest prediction through a JSON endpoint.

## 02. Features

* Real-time webcam video streaming.
* Hand landmark detection and visualization.
* Hand bounding box and predicted-letter overlay.
* Random Forest classification using hand landmark coordinates.
* Prediction updates approximately once per second.
* Flask endpoints for video streaming and retrieving predictions.

## 03. Tech Stack

| Technology   | Role                                |
| ------------ | ----------------------------------- |
| Python       | Application logic                   |
| OpenCV       | Image processing and webcam capture |
| MediaPipe    | Hand landmark detection             |
| NumPy        | Numerical data processing           |
| Scikit-learn | Machine learning classification     |
| Flask        | Web application and HTTP endpoints  |
| Pickle       | Loading the trained model           |

## 04. Project Structure

```text
Sign-Language-Recognition-/
├── App.py
├── recognition.py
├── create_dataset.py
├── train_classifier.py
├── test_classifier.py
├── requirements.txt
├── model.p
├── data.pickle
├── SL.jpeg
├── templates/
│   └── index.html
└── README.md
```

The structure above represents the expected application files. Ensure `templates/index.html` exists in the repository.

## 05. Installation & Setup

### Prerequisites

* Python installed on your machine.
* A working webcam.
* The trained model file `model.p`.

### Step 1 — Clone the repository

```bash
git clone https://github.com/baraah29/Sign-Language-Recognition-.git
cd Sign-Language-Recognition-
```

### Step 2 — Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the application

```bash
python App.py
```

Open your browser and navigate to:

`http://127.0.0.1:5000`

Allow webcam access if your browser requests it.

## 06. Application Endpoints

| Endpoint          | Description                                 |
| ----------------- | ------------------------------------------- |
| `/`               | Serves the web interface                    |
| `/video_feed`     | Streams processed webcam frames using MJPEG |
| `/get_prediction` | Returns the latest predicted letter as JSON |

## 07. How It Works

1. **Capture:** OpenCV reads frames from the webcam.
2. **Detection:** MediaPipe detects hand landmarks.
3. **Feature Extraction:** The application collects the normalized X and Y coordinates of the hand landmarks.
4. **Classification:** The trained Random Forest model predicts a class.
5. **Visualization:** OpenCV draws the landmarks, bounding box, and predicted letter.
6. **Web Streaming:** Flask delivers the processed frames and prediction data to the frontend.

## 08. Supported Labels

The classifier maps its output classes to the English letters **A–Z**.

Recognition performance depends on the training dataset, lighting, camera position, and hand gestures.

## 09. Developer

**Bara'ah Kareem**

Junior Full-Stack Developer | React.js | ASP.NET Core

* GitHub: [@baraah29](https://github.com/baraah29)
* LinkedIn: [baraah-kareem](https://linkedin.com/in/baraah-kareem)
* Email: [baraah.kareem@gmail.com](mailto:baraah.kareem@gmail.com)

---

<p align="center">
  <strong>BUILDING TECHNOLOGY FOR A MORE ACCESSIBLE WORLD.</strong>
</p>
