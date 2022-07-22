FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/kidsage/minirest.git

WORKDIR /home/minirest

RUN pip install -r requirements.txt

# 수정할 부분임 (임시 테스트용 시크릿 키 제공)
RUN echo "SECRET_KEY=django-insecure-!yts=3r-hvw&b@40qg7u-3e9umn62h=!-22yt-_)ecx!k8iv!*" > .env

RUN python manage.py migrate

EXPOSE 8000

# CMD ["gunicorn", "minirest.wsgi", "--bind", "0.0.0.0:8000"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]