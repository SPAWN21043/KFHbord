from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class TypeProduct(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


def load_main_photo(instance, filename):
    product_id = instance.id
    return f'product_{product_id}/main_photo/{filename}'


def load_dop_photo(instance, filename):
    product_id = instance.id
    return f'product_{product_id}/dop_photo/{filename}'


class Specification(models.Model):
    name_specification = models.CharField(max_length=250, verbose_name='Спецификация')

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'

    def __str__(self):
        return self.name_specification


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Категория')
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, related_name='Подкатегория')
    title_product = models.CharField(max_length=250, verbose_name='Название')
    # description_product = models.TextField()
    description_product = CKEditor5Field(verbose_name='Описание объявления', config_name='extends')
    main_photo = models.ImageField(verbose_name='Фото товара', upload_to=load_main_photo,
                                   blank=True, null=True, default='default_user/logo/user.png')
    specifications = models.ManyToManyField(Specification, related_name='specific')
    in_stock = models.BooleanField(verbose_name='Наличие')
    is_active = models.BooleanField(verbose_name='Активность продукта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title_product']

    def __str__(self):
        return self.title_product


class PackingType(models.Model):
    name = models.CharField(max_length=250, verbose_name='Упаковка')

    class Meta:
        verbose_name = 'Тип упаковки'
        verbose_name_plural = 'Типы упаковки'

    def __str__(self):
        return self.name


class PackingProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_pack')
    type_packing = models.ForeignKey(PackingType, on_delete=models.CASCADE, related_name='type_packing')
    price = models.DecimalField(verbose_name='Стоимость', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Упаковка продукта'
        verbose_name_plural = 'Упаковка продуктов'

    def __str__(self):
        return self.product


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(verbose_name='Доп фото', upload_to=load_dop_photo, blank=True, null=True)

    class Meta:
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительные фото'

    def __str__(self):
        return self.product
