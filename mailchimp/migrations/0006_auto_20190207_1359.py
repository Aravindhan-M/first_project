# Generated by Django 2.1.5 on 2019-02-07 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailchimp', '0005_auto_20190206_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailscheduler',
            options={'verbose_name': 'Scheduler', 'verbose_name_plural': 'Email Schedulers'},
        ),
    ]
