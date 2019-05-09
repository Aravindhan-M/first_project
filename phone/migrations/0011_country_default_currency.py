# Generated by Django 2.1.5 on 2019-04-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0010_phonecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='default_currency',
            field=models.CharField(choices=[('DZD', 'Algerian dinar'), ('BHD', 'Bahraini dinar'), ('EGP', 'Egyptian pound'), ('IQD', 'Iraqi dinar'), ('JOD', 'Jordanian dinar'), ('KWD', 'Kuwaiti dinar'), ('LBP', 'Lebanese Pound'), ('LYD', 'Libyan dinar'), ('MAD', 'Moroccan dirham'), ('OMR', 'Omani rial'), ('ent', 'Palestine pound'), ('QAR', 'Qatari riyal'), ('SAR', 'Saudi riyal'), ('SSP', 'Sudanese pound'), ('SYP', 'Syrian pound'), ('TND', 'Tunisian dinar'), ('AED', 'United Arab Emirates dirham'), ('YER', 'Yemeni rial'), ('USD', 'United States Dollar'), ('EUR', 'Euro'), ('GBP', 'GBP')], max_length=20, null=True, verbose_name='Default Currency'),
        ),
    ]
