from django.shortcuts import render
from rest_framework import generics
from inventory.models import User, Category, Product
from .serializers import UserSerializer, ProductSerializer, CustomerSerializer, SaleSerializer, SaleItemSerializer, CategorySerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryListCrateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCrateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer