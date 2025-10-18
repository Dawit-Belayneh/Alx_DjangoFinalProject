from rest_framework import permissions 

class IsAdminUserRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsAdminOrCashier(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.role == 'admin':
            return True

        if request.user.role == 'cashier' and request.method in ['GET', 'POST', 'PUT', 'PATCH']:
            return True

        return False