# Generated by Django 2.1.5 on 2019-03-06 04:58

from django.db import migrations
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0069_auto_20190306_0757'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
    ]
