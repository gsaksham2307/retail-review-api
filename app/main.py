from fastapi import FastAPI, Request, Body, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import io

from app.predictor import predict_sentiment
from app.summarizer import summarize_review

app = FastAPI()

# Setup static files and Jinja2 templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# ------------------- UI Routes -------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict-ui", response_class=HTMLResponse)
async def predict_ui(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request})

@app.get("/batch-ui", response_class=HTMLResponse)
async def batch_ui(request: Request):
    return templates.TemplateResponse("batch.html", {"request": request})

# ------------------- API Routes -------------------

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(review: str = Body(..., embed=True)):
    sentiment = predict_sentiment(review)
    summary = summarize_review(review)
    return {"sentiment": sentiment, "summary": summary}

@app.post("/batch_predict")
async def batch_predict(file: UploadFile = File(...)):
    content = await file.read()

    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(io.BytesIO(content))
            texts = df["reviews.text"].dropna().tolist()
        elif file.filename.endswith(".json"):
            df = pd.read_json(io.BytesIO(content))
            texts = df["review"].dropna().tolist()
        else:
            return {"error": "Unsupported file format"}
    except Exception as e:
        return {"error": f"File parsing failed: {str(e)}"}

    results = [{"review": text, "sentiment": predict_sentiment(text)} for text in texts]
    return {"predictions": results}

