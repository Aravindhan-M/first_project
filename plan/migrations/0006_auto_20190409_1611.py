# Generated by Django 2.1.5 on 2019-04-09 13:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_auto_20190409_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='publication_date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 11, 16, 483899, tzinfo=utc), verbose_name='Deactivate Plan on:'),
        ),
    ]
