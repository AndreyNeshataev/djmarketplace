# Generated by Django 4.1.1 on 2022-09-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0015_alter_comments_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user_name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Имя пользователя'),
        ),
    ]