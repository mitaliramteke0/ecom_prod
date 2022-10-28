from django.db import models
from enum import Enum
# Create your models here.
warranty=(('international','International'),
          ('national','National'), ('domestic','Domestic'))




class Product(models.Model):
        class Meta:
                db_table="prod"
                verbose_name="Product"
                verbose_name_plural="Products"

        # pid=models.AutoField(primary_key=True)
        name=models.CharField(max_length=20,verbose_name="Product Name")
        brand=models.CharField(max_length=22,verbose_name="Product Brand")
        price=models.FloatField()
        qty=models.SmallIntegerField()
        warranty=models.CharField(max_length=21,choices=warranty)
        Home_delivery=models.BooleanField()

        def __str__(self):
            return f"{self.name}"


class Gadgets(models.Model):
    class Meta:
        verbose_name = "Gadget"
        verbose_name_plural = "Gadgets"
