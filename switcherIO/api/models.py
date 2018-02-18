from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Device(models.Model):
    mac_address = models.CharField(max_length=16)
    serial_number = models.CharField(max_length=32)
    product = models.ForeignKey('Product')


class Product(models.Model):
    STATUS_READY = 0
    STATUS_PRODUCTION = 1
    STATUS_EXTINCTION = 2

    PRODUCT_STATUS = (
        (STATUS_READY, '준비중'),
        (STATUS_PRODUCTION, '생산중'),
        (STATUS_EXTINCTION, '단종됨'),
    )

    name = models.CharField(max_length=128, verbose_name='제품이름')
    price = models.IntegerField(default=0, validators=[MinValueValidator(-1),], verbose_name='제품가격')
    status = models.IntegerField(default=0, choices=PRODUCT_STATUS)