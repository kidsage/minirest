from operator import mod
from accountapp.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify

from projectapp.models import Project

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # 회원 탈퇴를 했을 때 게시글이 사라지지 않고 주인 없는 게시글로 남음
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='project', null=True)
    slug = models.SlugField(max_length=200, allow_unicode=True, null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)
    liked_user = models.ManyToManyField(User, through='Like', related_name='likes')
    tags = TaggableManager(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.liked_user

    # def get_absolute_url(self):
    #     return reverse('articleapp:detail', slug=self.slug)

    def get_comments(self):
        return self.comment.filter(parent_comment=None)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_article')

    class Meta:
        unique_together = ('user', 'article')