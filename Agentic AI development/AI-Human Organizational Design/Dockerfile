FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m -u 10001 appuser
USER appuser
EXPOSE 8080
CMD ["uvicorn","src.hcia.service:app","--host","0.0.0.0","--port","8080"]
