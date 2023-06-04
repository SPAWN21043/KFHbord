from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Product(models.Model):
    category = models.OneToOneField()
    type_product = models.OneToOneField()
    name_product = models.CharField(max_length=200)
    description = CKEditor5Field('Text', config_name='extends')
    specification_product = models.ManyToManyField()
    info_product = models.OneToOneField()
    in_stock_product = models.IntegerField()
    price_product = models.FloatField()
    currency_product = models.OneToOneField()
    pass
