# Retail Review Analysis API

## Overview

The **Retail Review Analysis API** is a FastAPI-based application for:

1. **Sentiment Analysis** – Classifying customer reviews as positive, negative, or neutral.
2. **Summarization** – Generating concise summaries of customer reviews.
3. **Batch Processing** – Analyzing multiple reviews uploaded via CSV.

It includes both **API endpoints** and a **web-based UI** for easy interaction.

---

## Project Structure

```
retail_review_api/
│
├── app/
│   ├── main.py                # FastAPI entry point, routes & templates
│   ├── predictor.py           # Sentiment analysis logic
│   ├── summarizer.py          # Review summarization logic
│   ├── static/                 # CSS, JS, and static files
│   └── templates/              # HTML templates (Jinja2)
│
├── archive/                    # Data archive (currently empty)
│
├── models/                     # Pre-trained model files
│   ├── count_vectorizer.pkl
│   ├── tfidf_transformer.pkl
│   ├── logistic_model.pkl
│
├── notebooks/
│   ├── 1429_1.ipynb             # Example analysis notebook
│
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker container definition
└── README.md                   # Project documentation
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/retail_review_api.git
cd retail_review_api
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

### **Run locally**

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

### **1. Health Check**

**GET** `/health`
Returns the API status.

```json
{ "status": "ok" }
```

### **2. Predict Sentiment & Summary**

**POST** `/predict`
**Request Body:**

```json
{
  "review": "The product was excellent, but delivery was late."
}
```

**Response:**

```json
{
  "sentiment": "positive",
  "summary": "Excellent product, delayed delivery."
}
```

### **3. Batch Processing**

**POST** `/batch-predict` (CSV upload)

* Upload a CSV containing customer reviews.
* Returns sentiment and summaries for each review.

---

## Web UI

The app provides a browser-based interface:

* **`/`** – Home page
* **`/predict-ui`** – Single review analysis form
* **`/batch-ui`** – Batch CSV upload form

---

## How It Works

* **Sentiment Analysis**: Uses a trained logistic regression model with TF-IDF features and `TextBlob` for polarity analysis.
* **Summarization**: Utilizes NLP transformers (`transformers` library) for abstractive or extractive summaries.
* **Batch Mode**: Reads uploaded CSV into Pandas, applies both sentiment and summarization for each review.

---

## Testing with Swagger

Once running, go to:

```
http://127.0.0.1:8000/docs
```

to test endpoints via Swagger UI.

---

## License

This project is for educational and research purposes. You may adapt and extend it for your own use.
