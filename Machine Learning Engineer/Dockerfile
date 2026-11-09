FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY tests ./tests
RUN python -m unittest discover -s tests -v
CMD ["python", "-m", "src.ml_eval_lab", "--rows", "3000", "--seed", "42", "--output-dir", "/app/artifacts"]
