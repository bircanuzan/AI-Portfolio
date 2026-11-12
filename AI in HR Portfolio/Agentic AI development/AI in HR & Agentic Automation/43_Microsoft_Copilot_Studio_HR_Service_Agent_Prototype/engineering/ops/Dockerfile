FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY engineering/ /app/
RUN python -m compileall -q src/ && python -m unittest discover -s tests
RUN python run_lab.py ingest
EXPOSE 8000
# Local-only defaults: this container is NOT suitable for public exposure without auth, TLS, security controls.
CMD ["python","run_lab.py","serve"]
