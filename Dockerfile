FROM python:3.13.0-bookworm

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]