FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY project .

ENTRYPOINT ["pytest"]