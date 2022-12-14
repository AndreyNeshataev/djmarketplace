# Generated by Django 4.1.1 on 2022-11-17 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество баллов')),
            ],
            options={
                'verbose_name': 'Переменная',
                'verbose_name_plural': 'Переменные',
            },
        ),
        migrations.RemoveField(
            model_name='goods',
            name='price',
        ),
        migrations.AddField(
            model_name='goods',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Описание товара'),
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
        migrations.AddField(
            model_name='goods',
            name='variables',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_shops', to='app_marketplace.variables', verbose_name='Магазин'),
        ),
    ]
