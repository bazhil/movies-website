# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /movies-website
COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install -r requirements.txt

RUN apt update
RUN apt install -y gdal-bin

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]