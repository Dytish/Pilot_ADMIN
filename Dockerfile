FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.4.2

RUN apt-get update && apt-get install -y vim && apt-get upgrade -y

COPY ./requirements.txt /requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

RUN mkdir -p /django/static
RUN chmod 777 -R /django/static
RUN mkdir -p /django/media && chmod 777 -R /django/media

COPY django /django
WORKDIR /django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]