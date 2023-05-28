from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SalesRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    partner_organization = models.CharField(max_length=255)
    sold_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.partner_organization
