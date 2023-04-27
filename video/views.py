from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import FileResponse
from django.conf import settings
from .models import Video
from .serializers import VideoSerializer


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
