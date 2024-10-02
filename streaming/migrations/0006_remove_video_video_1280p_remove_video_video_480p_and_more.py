# Generated by Django 5.1.1 on 2024-10-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0005_remove_video_hls_path_video_video_1280p_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_1280p',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_480p',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_720p',
        ),
        migrations.AddField(
            model_name='video',
            name='hls_playlist',
            field=models.URLField(blank=True, null=True),
        ),
    ]
