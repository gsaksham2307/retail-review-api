import joblib
import os
from pathlib import Path

# Load model files
BASE_DIR = Path(__file__).resolve().parent.parent / "models"
model = joblib.load(BASE_DIR / "logistic_model.pkl")
vectorizer = joblib.load(BASE_DIR / "count_vectorizer.pkl")
transformer = joblib.load(BASE_DIR / "tfidf_transformer.pkl")

def predict_sentiment(review_text: str) -> str:
    cleaned = review_text.lower()
    vec = vectorizer.transform([cleaned])
    tfidf = transformer.transform(vec)
    pred = model.predict(tfidf)[0]
    return pred
