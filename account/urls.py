from django.urls import path
from account.views import AccountCreateView, hello_world

app_name = "account"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
]