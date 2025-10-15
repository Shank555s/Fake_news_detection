# Fake News Detection Project

A machine learning project that detects whether a piece of news is **real** or **fake** using Natural Language Processing (NLP) and Logistic Regression.

---

## 🔹 Features

- Trains a **Logistic Regression model** on the ISOT Fake News Dataset.
- Uses **TF-IDF vectorization** for text preprocessing.
- Provides a **Flask web application** for user-friendly predictions.
- Model and preprocessing pipeline are saved for future use (`.pkl` files).

---

## 🗂️ Project Structure


---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/Shank555s/fake_news_detection.git
1.cd fake_news_full_app
//Activate python environment
2.python -m venv venv
.\venv\Scripts\Activate.ps1
//Download the requirements
3.pip install -r requirements.txt
//Training the model
4.python train_model.py
//Running the web app
5.python app.py
http://127.0.0.1:5000/
