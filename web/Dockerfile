FROM python:3.7
LABEL maintainer="nicholas.johnston@sheridancollege.ca"

ADD ./runserver.sh /runserver.sh
ADD ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt && pip install gunicorn

ADD ./app /app

ENTRYPOINT ["/runserver.sh"]
