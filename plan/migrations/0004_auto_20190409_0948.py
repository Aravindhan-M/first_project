# Generated by Django 2.1.5 on 2019-04-09 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20190408_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='device_ram',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='plan_device',
        ),
        migrations.AlterField(
            model_name='plan',
            name='publication_date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 6, 48, 4, 452668, tzinfo=utc), verbose_name='Deactivate Plan on:'),
        ),
    ]
