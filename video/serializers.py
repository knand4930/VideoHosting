from rest_framework import serializers
from .models import Video, VideoPlaylist, VideoPlayer, ContentUnit


class VideoSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()
    embed_url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ('id', 'title', 'user_id', 'description', 'file', 'uploaded_at', 'download_url', 'embed_url')

    def get_download_url(self, obj):
        return obj.get_download_url()

    def get_embed_url(self, obj):
        return obj.get_embed_url()


class VideoPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPlaylist
        fields = ('id', 'name', 'user_id')


class VideoPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPlayer
        fields = ('id', 'user_id', 'logo', 'src', 'logoPos', 'logoUrl', 'start_muted', 'start_volume', 'monetize',
                  'name', 'width', 'height', 'ad_preload', 'ad_postload', 'autoplay', 'volume', 'fullscreen',
                  'controls',
                  'controlsBehavior', 'afterPlaylistEnd', 'playlistPlayback', 'shuffle', 'autohide_ad_controls',
                  'share')


class ContentUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentUnit
        fields = "__all__"
