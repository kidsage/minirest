from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleLikesView, ArticleListView, ArticleUpdateView, TagCloudView, TaggedObjectView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('like/<int:pk>', ArticleLikesView.as_view(), name='like'),
    path('tag/', TagCloudView.as_view() , name='tag_cloud'),
    path('tag/<str:tag>', TaggedObjectView.as_view(), name='tagged_object_list'),
]