FROM python:3.10-buster

ENV DEBIAN_FRONTEND noninteractive
COPY . /home/docker/code
WORKDIR /home/docker/code

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

CMD ["uvicorn", "main:app", "--reload"]
