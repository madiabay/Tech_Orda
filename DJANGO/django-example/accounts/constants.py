from django.db import models


class AmountCurrencyChoices(models.TextChoices):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'