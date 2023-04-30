import os

import django_filters
from django.shortcuts import render
from django_filters import UUIDFilter
from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import FileResponse
from django.conf import settings
from rest_framework.views import APIView

from .models import Video, VideoPlayer, VideoPlaylist, ContentUnit
from .serializers import VideoSerializer, VideoPlaylistSerializer, VideoPlayerSerializer, ContentUnitSerializer
from django_filters.rest_framework import DjangoFilterBackend


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(uploaded_by=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def video_download(request, id):
    video = Video.objects.get(id=id)
    response = FileResponse(video.file, as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{video.file.name}"'
    return response


@api_view(['GET'])
def video_embed(request, id):
    video = Video.objects.get(id=id)
    embed_code = f'<iframe src="{request.build_absolute_uri(video.get_download_url())}" width="640" height="360"></iframe>'
    return Response({'embed_code': embed_code})


class VideoPlaylistListAPI(generics.ListCreateAPIView):
    queryset = VideoPlaylist.objects.all()
    serializer_class = VideoPlaylistSerializer

    def post(self, request, format=None):
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoPlaylistUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoPlaylist.objects.all()
    serializer_class = VideoPlaylistSerializer


class VideoPlayerListCreate(generics.ListCreateAPIView):
    queryset = VideoPlayer.objects.all()
    serializer_class = VideoPlayerSerializer


class VideoPlayerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoPlayer.objects.all()
    serializer_class = VideoPlayerSerializer


def home(request):
    path = f'{settings.BASE_URL}/static/player/video/play.min.js'
    print(path)
    return render(request, 'home.html', {'path': path})


class VidoPlayListFilter(django_filters.Filter):
    id = UUIDFilter(field_name='id')

    class Meta:
        model = VideoPlaylist
        fields = ['id']


class VidoPlayListFilterAPI(generics.ListAPIView):
    queryset = VideoPlaylist.objects.all()
    serializer_class = VideoPlaylistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = VidoPlayListFilter


class VideoPlayerGet(APIView):
    def get(self, request, id, format=None, *args, **kwargs):
        data = get_object_or_404(VideoPlayer, id=id)
        serializer = VideoPlayerSerializer(data)
        return Response(serializer.data)


class VideoGet(APIView):
    def get(self, request, id, format=None, *args, **kwargs):
        data = get_object_or_404(Video, id=id)
        serializer = VideoSerializer(data)
        return Response(serializer.data)


class ContentUnitListAPI(generics.ListCreateAPIView):
    queryset = ContentUnit.objects.all()
    serializer_class = ContentUnitSerializer


class ContentUnitDeleteUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentUnit.objects.all()
    serializer_class = ContentUnitSerializer


class ContentUnitGet(APIView):
    def get(self, request, id, format=None, *args, **kwargs):
        data = get_object_or_404(ContentUnit, id=id)
        serializer = ContentUnitSerializer(data)
        return Response(serializer.data)


class PlayListFilterAPI(APIView):
    def get(self, request, id, format=None, *args, **kwargs):
        playlist = VideoPlaylist.objects.get(id=id)
        value = Video.objects.filter(playlist=playlist)
        serializer = VideoSerializer(value, many=True)
        return Response(serializer.data)
