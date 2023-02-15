# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /movies-website
COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN apt update
RUN apt install -y gdal-bin

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]