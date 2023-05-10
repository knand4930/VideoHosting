from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Video)
admin.site.register(VideoPlaylist)
admin.site.register(VideoPlayer)
admin.site.register(ContentUnit)

"""
Video Player Details 
"""

admin.site.register(PlayerPosition)
admin.site.register(PlayerSize)
admin.site.register(MobilePosition)
admin.site.register(MobileSize)
admin.site.register(StickyPosition)
admin.site.register(StickyPlayer)
admin.site.register(Sticky)
admin.site.register(adUnit)
admin.site.register(generalSettings)
admin.site.register(UserSettings)