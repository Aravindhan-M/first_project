# Generated by Django 2.1.5 on 2019-03-06 14:20

from django.db import migrations, models
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0071_auto_20190306_0759'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name_ar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name_en',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name_fr',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name_ar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name_en',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name_fr',
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False, verbose_name='Email Verified Status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_phone_verified',
            field=models.BooleanField(default=False, verbose_name='Mobile Verified Status'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='user',
            name='name_ar',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='user',
            name='name_en',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='user',
            name='name_fr',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(max_length=30, unique=True, verbose_name='Mobile number'),
        ),
    ]
