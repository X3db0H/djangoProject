from django.db import models


class Reg(models.Model):
    login = models.CharField('Логин', max_length=30)
    password = models.CharField('Пароль', max_length=20)
    mail = models.CharField('Почта', max_length=30,)
    name = models.CharField('Имя', max_length=20,)
    surname = models.CharField('Фамиялия', max_length=20,)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
