"""HappiBodhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView, PeopleView
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('<int:pk>/edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='password'),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name="profile_page"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="create_profile_page"),
    path('people/', PeopleView.as_view(), name="people"),

]
