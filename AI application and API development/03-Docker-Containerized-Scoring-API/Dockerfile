FROM python:3.12-slim
WORKDIR /app
COPY main.py /app/main.py
RUN useradd --create-home appuser
USER appuser
EXPOSE 8080
CMD ["python", "main.py"]
