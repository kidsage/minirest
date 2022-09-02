from django.db import models
from accountapp.models import User
from articleapp.models import Article
from django.urls import reverse

# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField(null=False)
    created_at = models.DateField(auto_created=True, null=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True) # 1:N의 관계. 대댓글이 아닌 경우에는 null값이 생기니 True로 설정.

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.article.pk})



"""
comment 모델 내부에 parent 번호를 두어서 재귀호출로 사용을 할지, 아니면 reply로 종속되게 사용을 할지에 대한 선택이 필요하다.
거기에 view단에서 어떻게 처리할지에 대한 고민, template에서도 어떻게 보여줄지에 대한 고민이 꽤 오래됐는데,
아직 해결된 부분은 없다.

~ 9/1 여러 예제의 코드를 두고 실험을 했는데, 기본 구조가 달라 성공 결과를 볼 순 없었다.
9/2 > parent 번호를 두고 사용할 생각이다.
"""