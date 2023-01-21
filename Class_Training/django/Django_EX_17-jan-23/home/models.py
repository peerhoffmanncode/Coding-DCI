from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_num = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    price = models.FloatField()
