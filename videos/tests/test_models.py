from django.test import TestCase
from videos.models import Categoria, Video

class CategoriaModelTestCase(TestCase):

    def setUp(self) -> None:
        self.categoria = Categoria(
            titulo = 'JUVENIL',
            cor = '#fcfc0a'
        )

    def test_verifica_atributos_da_categoria(self):
        """Teste que verifica os atributos de uma categoria de video"""
        self.assertEqual(self.categoria.titulo, 'JUVENIL')
        self.assertEqual(self.categoria.cor, '#fcfc0a')

class VideoModelTestCase(TestCase):

    def setUp(self) -> None:
        self.video = Video(
            titulo = 'Titulo de teste',
            descricao = 'Descricao de um video teste',
            url = "https://www.youtube.com/watch?v=SjDv3k3CVY4&t=389s",
        )
        self.categoria = Categoria(
            id = 2,
            titulo = 'JUVENIL',
            cor = '#fcfc0a'
        )
    
    def teste_verifica_atributos_do_video(self):
        """Teste que verifica os atributos de um video"""
        self.assertEqual(self.video.titulo, 'Titulo de teste')
        self.assertEqual(self.video.descricao, 'Descricao de um video teste')
        self.assertEqual(self.categoria.id, 2)