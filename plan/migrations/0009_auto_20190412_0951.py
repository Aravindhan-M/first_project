# Generated by Django 2.1.5 on 2019-04-12 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0008_auto_20190411_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='publication_date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 6, 51, 36, 314186, tzinfo=utc), verbose_name='Deactivate Plan on:'),
        ),
    ]
