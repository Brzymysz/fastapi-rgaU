FROM python:alpine3.11

WORKDIR /app

RUN python -m venv .venv

RUN source .venv/bin/activate

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4040"]