# Generated by Django 4.1.1 on 2022-11-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_marketplace', '0003_alter_goods_variables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variables',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество товара'),
        ),
    ]
