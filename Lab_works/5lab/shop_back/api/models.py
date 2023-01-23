from django.db import models


class Product(models.Model):
    category = models.ForeignKey(to='Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        )
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    amount = models.IntegerField()
    is_active = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=200)