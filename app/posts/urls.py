from django.urls import path

from . import views

# 이 urls모듈의 app_name에 'posts'를 사용
#

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post-list'),
]