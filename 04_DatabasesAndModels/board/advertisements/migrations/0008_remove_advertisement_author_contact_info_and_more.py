# Generated by Django 4.1.1 on 2022-09-14 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0007_rename_advertisementstatus_advertisementsstatus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='author_contact_info',
        ),
        migrations.DeleteModel(
            name='AdvertisementContactInformation',
        ),
    ]
