from django.urls import path
from .views import UserListCreateAPIView
from . import views

urlpatterns = [
    path("users/", views.UserListCreateAPIView.as_view(), name="api/user")
]