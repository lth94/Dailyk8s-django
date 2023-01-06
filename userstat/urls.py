from django.urls import path

from . import views

app_name = 'userstat'

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('ranking/', views.ranking, name='ranking'),
    path('solved/', views.solved, name='solved'),
]