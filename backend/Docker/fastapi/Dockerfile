ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION} AS builder

WORKDIR /app

COPY Docker/fastapi/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# uvicorn infrastructure.fastapi.api:app --host 0.0.0.0 --reload

CMD ["uvicorn", "infrastructure.fastapi.app:app", "--host", "0.0.0.0", "--reload"]
