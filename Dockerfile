FROM python:3.9.0

WORKDIR /home/

RUN echo "server test"

RUN git clone https://github.com/kidsage/minirest.git

WORKDIR /home/minirest/

RUN pip install -r requirements.txt

RUN pip install psycopg2

RUN echo "SECRET_KEY=django-insecure-!yts=3r-hvw&b@40qg7u-3e9umn62h=!-22yt-_)ecx!k8iv!*" > .env

RUN python3 manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=minirest.settings.prod && gunicorn minirest.wsgi --env DJANGO_SETTINGS_MODULE=minirest.settings.prod --bind 0.0.0.0:8000"]