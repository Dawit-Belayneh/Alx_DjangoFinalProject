from django.urls import path
from . import views



urlpatterns = [
    path("users/", views.UserListCreateAPIView.as_view(), name="api-user"),
    path("user/<int:pk>", views.UserDetailAPIView.as_view(), name="api-user-detail"),
    path("categorys/", views.CategoryListCrateAPIView.as_view(), name="api-category"),
    path("category/<int:pk>", views.CategoryDetailAPIView.as_view(), name="api-category-detail"),
    path("products/", views.ProductListCrateAPIView.as_view(), name ="api-product"),
    path("product/<int:pk>/", views.ProductDetailAPIView.as_view(), name="api-product-detail"),
    path("sales/", views.SaleListCreateAPIView.as_view(), name = "api-sales"),
    path("sale/<int:pk>/", views.SaleDetailAPIView.as_view(), name="api-sales-detail"),
    path("saleitems/", views.SaleItemListCreateAPIView.as_view(), name = "api-saleItem"),
    path("saleitem/<int:pk>/", views.SaleItemDetailAPIView.as_view(), name = "api-saleitem-detail"),
    path("customers/", views.CustomerListCreateAPIView.as_view(), name="api-customer"),
    path("customer/<int:pk>/", views.CustomerDetailAPIView.as_view(), name="api-customer-detail"),
]