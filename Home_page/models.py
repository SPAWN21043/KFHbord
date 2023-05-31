from django.db import models


# Модель для описания сайта на главной странице
class InfoSite(models.Model):
    pass


# Модель для информации о КФХ в разделе о нас
class AboutUs(models.Model):
    pass


# Тип для связи
class TypePhoneKFH(models.Model):
    pass


# Модель Телефоны для связи
class PhoneKFH(models.Model):
    pass


# Модель контакты
class ContactsKFH(models.Model):
    address_kfh = models.CharField(max_length=250)
    email_kfh = models.EmailField()
    work_kfh = models.CharField(max_length=100)


# Модель для новостей
class NewsKFH(models.Model):
    pass


# Карточка КФХ
class CardKFH(models.Model):
    pass
