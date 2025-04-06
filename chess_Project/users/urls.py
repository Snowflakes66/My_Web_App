from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, UserView, custom_login, HomeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
]