from django.urls import path
from account.views import AccountCreateView, AccountDetailView, hello_world
from django.contrib.auth.views import LoginView, LogoutView

app_name = "account"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),  # primary key 정보를 받기 위해 뒤에 int:pk 붙여줌
]