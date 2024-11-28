from django.urls import path
from .views import RegisterView, UserInfoView, ResourceListCreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='rbac_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('user-info/', views.UserInfoView.as_view(), name='user_info'),
    path('resources/', views.ResourceListCreateView.as_view(), name='resources'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),  # Ensure this is /api/logout/
]
