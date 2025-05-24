from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Izin hanya untuk admin jika ingin mengubah data (POST, PUT, DELETE),
    user biasa hanya bisa membaca (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        # Jika metode HTTP adalah GET/SAFE, siapa saja yang login bisa akses
        if request.method in SAFE_METHODS:
            return True
        
        # Selain itu, hanya user dengan status 'admin' yang boleh
        return request.user.is_authenticated and request.user.status == 'admin'
