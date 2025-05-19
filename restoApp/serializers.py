
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import  RefreshToken
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'status', 'password','no_hp','alamat']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'],password=data['password'])
        if not user:
            raise serializers.ValidationError("Username atau Password tidak ditemukan")

        refresh =RefreshToken.for_user(user)
        return{
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user':UserSerializer(user).data
        }

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'no_hp', 'alamat')


   

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            no_hp=validated_data['no_hp'],
            alamat=validated_data['alamat']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'status', 'no_hp', 'alamat', 'created_at'
        ]


class KategoriMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriMenu
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    kategori = KategoriMenuSerializer(read_only=True)
    kategori_id = serializers.PrimaryKeyRelatedField(
        queryset=KategoriMenu.objects.all(), source='kategori', write_only=True
    )

    class Meta:
        model = Menu
        fields = ['menu_id', 'nama_menu', 'deskripsi', 'harga', 'stok', 'kategori', 'kategori_id']


class MejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meja
        fields = '__all__'


class PesananSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), source='user', write_only=True
    )
    meja = MejaSerializer(read_only=True)
    meja_id = serializers.PrimaryKeyRelatedField(
        queryset=Meja.objects.all(), source='meja', write_only=True
    )

    class Meta:
        model = Pesanan
        fields = [
            'pesanan_id', 'user', 'user_id', 'meja', 'meja_id',
            'tanggal_pesanan', 'status_pesanan', 'total_harga'
        ]


class DetailPesananSerializer(serializers.ModelSerializer):
    pesanan = PesananSerializer(read_only=True)
    pesanan_id = serializers.PrimaryKeyRelatedField(
        queryset=Pesanan.objects.all(), source='pesanan', write_only=True
    )
    menu = MenuSerializer(read_only=True)
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(), source='menu', write_only=True
    )

    class Meta:
        model = DetailPesanan
        fields = ['detail_id', 'pesanan', 'pesanan_id', 'menu', 'menu_id', 'jumlah', 'subtotal']


class ReservasiMejaSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    iduser = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), source='user', write_only=True
    )
    meja = MejaSerializer(read_only=True)
    idmeja = serializers.PrimaryKeyRelatedField(
        queryset=Meja.objects.all(), source='meja', write_only=True
    )

    class Meta:
        model = ReservasiMeja
        fields = [
            'id_reservasi', 'user', 'iduser', 'meja', 'idmeja',
            'tanggal_reservasi', 'jumlah_orang', 'status', 'keterangan'
        ]

