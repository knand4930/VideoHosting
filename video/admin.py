from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Video)
admin.site.register(VideoPlaylist)
admin.site.register(VideoPlayer)