from dagster import Definitions
from image_class_model_dagster.assets import (
    hackernews_stories,
    training_test_data,
    transformed_train_data,
    transformed_test_data,
    xgboost_comments_model,
    comments_model_test_set_r_squared,
    latest_story_comment_predictions
)

# Define the assets
defs = Definitions(
    assets=[
        hackernews_stories,
        training_test_data,
        transformed_train_data,
        transformed_test_data,
        xgboost_comments_model,
        comments_model_test_set_r_squared,
        latest_story_comment_predictions
    ]
)