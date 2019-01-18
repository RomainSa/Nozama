FROM python:3.6.7-stretch

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python app.py
