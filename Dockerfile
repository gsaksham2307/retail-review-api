FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and model files
COPY ./app ./app
COPY ./models ./models

# Download Flan-T5 tokenizer/model ahead of time
RUN python -c "from transformers import pipeline; pipeline('summarization', model='google/flan-t5-small')"

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
