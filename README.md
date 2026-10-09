# 🔴 Sign Language Recognition

<p align="center">
  <strong>Computer Vision · Machine Learning · Python</strong>
</p>

<p align="center">
  A machine learning project for sign language recognition using Python and computer vision.
</p>

---

## 🖤 About The Project

This project explores sign language recognition using a machine learning workflow. It includes scripts for preparing a dataset, training a classifier, and testing predictions.

The project combines Python-based data processing and model training to explore how computer vision can support sign language recognition.

## ⚙️ Technologies Used

* **Python** — Core programming language
* **OpenCV** — Computer vision
* **MediaPipe** — Hand landmark detection *(if used in the implementation)*
* **Machine Learning** — Model training and classification
* **Pickle** — Model and data serialization

## 📂 Project Structure

```text
Sign-Language-Recognition/
├── SL.jpeg
├── create_dataset.py
├── data.pickle
├── model.p
├── requirements.txt
├── test_classifier.py
├── train_classifier.py
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/baraah29/Sign-Language-Recognition-.git
cd Sign-Language-Recognition-
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

```bash
python create_dataset.py
```

### 5. Train the classifier

```bash
python train_classifier.py
```

### 6. Test the classifier

```bash
python test_classifier.py
```

> **Note:** Run the scripts in the order required by their implementation. Dataset files, model paths, camera access, and other prerequisites may need to be configured first.

## 📁 Main Files

| File                  | Purpose                                |
| --------------------- | -------------------------------------- |
| `create_dataset.py`   | Dataset preparation                    |
| `train_classifier.py` | Training the classification model      |
| `test_classifier.py`  | Testing the classifier                 |
| `requirements.txt`    | Python dependencies                    |
| `data.pickle`         | Serialized dataset or processed data   |
| `model.p`             | Serialized model or model-related data |
| `SL.jpeg`             | Project image                          |

## Project Goals

* Explore computer vision techniques for sign language recognition.
* Build a workflow for dataset preparation and model training.
* Test machine learning classification.
* Investigate technology that can help improve accessibility.

##  Developer

**Bara'ah Kareem**

Junior Full-Stack Developer | React.js | ASP.NET Core

[GitHub](https://github.com/baraah29)

---

<p align="center">
  <strong>BUILDING TECHNOLOGY FOR A MORE ACCESSIBLE WORLD.</strong>
</p>
