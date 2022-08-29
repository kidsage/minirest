from django.db import models
from accountapp.models import User
from articleapp.models import Article

# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    # reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.content


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='reply')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content