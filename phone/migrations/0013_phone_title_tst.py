# Generated by Django 2.1.5 on 2019-04-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0012_country_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='title_tst',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
