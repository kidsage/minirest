from django.urls import path

from searchapp.views import SearchListView

app_name = 'searchapp'

urlpatterns = [
    path('', SearchListView.as_view(), name='search'),
]