# Generated by Django 2.1.5 on 2019-04-16 06:50

from django.db import migrations
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0130_auto_20190412_1441'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
    ]
