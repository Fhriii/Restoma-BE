from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, req):
        serializer = LoginSerializer(data=req.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class KategoriMenuViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = KategoriMenu.objects.all()
    serializer_class = KategoriMenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]


class MejaViewSet(viewsets.ModelViewSet):
    queryset = Meja.objects.all()
    serializer_class = MejaSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]


class PesananViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer


class DetailPesananViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DetailPesanan.objects.all()
    serializer_class = DetailPesananSerializer


class ReservasiMejaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ReservasiMeja.objects.all()
    serializer_class = ReservasiMejaSerializer
