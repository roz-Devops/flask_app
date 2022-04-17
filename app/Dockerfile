# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /flask_app

COPY ./app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app .

ENV FLASK_APP=server.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=3000" ]


#docker build --tag flask_app .
