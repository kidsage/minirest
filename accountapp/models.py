from django.db import models

# Create your models here.
# cmd = python manage.py makemigrations < 생성
#     = python manage.py migrate < 연동

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
