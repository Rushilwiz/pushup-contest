FROM python:3.8-alpine

RUN mkdir -p /home/app

RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV APP_HOME=/home/app/site
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add libpq postgresql-dev \
    gcc python3-dev musl-dev libffi-dev

COPY . $APP_HOME

RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN chown -R app:app $APP_HOME

USER app

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "config.wsgi"]