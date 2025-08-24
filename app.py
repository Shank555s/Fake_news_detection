from flask import Flask, request, render_template
import joblib

# Load model & vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["news"]
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    result = "Real News!!!" if prediction == 1 else "Fake News:("
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
