# Generated by Django 2.1.5 on 2019-03-04 04:56

from django.db import migrations, models
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0048_auto_20190228_1443'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='first_name_fr',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name_fr',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='last name'),
        ),
    ]
