# api.py
from fastapi import FastAPI
import requests
import pandas as pd
import bentoml
from bentoml import models

app = FastAPI()

# Load the trained models using BentoML
tfidf_model = models.get("tfidf_model:latest")  # Adjust to your saved model name
xgboost_model = models.get("XG_model:latest")  # Adjust to your saved model name

# Load the actual model objects
tfidf_vectorizer = tfidf_model.load()  # Use load() instead of get()
xgboost_model = xgboost_model.load()  # Use load() instead of get()

@app.get("/latest_comments/")
async def latest_comments():
    # Get the max ID number from Hacker News
    latest_item = requests.get(
        "https://hacker-news.firebaseio.com/v0/maxitem.json"
    ).json()

    # Get the latest 10 items based on story ids from the HackerNews items endpoint
    results = []
    scope = range(latest_item - 10, latest_item)  # Fetch latest 10 items
    for item_id in scope:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        if item and item.get("type") == "story" and item.get("title"):
            results.append(item)

    # Prepare data for predictions
    if not results:
        return {"message": "No stories found."}

    df = pd.DataFrame(results)
    inference_x = df.title

    # Transform the new story titles using the existing vectorizer
    transformed_inference_x = tfidf_vectorizer.transform(inference_x)

    # Predict the number of comments
    predictions = xgboost_model.predict(transformed_inference_x)
    df["predicted_comments"] = predictions

    return df[["title", "predicted_comments"]].to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6000)
