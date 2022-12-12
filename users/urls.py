
from . import views
from django.urls import path

urlpatterns = [
    path("users/", views.RegisterView.as_view()),
    path("users/login", views.LoginView.as_view()),
]