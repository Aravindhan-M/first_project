# Generated by Django 2.1.5 on 2019-02-20 14:14

from django.db import migrations
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20190220_1407'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
    ]
