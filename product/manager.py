from django.db import models


class ProductManager(models.manager):

        def get_samsung_products(self):
            super().get_queryset().filter(brand__iexact="samsung").all()