FROM python:3.7.5

ADD ./recipe-server /recipe-server

WORKDIR /recipe-server

RUN pip install -r requirements/prod.txt

RUN flask db upgrade

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
