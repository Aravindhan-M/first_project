# Generated by Django 2.1.5 on 2019-02-20 04:19

from django.db import migrations
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20190219_0508'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
    ]
