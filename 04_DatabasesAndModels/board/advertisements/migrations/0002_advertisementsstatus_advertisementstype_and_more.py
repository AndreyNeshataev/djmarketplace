# Generated by Django 4.1.1 on 2022-09-14 05:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementsStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='advertisement',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='description',
            field=models.CharField(default='', max_length=1500, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(default=0, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='title',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, max_length=1500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementsstatus'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementstype'),
        ),
    ]
