from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView, CommentReplyView, CommentUpdateView


app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', CommentUpdateView.as_view(), name='update'),
    path('reply/<int:pk>', CommentReplyView.as_view(), name='reply'),
]