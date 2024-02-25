FROM python:3.10-buster

ENV DEBIAN_FRONTEND noninteractive
COPY . /home/docker/code/
RUN pip install fastapi