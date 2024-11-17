import bentoml

bentoml.models.export_model("xg_model:latest", "./xg_model")
bentoml.models.export_model("tfidf_model:latest", "./tfidf_model")