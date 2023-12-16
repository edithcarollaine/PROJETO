from django.urls import path
from app_organizador import views

urlpatterns = [
    path('criar/', views.evento, name='criar'),
    path('cursos/', views.lista, name='cursos'),
]