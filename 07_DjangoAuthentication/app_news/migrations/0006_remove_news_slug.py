# Generated by Django 4.1.1 on 2022-09-26 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_news_slug_alter_news_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]