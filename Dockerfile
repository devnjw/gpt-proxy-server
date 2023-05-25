FROM python:3.9

COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]
