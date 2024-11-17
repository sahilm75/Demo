print("ho")
import numpy as np
import bentoml
from bentoml.io  import NumpyNdarray
import requests
import pandas as pd

xgboost_comments_model = bentoml.sklearn.get("xg_model:latest").to_runner()
tfidf_vectorizer = bentoml.sklearn.get("tfidf_model:latest").to_runner()

svc = bentoml.Service("score_xg_model", runners=[xgboost_comments_model, tfidf_vectorizer])
print("here2")
@svc.api(input=NumpyNdarray(), output = NumpyNdarray())
def classify(no_of_news: np.ndarray) -> np.ndarray:
    print("here")
    # Get the max ID number from hacker news
    latest_item = requests.get(
        "https://hacker-news.firebaseio.com/v0/maxitem.json"
    ).json()
    # Get items based on story ids from the HackerNews items endpoint
    results = []
    scope = range(latest_item - 100, latest_item)
    for item_id in scope:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        results.append(item)

    df = pd.DataFrame(results)
    if len(df) > 0:
        df = df[df.type == "story"]
        df = df[~df.title.isna()]
    inference_x = df.title
    # Transform the new story titles using the existing vectorizer
    inference_x = tfidf_vectorizer.run(inference_x)
    result = xgboost_comments_model.run(inference_x)
    return result