from django.test import TestCase
from django.core.exceptions import ValidationError
from .forms import UsuarioForm
from .models import Usuario
from django.db.utils import IntegrityError

class UsuarioTestCase(TestCase):
    def test_criar_usuario(self):
        usuario = Usuario.objects.create(
            nome="Dione Wisley",
            email="dione.wisley@gmail.com",
            telefone="17992745859",
            cep="01101-211",
            rua="Dione's House",
            estado="SP"
        )
        self.assertEqual(usuario.nome, "Dione Wisley")
        print('\n== TESTE/ Testando criacao de um novo usuario')

    def test_nome_obrigatorio(self):
        form_unnamed_user = UsuarioForm(data={
            "nome": "",
            "email": "dione.wisley@gmail.com",
            "telefone": "17992745859",
            "cep": "01101-211",
            "rua": "Dione's House",
            "estado": "Teste",
        })
        self.assertFalse(form_unnamed_user.is_valid())
        self.assertIn("nome", form_unnamed_user.errors)
        print('\n== TESTE/ Testando se o nome e obrigatorio no Formulario')
        
    def test_email_obrigatorio(self):
        form_no_email = UsuarioForm(data={
            'nome': 'Teste',
            'email': '',
            "telefone": "17992745859",
            'cep': '01101-211',
            'rua': "Dione's House",
            'estado': 'Teste',
        })
        self.assertFalse(form_no_email.is_valid())
        self.assertIn("email", form_no_email.errors)
        print('\n== TESTE/ Testando se o email e obrigatorio no Formulario')
        
    def test_email_unico(self):
        user1 = Usuario(nome='Teste', email='teste@gmail.com', cep='01101-211', rua='teste', estado='SP')
        user1.full_clean()
        user1.save()
        
        user2 = Usuario(nome='Teste2', email='teste@gmail.com', cep='01101-212', rua='tete', estado='DP')
        with self.assertRaises(ValidationError):
            user2.full_clean()
        print('\n== TESTE/ Testando se o email cadastrado e unico')
            
    def test_formato_email_valido(self):
        form_email_invalido = UsuarioForm(data={
            'nome': 'Teste',
            'email': 'teste.com',
            "telefone": "17992745859",
            'cep': '01101-211',
            'rua': "Dione's House",
            'estado': 'Teste',
        })
        self.assertFalse(form_email_invalido.is_valid())
        self.assertIn("email", form_email_invalido.errors)
        print('\n== TESTE/ Testando se o formato do email cadastrado e valido')
        
    def test_tamanho_campos_formulario(self):
        usuarios_caracteres_acima_100 = Usuario(
            nome="A" * 101,
            email="teste@gmail.com",
            telefone="17" * 16,
            cep="A" * 21,
            rua="A" * 101,
            estado="A" * 51, 
        )
        with self.assertRaises(ValidationError):
            usuarios_caracteres_acima_100.full_clean()
        print('\n== TESTE/ Testando se a quantidade de caracteres e valida')
