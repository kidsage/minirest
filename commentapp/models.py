from django.db import models
from accountapp.models import User
from articleapp.models import Article
from django.urls import reverse

# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True) # 1:N의 관계. 대댓글이 아닌 경우에는 null값이 생기니 True로 설정.

    def __str__(self):
        return self.content



"""
comment 모델 내부에 parent 번호를 두어서 재귀호출로 사용을 할지, 아니면 reply로 종속되게 사용을 할지에 대한 선택이 필요하다.
거기에 view단에서 어떻게 처리할지에 대한 고민, template에서도 어떻게 보여줄지에 대한 고민이 꽤 오래됐는데,
아직 해결된 부분은 없다.

~ 9/1 여러 예제의 코드를 두고 실험을 했는데, 기본 구조가 달라 성공 결과를 볼 순 없었다.
9/2 > parent 번호를 두고 사용할 생각이다. 
9/3 > 시리얼라이징을 하려고 했는데, 아싸리 따로 구현한 다음에 띄우는 방법도 간단히 사용할 수 있겠구나 생각이 듬
 > 시리얼라이징을 하면 처음에는 메인 parent comment들만 띄워놓고, 불러온 후에 댓글을 볼 수 있는 기능을 구현할 수 있음
 > 대댓글을 그냥 띄우면 따로 시리얼라이징 없이 바로 댓글 구현이 가능함.
"""