# Generated by Django 2.0.4 on 2018-05-06 07:58

import Bish_vip.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bish_vip', '0002_auto_20180506_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_2',
            field=models.FileField(blank=True, null=True, upload_to=Bish_vip.models.upload_location),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_3',
            field=models.FileField(blank=True, null=True, upload_to=Bish_vip.models.upload_location),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_4',
            field=models.FileField(blank=True, null=True, upload_to=Bish_vip.models.upload_location),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_5',
            field=models.FileField(blank=True, null=True, upload_to=Bish_vip.models.upload_location),
        ),
    ]
