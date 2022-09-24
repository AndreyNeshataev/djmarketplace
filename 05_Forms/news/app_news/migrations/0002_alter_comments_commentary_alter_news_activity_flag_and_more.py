# Generated by Django 4.1.1 on 2022-09-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentary',
            field=models.CharField(max_length=500, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='news',
            name='activity_flag',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Заголовок'),
        ),
    ]
