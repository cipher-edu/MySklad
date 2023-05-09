# models.py
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
# to'lov turlari
class Cash(models.Model):
    cash_value = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'To\'lov turui'
        verbose_name_plural = 'To\'lov turi'

    def __str__(self):
        return self.cash_value
# ishchilarni ro'yxatga olish
# class Ishchilar(models.Model):
#     worker_name = models.CharField(max_length=45, verbose_name="Ismi")
#     worker_stage = models.IntegerField()

#     class Meta:
#         verbose_name = 'ishchilar nomi'
#         verbose_name_plural = 'ishchilar nomi'
#     def __str__(self):
#         return self.worker_name
    
class UserRegister(models.Model):
    name = models.CharField(max_length=150, verbose_name='foydalanuvchining ismi')
    number = models.IntegerField(verbose_name='Foydalanuvchinig telefon raqami')
    ovner = models.CharField(max_length=150, verbose_name='ishchi nomi')
    client_reception_time = models.DateField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        verbose_name = 'Klient yaratish'
        verbose_name_plural = 'Klient yaratish'
    def __str__(self):
        return self.client_name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(UserRegister, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Foydalanuvchi yaratish'
        verbose_name_plural = 'Foydalanuvchilarni yaratish'
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    items_incash_value = models.ForeignKey(Cash, on_delete=models.CASCADE, verbose_name="To'lov turi") 
    items_outprice = models.IntegerField(verbose_name="Sotilish narxi")
    brand = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name
    
class UserService(models.Model):
    name = models.ForeignKey( UserRegister, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} {self.product} {'added' if self.added else 'subtracted'} on {self.date}"

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} {self.product} {'added' if self.added else 'subtracted'} on {self.date}"
