from rest_framework import viewsets
from videos.models import Video
from videos.serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """Exibir todos os videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
