# Generated by Django 2.1.5 on 2019-03-04 11:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0005_country_allowed_laguages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='allowed_laguages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('en', 'English'), ('ar', 'Arabic'), ('fr', 'French')], max_length=8, null=True),
        ),
    ]
