# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /movies-website
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt update
RUN apt install -y gdal-bin

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]