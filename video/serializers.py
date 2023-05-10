from rest_framework import serializers
from .models import Video, VideoPlaylist, VideoPlayer, ContentUnit, PlayerPosition, PlayerSize, MobilePosition, \
    MobileSize, StickyPosition, Sticky, adUnit, generalSettings, UserSettings, StickyPlayer


class VideoSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()
    embed_url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = (
            'id', 'title', 'playlist', 'user_id', 'description', 'file', 'uploaded_at', 'download_url', 'embed_url')

    def get_download_url(self, obj):
        return obj.get_download_url()

    def get_embed_url(self, obj):
        return obj.get_embed_url()


class VideoPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPlaylist
        fields = ('id', 'name', 'user_id', 'video_id')


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


"""
Video Player Unit

"""


class PlayerPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPosition
        fields = "__all__"


class PlayerSizeSerializer(serializers.ModelSerializer):
    position = PlayerPositionSerializer()

    class Meta:
        model = PlayerSize
        fields = "__all__"


class MobilePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePosition
        fields = "__all__"


class MobileSizeSerializer(serializers.ModelSerializer):
    position = MobilePositionSerializer()

    class Meta:
        model = MobileSize
        fields = "__all__"


class StickyPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickyPosition
        fields = "__all__"


class StickyPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickyPlayer
        fields = "__all__"


class StickySerializer(serializers.ModelSerializer):
    position = StickyPositionSerializer()
    playerSize = StickyPlayerSerializer()

    class Meta:
        model = Sticky
        fields = "__all__"


class adUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = adUnit
        fields = "__all__"


class generalSettingsSerializer(serializers.ModelSerializer):
    playerSize = PlayerSizeSerializer()
    mobileSize = MobileSizeSerializer()

    class Meta:
        model = generalSettings
        fields = "__all__"


class UserSettingsSerializer(serializers.ModelSerializer):
    generalSettings = generalSettingsSerializer()
    adUnit = adUnitSerializer()
    sticky = StickySerializer()

    class Meta:
        model = UserSettings
        fields = "__all__"

    def create(self, validated_data):
        generalSettings_data = validated_data.pop('generalSettings')
        adUnit_data = validated_data.pop('adUnit')
        sticky_data = validated_data.pop('sticky')

        # Create nested objects using the serializer's create() method
        generalSettings = generalSettingsSerializer().create(validated_data=generalSettings_data)
        adUnit = adUnitSerializer().create(validated_data=adUnit_data)
        sticky = StickySerializer().create(validated_data=sticky_data)

        # Create the UserSettings object with the nested objects
        user_settings = UserSettings.objects.create(generalSettings=generalSettings, adUnit=adUnit, sticky=sticky,
                                                    **validated_data)
        return user_settings