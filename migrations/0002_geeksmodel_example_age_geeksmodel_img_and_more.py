# Generated by Django 5.0.6 on 2024-06-17 07:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='Example_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='geeksmodel',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='quot images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geeksmodel',
            name='vinay',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='geeksmodel',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]