from django.urls import path

from projectapp.views import ProjectCreateView

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetialView.as_view(), name='detail'),
]