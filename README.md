## Demo

### How to Run the Code

1. **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run Dagster or MLFlow:**
    - Navigate to the `image_class_model_dagster` directory:
      ```bash
      cd image_class_model_dagster
      ```

    - To run Dagster:
      ```bash
      dagster-webserver -p 4000 -f ./definitions.py
      ```

    - To run MLFlow:
      ```bash
      mlflow server --host 127.0.0.1 --port 10000
      ```

3. **Run BentoML:**
    - Return to the parent directory:
      ```bash
      cd ..
      ```

    - Start the BentoML service:
      ```bash
      bentoml serve service.py:svc
      ```

> **Note:** After running Dagster's code, it produces two model files, `tfidf-model.bentomodel` and `xg_model.bentomodel`. For simplicity, we have included these models directly so you do not have to wait for Dagster to run (~8 mins) and can run the BentoML service immediately.
