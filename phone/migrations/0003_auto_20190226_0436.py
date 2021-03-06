# Generated by Django 2.1.5 on 2019-02-26 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_auto_20190225_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='phone.Phone'),
        ),
        migrations.AlterField(
            model_name='color',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='phone.Phone'),
        ),
        migrations.AlterField(
            model_name='image',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='phone.Phone'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rams', to='phone.Phone'),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='phone.Phone'),
        ),
    ]
