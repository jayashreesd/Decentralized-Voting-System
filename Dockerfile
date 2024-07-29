FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts /app/scripts

ENTRYPOINT ["python", "scripts/cast_votes.py"]
