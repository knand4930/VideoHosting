# Generated by Django 4.2 on 2023-04-28 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='videos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='player/video/logo/')),
                ('src', models.URLField(blank=True, default='127.0.0.1:8000/static/player/video/play.min.js', null=True)),
                ('logoPos', models.IntegerField(blank=True, null=True)),
                ('logoUrl', models.URLField(blank=True, null=True)),
                ('start_muted', models.BooleanField(default=False)),
                ('start_volume', models.IntegerField(blank=True, null=True)),
                ('monetize', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('ad_preload', models.BooleanField(default=False)),
                ('ad_postload', models.BooleanField(default=False)),
                ('autoplay', models.BooleanField(default=True)),
                ('volume', models.BooleanField(default=True)),
                ('fullscreen', models.BooleanField(default=True)),
                ('controls', models.BooleanField(default=True)),
                ('controlsBehavior', models.CharField(blank=True, default='visible', max_length=200, null=True)),
                ('afterPlaylistEnd', models.CharField(blank=True, default='stop', max_length=200, null=True)),
                ('playlistPlayback', models.CharField(blank=True, default='continuous', max_length=200, null=True)),
                ('shuffle', models.BooleanField(default=True)),
                ('autohide_ad_controls', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
