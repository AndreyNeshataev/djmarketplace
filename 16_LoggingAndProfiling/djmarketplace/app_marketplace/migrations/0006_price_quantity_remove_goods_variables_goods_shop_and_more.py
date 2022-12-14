# Generated by Django 4.1.1 on 2022-11-18 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_marketplace', '0005_remove_goods_shop_variables_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество товара')),
            ],
        ),
        migrations.RemoveField(
            model_name='goods',
            name='variables',
        ),
        migrations.AddField(
            model_name='goods',
            name='shop',
            field=models.ManyToManyField(related_name='goods_shop', to='app_marketplace.marketplace', verbose_name='Магазин'),
        ),
        migrations.DeleteModel(
            name='Variables',
        ),
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_marketplace.price', verbose_name='Переменные'),
        ),
        migrations.AddField(
            model_name='goods',
            name='quantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_marketplace.quantity', verbose_name='Переменные'),
        ),
    ]
