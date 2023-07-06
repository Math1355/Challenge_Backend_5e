from rest_framework import viewsets, generics, filters
from videos.models import Video, Categoria
from videos.serializers import VideoSerializer, VideoSerializerV1, CategoriaSerializer, CategoriaSerializerV1, ListaVideosCategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class VideoViewSet(viewsets.ModelViewSet):
    """Exibir todos os videos"""
    queryset = Video.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.version == 'v1':
            return VideoSerializerV1
        else:
            return VideoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """Exibir todos os videos"""
    queryset = Categoria.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.version == 'v1':
            return CategoriaSerializerV1
        else:
            return CategoriaSerializer

class ListaCategoriasVideo(generics.ListAPIView):
    """Listando as categorias de um video"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVideosCategoriaSerializer
    