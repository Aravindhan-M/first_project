# Generated by Django 2.1.5 on 2019-03-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
    ]
