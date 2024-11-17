import bentoml
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


xgboost_comments_model = bentoml.sklearn.get("xg_model:latest").to_runner()
xgboost_comments_model.init_local()

tfidf_vectorizer = bentoml.sklearn.get("tfidf_model:latest").to_runner()
tfidf_vectorizer.init_local()

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
print(xgboost_comments_model.run(inference_x))




# @asset
# def comments_model_test_set_r_squared(transformed_test_data, xgboost_comments_model):
#     transformed_X_test, transformed_y_test = transformed_test_data
#     # Use the test set data to get a score of the XGBoost model
#     print("transformed_X_test:",transformed_X_test)
#     print("transformed_X_test",transformed_y_test)
#     score = xgboost_comments_model.score(transformed_X_test, transformed_y_test)
#   #  print('score:',score)
#     return score


# Evaluating
# @asset
# def latest_story_comment_predictions(xgboost_comments_model, tfidf_vectorizer):
#     # Get the max ID number from hacker news
#     latest_item = requests.get(
#         "https://hacker-news.firebaseio.com/v0/maxitem.json"
#     ).json()
#     # Get items based on story ids from the HackerNews items endpoint
#     results = []
#     scope = range(latest_item - 100, latest_item)
#     for item_id in scope:
#         item = requests.get(
#             f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
#         ).json()
#         results.append(item)

#     df = pd.DataFrame(results)
#     if len(df) > 0:
#         df = df[df.type == "story"]
#         df = df[~df.title.isna()]
#     inference_x = df.title
#     # Transform the new story titles using the existing vectorizer
    
#     inference_x = tfidf_vectorizer.transform(inference_x)
#     return xgboost_comments_model.predict(inference_x)