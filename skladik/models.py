from django.db import models
import uuid 
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Ishchilar(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
# pul birliklari start
class Cash(models.Model):
    cash = models.CharField(max_length=15, verbose_name="Valyuta nomi")

    def __str__(self):
        return self.cash
# pul birliklari end

# service xizmatlar turi

class ServiceCategory(models.Model):
    servicee_name = models.CharField(max_length=150, verbose_name='Servise xiamt nomi')

    def __str__(self):
        return self.servicee_name
    
#service xizmat end

# product register start
class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="Maxsulot nomi")
    cash = models.ForeignKey(Cash, on_delete=models.CASCADE, verbose_name="To'lov turi")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    items_incash_value = models.ForeignKey(Cash, on_delete=models.CASCADE, verbose_name="To'lov turi") 
    items_outprice = models.IntegerField(verbose_name="Sotilish narxi")
    brand = models.CharField(max_length=150, verbose_name="Maxsulot brandi")
    color = models.CharField(max_length=150, verbose_name="Maxsulot rangi")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.product_name
# product register end

# user ruyxatga olish start
class UserRegister(models.Model):
    user_name = models.CharField(max_length=150, verbose_name="Mijoz ismi")
    user_phone = models.IntegerField(verbose_name='Mijoz raqami')

    class Meta:
        verbose_name = 'Klient yaratish'
        verbose_name_plural = 'Klient yaratish'
    def __str__(self):
        return self.user_names
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(UserRegister, self).save(*args, **kwargs)
    
# user ruyxatga olish end

# user qabul qilish start

class UserReseption(models.Model):
    user_name = models.ForeignKey(UserRegister, on_delete=models.CASCADE, verbose_name='Foydalanuvchining ismi')
    service = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Service xizmat nomi')
    product = models.CharField(max_length=150, verbose_name='Texnika nomi')
    quanity = models.IntegerField(verbose_name= 'Texnika qiymati')
    color = models.CharField(max_length=150, verbose_name='Texnika rangi')

    class Meta:
        verbose_name = 'mijozni qabul qilish'
        verbose_name_plural = 'Mijozlarni qabul qilish'

    def __str__(self):
        return self.color
    
# user qabul qilish end

class UserCervice(models.Model):
    product_defective = models.CharField(max_length=150, verbose_name="Maxsulot aybi")
    product_repaired = models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlash")
    produtct_not_repaired = models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlamaslik")
    cervice_item_price = models.IntegerField(verbose_name="Ishlatilingan texnika narxi")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='maxsulot')
    quantity = models.IntegerField(verbose_name='qiymati')
    added = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    clien_service_price = models.IntegerField(verbose_name="Service narxi")
    topshiruvchi = models.ForeignKey(Ishchilar, on_delete=models.CASCADE, verbose_name='xizmatni yakunlvchi')

    class Meta:
        verbose_name = 'Service xizmat yakunlash'
        verbose_name_plural = 'Service xizmat yakunlash'
    
    def __str__(self):
        return f"{self.quantity} {self.product} {'added' if self.added else 'subtracted'} on {self.date}"