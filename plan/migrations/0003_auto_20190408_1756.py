# Generated by Django 2.1.5 on 2019-04-08 14:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_20190405_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinstallment',
            name='device',
        ),
        migrations.AddField(
            model_name='deviceinstallment',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_installment_phone', to='plan.DeviceRam'),
        ),
        migrations.AddField(
            model_name='deviceinstallment',
            name='plan_device',
            field=models.ManyToManyField(blank=True, related_name='device_installment_device', to='plan.PlanDevice', verbose_name='Plan Device'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publication_date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 14, 56, 44, 928449, tzinfo=utc), verbose_name='Deactivate Plan on:'),
        ),
    ]
