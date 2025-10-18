from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from inventory.models import User, Category, Product, Customer, Sale, SaleItem
from .serializers import (
    UserSerializer, 
    ProductSerializer, 
    CustomerSerializer, 
    SaleSerializer, 
    SaleItemSerializer, 
    CategorySerializer,
    UserSignupSerializer,
    UserLoginSerializer,
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserRole, IsAdminOrCashier
from django.shortcuts import get_object_or_404


# users list view api
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUserRole]

# user detail views api
class UserDetailAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUserRole]
    # get list or single user
    def get(self, request, pk=None):

        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    #update single list
    def patch(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete single list
    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# category list

class CategoryListCrateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]


# category detail list

class CategoryDetailAPIView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]
    # get list or single category
    def get(self, request, pk=None):

        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
    # update single list
    def patch(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delte single list
    def delete(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)
        category.delete()
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# product list api view

class ProductListCrateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]

# product detail api view

class ProductDetailAPIView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]
    # get list or single product
    def get(self, request, pk):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data)
    #update single list
    def patch(self, request, pk):
        product = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.get_serializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    #delete a single list
    def delete(self, request, pk):
        product = self.get_object()
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



# customer all list api view
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]

#customer detail list view
class CustomerDetailAPIView(generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]
    # get list or single customer
    def get(self, request, pk=None):

        if pk:
            try:
                customer = Customer.objects.get(pk=pk)
                serializer = CustomerSerializer(customer)
            except Customer.DoesNotExist:
                return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            customer = Customer.objects.all()
            serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    # update single list
    def patch(self, request, pk=None):
        customer = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  delete a single list
    def delete(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_400_BAD_REQUEST)
        customer.delete()
        return Response({"message": "Customer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# sale item all list
class SaleItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]

# sale item detail list
class SaleItemDetailAPIView(generics.GenericAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]
    # get list or single sale item
    def get(self, request, pk=None):

        if pk:
            try:
                sale_item = SaleItem.objects.get(pk=pk)
                serializer = SaleItemSerializer(sale_item)
            except SaleItem.DoesNotExist:
                return Response({"error": "SaleItem not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            sale_item = SaleItem.objects.all()
            serializer = SaleItemSerializer(sale_item, many=True)
        return Response(serializer.data)
    # update a list
    def patch(self, request, pk=None):
        try:
            sale_item = SaleItem.objects.get(pk=pk)
        except SaleItem.DoesNotExist:
            return Response({"error": "SaleItem not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SaleItemSerializer(sale_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete a list
    def delete(self, request, pk=None):
        try:
            sale_item = SaleItem.objects.get(pk=pk)
        except SaleItem.DoesNotExist:
            return Response({"error": "SaleItem not found"}, status=status.HTTP_400_BAD_REQUEST)
        sale_item.delete()
        return Response({"message": "SaleItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# sale item api view
class SaleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]

# sale item detail api view
class SaleDetailAPIView(generics.GenericAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCashier]
    # get list or single sale
    def get(self, request, pk=None):

        if pk:
            try:
                sale = Sale.objects.get(pk=pk)
                serializer = SaleSerializer(sale)
            except Sale.DoesNotExist:
                return Response({"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            sale = Sale.objects.all()
            serializer = SaleSerializer(sale, many=True)
        return Response(serializer.data)

    # update a list
    def patch(self, request, pk=None):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SaleSerializer(sale_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a list
    def delete(self, request, pk=None):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({"error": "Sale not found"}, status=status.HTTP_400_BAD_REQUEST)
        sale.delete()
        return Response({"message": "Sale deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


#login and signup views

class SignupAPIView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "message": "User created successfully",
            "token": token.key,
            "username": user.username,
            "role": user.role
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "username": user.username,
            "role": user.role
        }, status=status.HTTP_200_OK)