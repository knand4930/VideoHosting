from django.urls import path
from .views import VideoList, VideoDetail, video_download, video_embed, VideoPlaylistListAPI, VideoPlaylistUpdateDelete, \
    home, VideoPlayerListCreate, VideoPlayerUpdateDelete


urlpatterns = [
    path('video/list/', VideoList.as_view(), name='video_list'),
    path('videos/<uuid:pk>/', VideoDetail.as_view(), name='video_detail'),

    path('videos/<uuid:id>/download/', video_download, name='video_download'),
    path('videos/<uuid:id>/embed/', video_embed, name='video_embed'),

    path('video/playlist/', VideoPlaylistListAPI.as_view(), name='VideoListAPI'),
    path('video/playlist/update/delete/<int:pk>/', VideoPlaylistUpdateDelete.as_view(), name='VideoPlaylistUpdateDelete'),

    path('video/player/list/create', VideoPlayerListCreate.as_view(), name='VideoPlayerListCreate'),
    path('video/player/update/delete/<uuid:pk>/', VideoPlayerUpdateDelete.as_view(), name='VideoPlayerUpdateDelete'),

    # path('testing', home, name='home')
]
