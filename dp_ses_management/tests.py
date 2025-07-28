from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from dp_ses_management.models import Colaborador # Importa o modelo Colaborador

class CadastroColaboradorTestCase(TestCase):
    def setUp(self):
        # Cria um usuário para login
        self.user = User.objects.create_user(username='testeuser', password='senha123')
        self.client = Client()
        # Assumindo que o namespace é 'tarefas' e o nome da URL é 'cadastrar_colaborador'
        self.url = reverse('tarefas:cadastrar_colaborador')

    def test_cadastro_colaborador_valido(self):
        # Garante que o usuário está logado para acessar a view
        self.client.login(username='testeuser', password='senha123')

        # Dados de teste para um colaborador válido
        # Ajustados conforme as últimas mudanças no models.py e views.py
        dados = {
            # 'registro' é AutoField (PK), não deve ser enviado no POST de cadastro
            'matricula': '123456',
            'nome_completo': 'João da Silva Teste', # Nome ligeiramente diferente para evitar conflitos se você testar manualmente
            'cargo': 'medico', # Chave exata do CHOICE
            'funcao': 'Cardiologista Intervencionista',
            'numero_conselho': 'CRM12345',
            'uf_conselho': 'PE',
            'nome_conselho': 'CRM',
            'setor_trabalho': 'uti', # Chave exata do CHOICE (minúsculas)
            'turno': 'manha', # Chave exata do CHOICE
            'dias_trabalho': 'Seg-Sex',
            'jornada_trabalho': '40h semanais',
            'tipo_contrato': 'CLT',
            'status': 'ativo', # Chave exata do CHOICE
            'data_admissao': '2022-01-01', # Formato YYYY-MM-DD para DateField

            'nome_mae': 'Maria da Silva Teste',
            'nome_pai': 'José da Silva Teste', # Opcional, pode ser vazio ou None

            'data_nascimento': '1990-05-15', # Formato YYYY-MM-DD
            'naturalidade': 'Serra Talhada/PE',
            'estado_civil': 'solteiro', # Chave exata do CHOICE
            'titulo_eleitor': '123456789012', # Corrigido para 'titulo_eleitor'
            'zona_eleitoral': '012',
            'secao_eleitoral': '034',
            'estado_vota': 'PE',
            'rg_completo': '12345678 SSP-PE',
            'cpf': '12345678901', # Sem máscara para corresponder à limpeza na view
            'numero_ctps': '9876543',
            'serie_ctps': '1234',
            'uf_ctps': 'PE',
            'documento_militar': '', # Opcional
            'grau_instrucao': 'Ensino Superior Completo',
            'numero_pasep': '123456789012', # Opcional, sem máscara

            'celular': '87999999999', # Sem máscara
            'telefone_fixo': '', # Opcional, sem máscara
            'email': 'joao.teste@example.com', # Deve ser único

            'cep': '56900000', # Sem máscara
            'endereco': 'Rua de Teste, 123',
            'numero': '123',
            'complemento': 'Apto 101', # NOVO CAMPO: Adicionado ao teste
            'bairro': 'Centro Teste',
            'cidade': 'Serra Talhada',
            'uf': 'PE',
            'observacoes': 'Este é um teste de observação de até 1000 caracteres.', # NOVO CAMPO: Adicionado ao teste
        }

        resposta = self.client.post(self.url, dados)

        # Verifica se houve redirecionamento (código 302 para sucesso)
        self.assertEqual(resposta.status_code, 302, f"Status code não é 302. Resposta: {resposta.content}")

        # Verifica se um novo colaborador foi criado no banco de dados
        self.assertEqual(Colaborador.objects.count(), 1)

        # Recupera o colaborador criado e verifica alguns campos
        colaborador_salvo = Colaborador.objects.first()
        self.assertEqual(colaborador_salvo.nome_completo, dados['nome_completo'])
        self.assertEqual(colaborador_salvo.matricula, dados['matricula'])
        self.assertEqual(colaborador_salvo.cargo, dados['cargo'])
        self.assertEqual(colaborador_salvo.setor_trabalho, dados['setor_trabalho'])
        self.assertEqual(colaborador_salvo.email, dados['email'])
        self.assertEqual(colaborador_salvo.observacoes, dados['observacoes']) # Verifica o novo campo

        # Teste para dados inválidos (ex: matrícula duplicada)
    def test_cadastro_colaborador_matricula_duplicada(self):
        self.client.login(username='testeuser', password='senha123')

        # Cria um primeiro colaborador
        Colaborador.objects.create(
            matricula='duplicado', nome_completo='Colaborador A', cargo='aux_admin', funcao='Auxiliar',
            setor_trabalho='administrativo', turno='manha', dias_trabalho='Seg-Sex', jornada_trabalho='8h',
            tipo_contrato='CLT', status='ativo', data_admissao='2020-01-01', nome_mae='Mae A',
            data_nascimento='1980-01-01', naturalidade='Cidade A', estado_civil='solteiro',
            rg_completo='12345 RG', cpf='00000000000', numero_ctps='1234567', serie_ctps='123', uf_ctps='SP',
            celular='11987654321', email='a@example.com', cep='11111111', endereco='Rua A', numero='1',
            bairro='Bairro A', cidade='Cidade A', uf='SP', observacoes=''
        )
        
    

        resposta = self.client.post(self.url, dados_duplicados)
        
        # Com o `try...except` na view, o Django não lança um 500, mas redireciona para a mesma página
        # com a mensagem de erro. O count ainda deve ser 1.
        self.assertEqual(resposta.status_code, 200) # Deverá retornar 200 (OK) pois renderiza o mesmo formulário
        self.assertIn(b'Erro ao cadastrar colaborador:', resposta.content) # Verifica se a mensagem de erro está presente
        self.assertEqual(Colaborador.objects.count(), 1) # Apenas o primeiro colaborador deve ter sido salvo

    # Teste para acesso não-logado
    def test_cadastro_colaborador_nao_logado(self):
        resposta = self.client.post(self.url, {}) # Tenta POST sem login
        self.assertEqual(resposta.status_code, 302) # Deve redirecionar para a página de login
        self.assertIn(reverse('tarefas:login'), resposta.url) # Verifica se redirecionou para o login
        self.assertEqual(Colaborador.objects.count(), 0) # Nenhum colaborador deve ser salvo