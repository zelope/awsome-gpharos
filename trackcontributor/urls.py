from django.urls import path
from . import views

urlpatterns = [
    path('', views.contributor, name='contributor'),  # 대시보드 페이지 URL 패턴
]
