FROM python:3.8
LABEL maintainer="amontg14@uoregon.edu"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt