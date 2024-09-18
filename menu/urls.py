from django.urls import path
from .views import home, test_url, test_url1, test_url2

app_name = 'menu'

urlpatterns = [
    path('', home, name='home'),
    path('test/', test_url, name='test_url'),
    path('test1/', test_url1, name='test_url1'),
    path('test2/', test_url2, name='test_url2'),
]