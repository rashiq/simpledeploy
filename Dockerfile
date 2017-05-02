FROM python:2.7.13
RUN apt-get update -y
RUN apt-get install -y gunicorn
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
