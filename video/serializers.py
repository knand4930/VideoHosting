from rest_framework import serializers
from .models import Video, VideoPlaylist, VideoPlayer


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
        fields = ('id', 'name', 'video', 'user_id')


class VideoPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPlayer
        fields = "__all__"
