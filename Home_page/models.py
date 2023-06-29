from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Модель для описания сайта на главной странице
class InfoSite(models.Model):
    id_info_site = models.BigAutoField(primary_key=True)
    # info_site_kfh = models.TextField()
    info_site_kfh = CKEditor5Field(verbose_name='Описание сайта', config_name='extends')

    class Meta:
        verbose_name = "Описание главной страницы"
        verbose_name_plural = verbose_name


# Модель для информации о КФХ в разделе о нас
class AboutUs(models.Model):
    id_about_us = models.BigAutoField(primary_key=True)
    # about_us_kfh = models.TextField()
    about_us_kfh = CKEditor5Field(verbose_name='Описание о нас', config_name='extends')

    class Meta:
        verbose_name = "Описание страницы о нас"
        verbose_name_plural = verbose_name


# Тип для связи
class TypePhoneKFH(models.Model):
    id_type_phone = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250, name="Описание типа связи")

    class Meta:
        verbose_name = "Типы телефонов для связи"
        verbose_name_plural = verbose_name


# Модель Телефоны для связи
class PhoneKFH(models.Model):
    id_phone = models.BigAutoField(primary_key=True)
    number_phone = models.IntegerField(verbose_name="Телефон")
    type_phone = models.ForeignKey(TypePhoneKFH, on_delete=models.CASCADE)
    contacts_kfh = models.ForeignKey('ContactsKFH', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Информация о телефоне"
        verbose_name_plural = verbose_name


# Модель контакты
class ContactsKFH(models.Model):
    id_info_site = models.BigAutoField(primary_key=True)
    address_kfh = models.CharField(max_length=250)
    email_kfh = models.EmailField()
    work_kfh = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = verbose_name


# Модель для новостей
class NewsKFH(models.Model):
    id_new = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250)
    news = CKEditor5Field('Text', config_name='extends')

    class Meta:
        verbose_name = "Новости Акции"
        verbose_name_plural = verbose_name


# Карточка КФХ
class CardKFH(models.Model):
    id_card = models.BigAutoField(primary_key=True)
    inn_kfh = models.IntegerField(name="ИНН")
    ogrn_kfh = models.IntegerField(name="ОГРН")

    class Meta:
        verbose_name = "Карточка КФХ"
        verbose_name_plural = verbose_name
