from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import CreateDocument as CreateDocumentView
import json
import os


# Create your tests here.

# ViewTests
class SimpleTest(TestCase):
    
    # Inicia as variaveis como usuario, autenticacao do token e factory das requests
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='joao', password='TestPassword')
        res = self.client.post("/login/", {"username": "joao", "password": "TestPassword"})
        res_json = json.loads(res.content.decode('utf-8'))
        self.token = res_json["access"]

    # Testa se ao nao passar os parametros nao cria o documento
    def test_document_cannot_created_with_no_data(self):        
        request = self.factory.post('/document/create/', {}, HTTP_AUTHORIZATION='Bearer {}'.format(self.token))        
        response = CreateDocumentView.as_view()(request)
        self.assertEqual(response.status_code, 400)

    # Testa se cria o documento com requisicao correta
    def test_document_cannot_created_with_no_data(self):        
        request = self.factory.post('/document/create/', {"nome":"Augusto Teste","data":"10/10/1990","cpf":"000.111.222-33","rg":"12345678"}, HTTP_AUTHORIZATION='Bearer {}'.format(self.token))        
        response = CreateDocumentView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        # Remove o arquivo criado pelo teste
        os.remove('cadastro.txt')

    # Testa se ao nao passar o Token nao cria documento
    def test_no_authorized_without_token(self):
        request = self.factory.post('/document/create/', {"nome":"Augusto Teste","data":"10/10/1990","cpf":"000.111.222-33","rg":"12345678"})        
        response = CreateDocumentView.as_view()(request)
        self.assertEqual(response.status_code, 401)
