from django.urls import path

from . import views

# reverse또는 템플릿의 {% url %}태그에서 사용
app_name = 'members'

urlpatterns = [
    # members.urls내의 패턴들은, prefix가 '/members/'임
    path('login/', views.login_view, name='login-view'),
]