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

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        position_serializer = PlayerPositionSerializer(data=position_data)
        position_serializer.is_valid(raise_exception=True)
        position = position_serializer.save()
        player_size = PlayerSize.objects.create(position=position, **validated_data)
        return player_size

    def update(self, instance, validated_data):
        position_data = validated_data.pop('position')
        position = instance.position

        # Update the nested object
        for attr, value in position_data.items():
            setattr(position, attr, value)
        position.save()

        # Update the parent object
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class MobilePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePosition
        fields = "__all__"


class MobileSizeSerializer(serializers.ModelSerializer):
    position = MobilePositionSerializer()

    class Meta:
        model = MobileSize
        fields = "__all__"

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        position = MobilePosition.objects.create(**position_data)
        mobile_size = MobileSize.objects.create(position=position, **validated_data)
        return mobile_size

    def update(self, instance, validated_data):
        position_data = validated_data.pop('position', None)
        if position_data is not None:
            position_serializer = MobilePositionSerializer(instance.position, data=position_data)
            position_serializer.is_valid(raise_exception=True)
            position = position_serializer.save()
            validated_data['position'] = position
        return super().update(instance, validated_data)


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

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        playerSize_data = validated_data.pop('playerSize')
        position_serializer = StickyPositionSerializer(data=position_data)
        playerSize_serializer = StickyPlayerSerializer(data=playerSize_data)
        if position_serializer.is_valid() and playerSize_serializer.is_valid():
            position = position_serializer.save()
            playerSize = playerSize_serializer.save()
            sticky = Sticky.objects.create(position=position, playerSize=playerSize, **validated_data)
            return sticky
        else:
            raise serializers.ValidationError("Error creating sticky.")

    def update(self, instance, validated_data):
        position_data = validated_data.pop('position')
        playerSize_data = validated_data.pop('playerSize')
        position_serializer = StickyPositionSerializer(instance.position, data=position_data)
        playerSize_serializer = StickyPlayerSerializer(instance.playerSize, data=playerSize_data)

        if position_serializer.is_valid() and playerSize_serializer.is_valid():
            position = position_serializer.save()
            playerSize = playerSize_serializer.save()
            instance.position = position
            instance.playerSize = playerSize
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("Error updating sticky.")


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

    def create(self, validated_data):
        player_size_data = validated_data.pop('playerSize')
        mobile_size_data = validated_data.pop('mobileSize')

        player_size = PlayerSizeSerializer().create(validated_data=player_size_data)
        mobile_size = MobileSizeSerializer().create(validated_data=mobile_size_data)

        general_settings = generalSettings.objects.create(playerSize=player_size, mobileSize=mobile_size,
                                                          **validated_data)
        return general_settings

    def update(self, instance, validated_data):
        # Retrieve the nested serializer instances from the validated data
        player_size_serializer = PlayerSizeSerializer(instance=instance.playerSize,
                                                      data=validated_data.pop('playerSize', {}))
        mobile_size_serializer = MobileSizeSerializer(instance=instance.mobileSize,
                                                      data=validated_data.pop('mobileSize', {}))

        # Validate and save the nested serializer instances
        if player_size_serializer.is_valid():
            player_size_serializer.save()
        if mobile_size_serializer.is_valid():
            mobile_size_serializer.save()

        # Update the instance with the validated data
        return super().update(instance, validated_data)


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

    def update(self, instance, validated_data):
        general_settings_data = validated_data.pop('generalSettings', None)
        ad_unit_data = validated_data.pop('adUnit', None)
        sticky_data = validated_data.pop('sticky', None)

        if general_settings_data:
            general_settings_serializer = generalSettingsSerializer(instance=instance.generalSettings,
                                                                    data=general_settings_data)
            general_settings_serializer.is_valid(raise_exception=True)
            general_settings_serializer.save()

        if ad_unit_data:
            ad_unit_serializer = adUnitSerializer(instance=instance.adUnit, data=ad_unit_data)
            ad_unit_serializer.is_valid(raise_exception=True)
            ad_unit_serializer.save()

        if sticky_data:
            sticky_serializer = StickySerializer(instance=instance.sticky, data=sticky_data)
            sticky_serializer.is_valid(raise_exception=True)
            sticky_serializer.save()

        return super().update(instance, validated_data)
