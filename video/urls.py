from django.urls import path
from .views import VideoList, VideoDetail, video_download, video_embed, VideoPlaylistListAPI, VideoPlaylistUpdateDelete, \
    home, VideoPlayerListCreate, VideoPlayerUpdateDelete, VideoPlayerGet, VideoGet, ContentUnitListAPI, \
    ContentUnitDeleteUpdateAPI, ContentUnitGet, VidoPlayListFilterAPI, PlayListFilterAPI, UserSettingsAPIView

urlpatterns = [
    path('video/list/', VideoList.as_view(), name='video_list'),
    path('videos/<uuid:pk>/', VideoDetail.as_view(), name='video_detail'),
    path('video/playlist/filter/api/<int:id>/',PlayListFilterAPI.as_view(), name='PlayListFilterAPI'),

    path('videos/<uuid:id>/download/', video_download, name='video_download'),
    path('videos/<uuid:id>/embed/', video_embed, name='video_embed'),
    path('video/get/<uuid:id>/', VideoGet.as_view(), name='VideoGet'),

    path('video/playlist/', VideoPlaylistListAPI.as_view(), name='VideoListAPI'),
    path('video/playlist/update/delete/<int:pk>/', VideoPlaylistUpdateDelete.as_view(), name='VideoPlaylistUpdateDelete'),
    path('video/playlist/filter/', VidoPlayListFilterAPI.as_view(),name='VidoPlayListFilterAPI'),


    path('video/player/list/create', VideoPlayerListCreate.as_view(), name='VideoPlayerListCreate'),
    path('video/player/update/delete/<int:pk>/', VideoPlayerUpdateDelete.as_view(), name='VideoPlayerUpdateDelete'),
    path('video/player/get/<uuid:id>/', VideoPlayerGet.as_view(), name='VideoPlayerFilterAPI'),
    path('video/player/update/delete/<uuid:pk>/', VideoPlayerUpdateDelete.as_view(), name='VideoPlayerUpdateDelete'),

    # path('testing', home, name='home')

    path('content/unit/list/create/', ContentUnitListAPI.as_view(), name='ContentUnitListAPI'),
    path('content/unit/update/delete/<uuid:pk>', ContentUnitDeleteUpdateAPI.as_view(), name='ContentUnitDeleteUpdateAPI'),
    path('content/unit/get/<uuid:id>/', ContentUnitGet.as_view(), name='ContentUnitGet'),

    path('user_settings/', UserSettingsAPIView.as_view()),
]
