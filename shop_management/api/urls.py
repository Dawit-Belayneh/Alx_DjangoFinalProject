from django.urls import path
from .views import UserListCreateAPIView, CategoryListCrateAPIView
from . import views

urlpatterns = [
    path("users/", views.UserListCreateAPIView.as_view(), name="api/user"),
    path("categorys/", views.CategoryListCrateAPIView.as_view(), name="api/category")
]