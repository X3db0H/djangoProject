# Generated by Django 5.0.3 on 2024-04-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_reg_options_reg_mail_reg_name_reg_surname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='mail',
            field=models.CharField(max_length=30, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='reg',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reg',
            name='surname',
            field=models.CharField(max_length=20, verbose_name='Фамиялия'),
        ),
    ]
