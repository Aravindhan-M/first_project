# Generated by Django 2.1.5 on 2019-02-05 12:32

from django.db import migrations, models
import user.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('mobile_number', models.CharField(max_length=30, unique=True, verbose_name='mobile number')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('first_name_en', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('first_name_ar', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('last_name_en', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('last_name_ar', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff status')),
                ('role_name', models.CharField(blank=True, choices=[('AD', 'Administrator'), ('TU', 'Telecom User'), ('EU', 'End User')], default='EU', max_length=2)),
                ('accept_reject_info', models.TextField(blank=True, max_length=300, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'User',
            },
            managers=[
                ('objects', user.managers.UserManager()),
            ],
        ),
    ]
