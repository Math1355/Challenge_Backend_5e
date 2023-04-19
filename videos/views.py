from rest_framework import viewsets, generics
from videos.models import Video
from videos.serializers import VideoSerializer, VideoSerializerV1


class VideoViewSet(viewsets.ModelViewSet):
    """Exibir todos os videos"""
    queryset = Video.objects.all()
    def get_serializer_class(self):
        if self.request.version == 'v1':
            return VideoSerializerV1
        else:
            return VideoSerializer
