# Generated by Django 4.2.7 on 2024-09-22 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_expedition_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 22, 17, 20, 2, 314764, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]
