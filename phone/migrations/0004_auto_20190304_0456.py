# Generated by Django 2.1.5 on 2019-03-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_auto_20190226_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionphoneattribute',
            name='attribute_name_fr',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='additionphoneattribute',
            name='attribute_value_fr',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='description_fr',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='name_fr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='title_fr',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='bluetooth_fr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='color_fr',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='display_color_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='display_size_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='generation_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='max_memory_card_fr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='max_memory_card_size_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='music_playback_time_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='pixel_density_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='processor_fr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='ram_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='resolution_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='sim_size_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='sim_slot_fr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='standby_talk_time_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='tracking_system_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='usb_connectivity_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='video_playback_time_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='volte_fr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='phoneattribute',
            name='wifi_features_fr',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
