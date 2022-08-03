from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # 회원 탈퇴를 했을 때 게시글이 사라지지 않고 주인 없는 게시글로 남음
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='project', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)
    liked_user = models.ManyToManyField(User, through='Like', related_name='like')

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.liked_user


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_article')

    class Meta:
        unique_together = ('user', 'article')