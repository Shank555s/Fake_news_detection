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

fake_news_full_app/
├── app.py # Flask app
├── train_model.py # Model training script
├── fake_news_dataset.csv # Combined dataset (removed from GitHub due to size)
├── fake_news_model.pkl # Trained model file
├── vectorizer.pkl # TF-IDF vectorizer file
├── templates/
│ └── index.html # Frontend for the web app
├── requirements.txt # Required Python packages
└── README.md


---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/Shank555s/fake_news_detection.git
cd fake_news_full_app
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:
   
```
Windows (PowerShell): .\venv\Scripts\Activate.ps1
Windows (CMD): .\venv\Scripts\activate.bat
Mac/Linux: source venv/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Train the model:
```
python train_model.py
```

7. Run the web app:
```
python app.py

http://127.0.0.1:5000/
```
