# Generated by Django 2.1.5 on 2019-04-05 09:01

from django.db import migrations
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0119_auto_20190405_1159'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
    ]
