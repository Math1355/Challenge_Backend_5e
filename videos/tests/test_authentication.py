from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCasa(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse('Videos-list')
        self.user = User.objects.create_user('teste', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um user com as credenciais corretas"""
        user = authenticate(username='teste', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.list_url)
        self.assertTrue(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_de_user_com_username_incorreto(self):
        """Teste que verifica a autenticação de um user com username incorreto"""
        user = authenticate(username='teste123', password = '123456')
        self.assertFalse((user is not None) and user.is_authenticated)