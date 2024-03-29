# Generated by Django 4.2.1 on 2023-08-07 06:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_value', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': "To'lov turui",
                'verbose_name_plural': "To'lov turi",
            },
        ),
        migrations.CreateModel(
            name='CerviseClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='Maxsulot nomini kiriting')),
                ('product_value', models.IntegerField(verbose_name='Maxsulot qiymatini kiriting')),
                ('product_color', models.CharField(max_length=35, verbose_name='Maxsulot rangini kiriting')),
            ],
            options={
                'verbose_name': "Service xizmat ko'rsatish",
                'verbose_name_plural': "Service xizmat ko'rsatish",
            },
        ),
        migrations.CreateModel(
            name='Clientadd',
            fields=[
                ('client_name', models.CharField(max_length=50, unique=True)),
                ('client_phonenumber', models.IntegerField(unique=True)),
                ('client_reception_time', models.DateField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Klient yaratish',
                'verbose_name_plural': 'Klient yaratish',
            },
        ),
        migrations.CreateModel(
            name='Organizationscategory',
            fields=[
                ('categoryname', models.CharField(max_length=100)),
                ('descriptions', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': "kategoriyalar ro'yxati",
            },
        ),
        migrations.CreateModel(
            name='Organizationsservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_catetegory', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Xizmat turlari',
                'verbose_name_plural': 'Xizmat turlari',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=45, verbose_name='Ismi')),
                ('worker_surname', models.CharField(max_length=45, verbose_name='Familiya')),
                ('worker_age', models.IntegerField(verbose_name='Yoshi')),
                ('worker_stage', models.IntegerField()),
            ],
            options={
                'verbose_name': 'ishchilar nomi',
                'verbose_name_plural': 'ishchilar nomi',
            },
        ),
        migrations.CreateModel(
            name='OrganizationPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_organizations', models.IntegerField()),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('payment_coment', models.TextField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='skladik.organizationscategory')),
            ],
            options={
                'verbose_name': "Tashkilot to'lovi",
                'verbose_name_plural': "Tashkilotlar to'lovi",
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('items_brand', models.CharField(max_length=150, verbose_name='Brend nomi')),
                ('items_name', models.CharField(max_length=150, verbose_name='Tovar nomi')),
                ('items_inprice', models.IntegerField(verbose_name='Tovar narxi')),
                ('items_outprice', models.IntegerField(verbose_name='Sotilish narxi')),
                ('items_value', models.IntegerField(verbose_name='Qiymati (dona)')),
                ('items_color', models.CharField(max_length=50, verbose_name='Tovar rangi')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('items_incash_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.cash', verbose_name="To'lov turi")),
            ],
            options={
                'verbose_name': 'Mahsulot turlari',
                'verbose_name_plural': 'Mahsulot turlarini yaratish',
            },
        ),
        migrations.CreateModel(
            name='EndserviceClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_defective', models.CharField(max_length=150, verbose_name='Maxsulot aybi')),
                ('product_repaired', models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlash")),
                ('produtct_not_repaired', models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlamaslik")),
                ('kuchadan_tovar', models.CharField(max_length=150, verbose_name='bozordan tavar olinishi')),
                ('cervice_item_price', models.IntegerField(verbose_name='Ishlatilingan texnika narxi')),
                ('clien_service_price', models.IntegerField(verbose_name='Service narxi')),
                ('coment', models.TextField(verbose_name='koment')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.clientadd', verbose_name='Mijozni tanlang')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.cerviseclient', verbose_name='Texnikani tanla')),
                ('sklad_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.items', verbose_name='Sklad maxsulot')),
                ('topshiruvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.worker', verbose_name='xizmatni yakunlvchi')),
            ],
            options={
                'verbose_name': 'Service xizmat yakunlash',
                'verbose_name_plural': 'Service xizmat yakunlash',
            },
        ),
        migrations.AddField(
            model_name='clientadd',
            name='ovner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.worker'),
        ),
        migrations.AddField(
            model_name='cerviseclient',
            name='client_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.clientadd', verbose_name='Mijozni tanlang'),
        ),
        migrations.AddField(
            model_name='cerviseclient',
            name='service_catetegory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.organizationsservice', verbose_name='Service xizmat turi'),
        ),
        migrations.CreateModel(
            name='AddOrganization',
            fields=[
                ('service_soni', models.IntegerField()),
                ('service_narxi', models.IntegerField()),
                ('xizmat_haqida', models.TextField()),
                ('service_date', models.DateField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='skladik.organizationscategory')),
                ('servise_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skladik.clientadd')),
            ],
            options={
                'verbose_name': 'Ishhona',
                'verbose_name_plural': "Ishhonalarga xizmat qo'shish",
            },
        ),
    ]
