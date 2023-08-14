ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION} AS builder

WORKDIR /app

COPY Docker/flask/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY infrastructure/flask/app.py infrastructure/flask/app.py

CMD ["python", "infrastructure/flask/app.py"]
