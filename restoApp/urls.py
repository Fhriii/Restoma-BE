from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'users', CustomUserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'kategori-menu', KategoriMenuViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'meja', MejaViewSet)
router.register(r'pesanan', PesananViewSet)
router.register(r'detail-pesanan', DetailPesananViewSet)
router.register(r'reservasi', ReservasiMejaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
