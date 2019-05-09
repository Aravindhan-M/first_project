# Generated by Django 2.1.5 on 2019-04-03 13:44

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0008_auto_20190331_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='name_ar',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='name_en',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='name_fr',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='color_ar',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='color_en',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='color_fr',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='currency_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='currency_code_ar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='currency_code_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='currency_code_fr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='model',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='model_ar',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='model_en',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='model_fr',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='price_notes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='price_notes_ar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='price_notes_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='price_notes_fr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='product_url_ar',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='product_url_en',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='product_url_fr',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='ram',
            name='ram_ar',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ram',
            name='ram_en',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ram',
            name='ram_fr',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_ar',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_en',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_fr',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_name_ar',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_name_en',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_name_fr',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_value',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_value_ar',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_value_en',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='additionphoneattribute',
            name='attribute_value_fr',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='currency',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('DZD', 'Algerian dinar'), ('BHD', 'Bahraini dinar'), ('EGP', 'Egyptian pound'), ('IQD', 'Iraqi dinar'), ('JOD', 'Jordanian dinar'), ('KWD', 'Kuwaiti dinar'), ('LBP', 'Lebanese Pound'), ('LYD', 'Libyan dinar'), ('MAD', 'Moroccan dirham'), ('OMR', 'Omani rial'), ('ent', 'Palestine pound'), ('QAR', 'Qatari riyal'), ('SAR', 'Saudi riyal'), ('SSP', 'Sudanese pound'), ('SYP', 'Syrian pound'), ('TND', 'Tunisian dinar'), ('AED', 'United Arab Emirates dirham'), ('YER', 'Yemeni rial'), ('USD', 'United States Dollar'), ('EUR', 'Euro'), ('GBP', 'GBP')], max_length=83, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='description_ar',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='description_en',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='description_fr',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(blank=True, max_length=2050, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name_ar',
            field=models.CharField(blank=True, max_length=2050, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name_en',
            field=models.CharField(blank=True, max_length=2050, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name_fr',
            field=models.CharField(blank=True, max_length=2050, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='product_url',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(blank=True, max_length=2050, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='title',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='title_ar',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='title_en',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='title_fr',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='store',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterModelTable(
            name='additionphoneattribute',
            table='scrape_additional_attribute',
        ),
    ]
