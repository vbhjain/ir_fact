# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN mkdir /python-docker
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./python-docker /python-docker

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
