from django.test import TestCase
from videos.models import Video, Categoria
from videos.serializers import VideoSerializerV1, CategoriaSerializerV1

class VideoSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.video = Video(
            id = 1,
            titulo = 'Titulo de teste',
            descricao = 'Descricao de um video teste',
            url = "https://www.youtube.com/watch?v=SjDv3k3CVY4&t=389s"
        )
        self.serializer = VideoSerializerV1(instance=self.video)


    def test_verifica_campos_video_serializados(self):
        """Teste que verifica os campos que estão sendo serializados pelo modelo de video"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','titulo', 'descricao', 'url', 'categoria']))

class CategoriaSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.categoria = Categoria(
            id = 1,
            titulo = 'JUVENIL',
            cor = '#fcfc0a'
        )
        self.serializer = CategoriaSerializerV1(instance=self.categoria)

    def test_verifica_campos_categoria_serializados(self):
        """Teste que verifica os campos que estão sendo serializados pelo modelo de categoria"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'titulo', 'cor']))
        