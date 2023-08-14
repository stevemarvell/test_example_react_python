ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION} AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# uvicorn infrastructure.rest.api:app --host 0.0.0.0 --reload

CMD ["uvicorn", "infrastructure.rest.api:app", "--host", "0.0.0.0", "--reload"]
