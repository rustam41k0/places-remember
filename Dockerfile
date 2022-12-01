FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/places-remember

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ADD . .

#EXPOSE 8000
#CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']