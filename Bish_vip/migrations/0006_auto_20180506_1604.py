# Generated by Django 2.0.4 on 2018-05-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bish_vip', '0005_auto_20180506_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='admin_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='user_is_active',
            field=models.BooleanField(default=True),
        ),
    ]
