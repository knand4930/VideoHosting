import uuid
from django.db import models
from main.models import User
from django.conf import settings


class VideoPlaylist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    playlist = models.ForeignKey(VideoPlaylist, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='videos/')
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/videos/{self.id}/'

    def get_download_url(self):
        return f'/videos/{self.id}/download/'

    def get_embed_url(self):
        return f'/videos/{self.id}/embed/'


class VideoPlayer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    logo = models.ImageField(upload_to="player/video/logo/", blank=True, null=True)
    src = models.URLField(blank=True, null=True, default=f'{settings.BASE_URL}/static/player/video/play.min.js')
    logoPos = models.IntegerField(blank=True, null=True)
    logoUrl = models.URLField(blank=True, null=True)
    start_muted = models.BooleanField(default=False)
    start_volume = models.IntegerField(blank=True, null=True)
    monetize = models.BooleanField(default=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(null=True, blank=True)
    ad_preload = models.BooleanField(default=False)
    ad_postload = models.BooleanField(default=False)
    autoplay = models.BooleanField(default=True)
    volume = models.BooleanField(default=True)
    fullscreen = models.BooleanField(default=True)
    controls = models.BooleanField(default=True)
    controlsBehavior = models.CharField(max_length=200, blank=True, null=True, default="visible")
    afterPlaylistEnd = models.CharField(max_length=200, blank=True, null=True, default="stop")
    playlistPlayback = models.CharField(max_length=200, blank=True, null=True, default="continuous")
    shuffle = models.BooleanField(default=True)
    autohide_ad_controls = models.BooleanField(default=True)

    def share(self):
        return f'/video/player/{self.id}/'


class ContentUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_id = models.ForeignKey(VideoPlayer, on_delete=models.CASCADE, blank=True, null=True)
    playlist_id = models.ForeignKey(VideoPlaylist, on_delete=models.CASCADE, blank=True, null=True)
