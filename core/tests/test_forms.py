from core.forms import ContatoForm
from django.test import TestCase

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felipe'
        self.email = 'cfelipeconsorte@gmail.com'
        self.assunto = 'Um assunto'
        self.mensagem = 'Uma menssagem'

        self.dados ={
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)


    def test_from(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
