# Generated by Django 5.2.1 on 2025-05-19 03:36

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriMenu',
            fields=[
                ('kategori_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(null=True)),
            ],
            options={
                'db_table': 'kategorimenu',
            },
        ),
        migrations.CreateModel(
            name='Meja',
            fields=[
                ('meja_id', models.AutoField(primary_key=True, serialize=False)),
                ('nomor_meja', models.CharField(max_length=10)),
                ('kapasitas', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'meja',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('admin', 'admin'), ('pelanggan', 'pelanggan')], default='pelanggan', max_length=15)),
                ('no_hp', models.CharField(max_length=100, null=True, unique=True)),
                ('alamat', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_menu', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(null=True)),
                ('harga', models.DecimalField(decimal_places=0, max_digits=10)),
                ('stok', models.IntegerField()),
                ('kategori', models.ForeignKey(db_column='kategori_id', on_delete=django.db.models.deletion.CASCADE, to='restoApp.kategorimenu')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('pesanan_id', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal_pesanan', models.DateTimeField()),
                ('status_pesanan', models.CharField(max_length=20)),
                ('total_harga', models.DecimalField(decimal_places=0, max_digits=12)),
                ('meja', models.ForeignKey(db_column='meja_id', on_delete=django.db.models.deletion.CASCADE, to='restoApp.meja')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pesanan',
            },
        ),
        migrations.CreateModel(
            name='DetailPesanan',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('jumlah', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=0, max_digits=12)),
                ('menu', models.ForeignKey(db_column='menu_id', on_delete=django.db.models.deletion.CASCADE, to='restoApp.menu')),
                ('pesanan', models.ForeignKey(db_column='pesanan_id', on_delete=django.db.models.deletion.CASCADE, to='restoApp.pesanan')),
            ],
            options={
                'db_table': 'detailpesanan',
            },
        ),
        migrations.CreateModel(
            name='ReservasiMeja',
            fields=[
                ('id_reservasi', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal_reservasi', models.DateTimeField()),
                ('jumlah_orang', models.IntegerField()),
                ('status', models.CharField(default='Menunggu', max_length=20)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('meja', models.ForeignKey(db_column='idmeja', on_delete=django.db.models.deletion.CASCADE, to='restoApp.meja')),
                ('user', models.ForeignKey(db_column='iduser', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reservasimeja',
                'constraints': [models.UniqueConstraint(fields=('meja', 'tanggal_reservasi'), name='uq_reservasi_unik')],
            },
        ),
    ]
