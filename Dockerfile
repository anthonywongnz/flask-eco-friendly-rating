# syntax=docker/dockerfile:1

FROM python:3.10-alpine

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

USER 1001
EXPOSE 5000
CMD [ "env.sh", "python3", "/app/run.py"]
