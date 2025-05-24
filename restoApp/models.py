from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'roles'


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('pelanggan', 'pelanggan'),
     
    )
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=15, choices=ROLE_CHOICES,default="pelanggan")
    no_hp = models.CharField(unique=True, max_length=100,null=True)
    alamat = models.CharField( max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        db_table = 'users'

class KategoriMenu(models.Model):
    kategori_id = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)
    deskripsi = models.TextField(null=True)

    class Meta:
        db_table = 'kategorimenu'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    nama_menu = models.CharField(max_length=100)
    deskripsi = models.TextField(null=True)
    harga = models.DecimalField(max_digits=10, decimal_places=0)
    kategori = models.ForeignKey(KategoriMenu, on_delete=models.CASCADE, db_column='kategori_id')
    stok = models.IntegerField()
    foto =  models.ImageField(upload_to="assets/", null=True, blank=True)


    class Meta:
        db_table = 'menu'


class Meja(models.Model):
    meja_id = models.AutoField(primary_key=True)
    nomor_meja = models.CharField(max_length=10)
    kapasitas = models.IntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'meja'


class Pesanan(models.Model):
    pesanan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='user_id')
    meja = models.ForeignKey(Meja, on_delete=models.CASCADE, db_column='meja_id')
    tanggal_pesanan = models.DateTimeField()
    status_pesanan = models.CharField(max_length=20)
    total_harga = models.DecimalField(max_digits=12, decimal_places=0)

    class Meta:
        db_table = 'pesanan'


class DetailPesanan(models.Model):
    detail_id = models.AutoField(primary_key=True)
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE, db_column='pesanan_id')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, db_column='menu_id')
    jumlah = models.IntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=0)

    class Meta:
        db_table = 'detailpesanan'


class ReservasiMeja(models.Model):
    id_reservasi = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='iduser')
    meja = models.ForeignKey(Meja, on_delete=models.CASCADE, db_column='idmeja')
    tanggal_reservasi = models.DateTimeField()
    jumlah_orang = models.IntegerField()
    status = models.CharField(max_length=20, default='Menunggu')
    keterangan = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'reservasimeja'
        constraints = [
            models.UniqueConstraint(fields=['meja', 'tanggal_reservasi'], name='uq_reservasi_unik')
        ]