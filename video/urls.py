from django.urls import path
from .views import VideoList, VideoDetail, video_download, video_embed


urlpatterns = [
    path('video/list/', VideoList.as_view(), name='video_list'),
    path('videos/<uuid:pk>/', VideoDetail.as_view(), name='video_detail'),
    path('videos/<uuid:id>/download/', video_download, name='video_download'),
    path('videos/<uuid:id>/embed/', video_embed, name='video_embed'),
]
