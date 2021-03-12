FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1


WORKDIR /code
# COPY . /code
COPY ./requirements.txt /code
COPY ./entrypoint.sh /code
RUN pip install -r /code/requirements.txt


ENTRYPOINT ["/code/entrypoint.sh"]
