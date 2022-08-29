from accountapp.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # user객체가 사라지면 프로필도 같이 삭제
    image = models.ImageField(upload_to='profile/', null=True) # media 밑에 profile 경로에 저장이 된다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)