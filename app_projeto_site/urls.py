from django.urls import path
from app_projeto_site import views


urlpatterns = [
     path('', views.home, name='home'),
     path('profile/', views.profile, name='profile'),
     path('profile-user/',views.profile_user, name='profile-user'),
     path('login/', views.login_user, name = 'login'),
     path('logout/', views.logout_user, name = 'logout'),
     path('register/', views.RegisterView.as_view(), name='register'),
]