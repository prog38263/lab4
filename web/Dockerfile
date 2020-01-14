FROM python:3.7
LABEL maintainer="nicholas.johnston@sheridancollege.ca"

COPY . /

RUN pip install -r requirements.txt && pip install gunicorn

ENTRYPOINT ["/runserver.sh"]
