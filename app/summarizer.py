from transformers import pipeline

summarizer = pipeline("summarization", model="google/flan-t5-small", tokenizer="google/flan-t5-small")

def is_garbage(summary: str) -> bool:
    return (
        not summary
        or len(summary.strip()) < 10
        or summary.lower() in ["n/a", "none", "summary", "review"]
        or summary.lower().count("the") > 5
    )

def summarize_review(text: str) -> str:
    try:
        cleaned = text.strip().replace('\n', ' ').replace('\r', '')
        prompt = (
            f"Summarize the following product review in 1–2 plain English sentences, "
            f"keeping only useful opinions and removing filler or noise:\n\n{cleaned}"
        )
        result = summarizer(prompt, max_length=50, min_length=10, do_sample=False)
        summary = result[0]["summary_text"].strip()
        return summary if not is_garbage(summary) else "[Summary unavailable]"
    except Exception as e:
        return "[Summary error]"
