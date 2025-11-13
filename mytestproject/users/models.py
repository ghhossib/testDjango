from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''добавим поля для нашего пользователя '''
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20,null=True,blank=True)
    birthday = models.DateTimeField(null=True,blank=True)
    class Meta:
        verbose_name = "Пользователь" #для админ панели указывать названия сущности в единственном числе
        verbose_name_plural = "Пользователи" #для админ панели указывать названия сущности в единственном числе
