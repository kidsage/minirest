from django.urls import path
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountFollowView, AccountUpdateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accountapp'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # primary key 정보를 받기 위해 뒤에 int:pk 붙여줌
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('follow/', AccountFollowView.as_view(), name='follow'),
]