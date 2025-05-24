from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permission import IsAdminOrReadOnly

class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, req):
        serializer = LoginSerializer(data=req.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegisterViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create(
                username=serializer.validated_data['username'],
            )
            user.set_password(serializer.validated_data['password'])  # Hashing
            user.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": RegisterSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserViewSet(viewsets.ModelViewSet):
    # Hanya admin bisa edit user, pelanggan hanya bisa lihat (jika diperbolehkan)
    permission_classes = [IsAdminOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    # Role hanya bisa diubah oleh admin
    permission_classes = [IsAdminOrReadOnly]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class KategoriMenuViewSet(viewsets.ModelViewSet):
    # Admin bisa tambah/edit/hapus kategori, pelanggan hanya lihat
    permission_classes = [IsAdminOrReadOnly]
    queryset = KategoriMenu.objects.all()
    serializer_class = KategoriMenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    # Admin bisa tambah/edit/hapus menu, pelanggan hanya lihat
    permission_classes = [IsAdminOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MejaViewSet(viewsets.ModelViewSet):
    # Admin bisa tambah/edit/hapus meja, pelanggan hanya lihat
    permission_classes = [IsAdminOrReadOnly]
    queryset = Meja.objects.all()
    serializer_class = MejaSerializer


class PesananViewSet(viewsets.ModelViewSet):
    # Pelanggan bisa membuat pesanan, admin bisa lihat semua
    permission_classes = [IsAuthenticated]
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer


class DetailPesananViewSet(viewsets.ModelViewSet):
    # Pelanggan bisa lihat detail, admin yang kelola
    permission_classes = [IsAdminOrReadOnly]
    queryset = DetailPesanan.objects.all()
    serializer_class = DetailPesananSerializer


class ReservasiMejaViewSet(viewsets.ModelViewSet):
    # Pelanggan boleh reservasi meja
    permission_classes = [IsAuthenticated]
    queryset = ReservasiMeja.objects.all()
    serializer_class = ReservasiMejaSerializer
