# Generated by Django 2.1.5 on 2019-03-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adsl',
            name='benefits_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='adsl',
            name='line_type_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='adsl',
            name='monthly_payment_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='adsl',
            name='pay_type_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='adsl',
            name='payment_note_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
