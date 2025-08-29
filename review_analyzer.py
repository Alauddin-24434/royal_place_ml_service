import re
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def preprocess_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = text.replace("awsome", "awesome").replace("resot", "resort")
    return text

def sentiment_analyzer_function(text: str, threshold: float = 0.6):
    clean_text = preprocess_text(text)
    result = sentiment_analyzer(clean_text)[0]
    label = result["label"]
    score = result["score"]
    if score < threshold:
        label = "NEUTRAL"
    return {"feature": "sentiment", "label": label, "score": score}
