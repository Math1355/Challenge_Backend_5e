from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, force_authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class TestsConexaoVideo(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('video/', include('setup.urls'))
    ]

    def test_criar_conexao_video(self):
        """Teste que verifica uma conexão para ver os videos"""
        user = authenticate(username='math', password='120518')
        if user is not None:
            url = reverse('Videos-list')
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestsConexaocategoria(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('video/', include('setup.urls'))
    ]
    
    def test_criar_conexao_video(self):
        """Teste que verifica uma conexão para ver os videos"""
        user = authenticate(username='math', password='120518')
        if user is not None:
            url = reverse('Categorias-list')
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

