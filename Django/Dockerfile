# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
COPY . /code/

