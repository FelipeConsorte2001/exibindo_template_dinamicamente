from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felipe Consorte',
            'email': 'felipeconsorte2001@gmail.com',
            'assunto': 'Email teste',
            'mensagem': 'Assunto'
        }
        self.client = Client()


    def test_from_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)


    def test_from_invalid(self):
        dados = {
            'nome': 'Felipe Consorte',
            'email': 'felipeconsorte2001@gmail.com',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
