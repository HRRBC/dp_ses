from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    # 1. Identificação
    registro = models.AutoField(primary_key=True)
    # Matrícula: Tornada obrigatória e única, como esperado para um código funcional
    matricula = models.CharField(max_length=50, unique=True, verbose_name="Matrícula (código funcional)")
    # Nome completo: Tornada obrigatória e sem default para novos registros
    nome_completo = models.CharField(max_length=150, verbose_name="Nome completo")

    # 2. Dados Profissionais
    CARGO_CHOICES = [
        ('medico', 'Médico'),
        ('enfermeiro', 'Enfermeiro'),
        ('tec_enfermagem', 'Técnico de Enfermagem'),
        ('aux_admin', 'Auxiliar Administrativo'),
        ('coordenador', 'Coordenador'), # Adicionado
        ('gerente', 'Gerente'),       # Adicionado
        # adicione outros cargos necessários conforme seus formulários
    ]
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES, verbose_name="Cargo", default='aux_admin')
    # Função: Tornada obrigatória e sem default
    funcao = models.CharField(max_length=100, verbose_name="Função Específica") # Verbose_name mais descritivo
    numero_conselho = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número do conselho profissional")
    uf_conselho = models.CharField(max_length=2, blank=True, null=True, verbose_name="UF do conselho")
    nome_conselho = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome do conselho")
    
    SETOR_CHOICES = [
        ('emergencia', 'Emergência'),
        ('uti', 'UTI'),
        ('enfermaria', 'Enfermaria'),
        ('administrativo', 'Administrativo'),
        ('cozinha', 'Cozinha'),
        ('higienizacao', 'Higienização'),
        ('farmacia', 'Farmácia'), # Corrigido para minúsculas e adicionado
        # adicione outros setores necessários
    ]
    setor_trabalho = models.CharField(
        max_length=100,
        choices=SETOR_CHOICES,
        verbose_name="Setor de trabalho",
        default='enfermaria'
    )
    
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
        ('integral', 'Integral'), # Adicionado
    ]
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES, verbose_name="Turno", default='manha')
    
    dias_trabalho = models.CharField(max_length=100, verbose_name="Dias de trabalho", blank=True, null=True)
    # Jornada de trabalho: Tornada obrigatória e sem default
    jornada_trabalho = models.CharField(max_length=100, verbose_name="Jornada de trabalho (Ex: 8h/dia)")
    # Tipo de contrato: Tornada obrigatória e sem default
    tipo_contrato = models.CharField(max_length=100, verbose_name="Tipo de contrato")

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('ferias', 'Férias'),      # Adicionado!
        ('afastado', 'Afastado'),  # Adicionado!
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status", default='ativo')

    # Data de admissão: Removido default=timezone.now para ser preenchida manualmente
    data_admissao = models.DateField(verbose_name="Data de admissão")

    # 3. Informações Familiares
    # Nome da mãe: Tornada obrigatória e sem default
    nome_mae = models.CharField(max_length=150, verbose_name="Nome da mãe")
    nome_pai = models.CharField(max_length=150, blank=True, null=True, verbose_name="Nome do pai")

    # 4. Dados Pessoais
    # Data de nascimento: Removido default=timezone.now para ser preenchida manualmente
    data_nascimento = models.DateField(verbose_name="Data de nascimento")
    # Naturalidade: Tornada obrigatória e sem default
    naturalidade = models.CharField(max_length=100, verbose_name="Naturalidade (cidade/estado)")

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'), # Adicionado
    ]
    # Aumentei max_length para acomodar 'uniao_estavel'
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado civil", default='solteiro')

    titulo_eleitor = models.CharField(max_length=20, blank=True, null=True, verbose_name="Título de eleitor")
    zona_eleitoral = models.CharField(max_length=10, blank=True, null=True, verbose_name="Zona eleitoral")
    secao_eleitoral = models.CharField(max_length=10, blank=True, null=True, verbose_name="Seção eleitoral")
    estado_vota = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado onde vota")

    # RG completo: Tornada obrigatória e sem default
    rg_completo = models.CharField(max_length=50, verbose_name="RG (Número e órgão emissor)")
    # CPF: Tornada obrigatória e única
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")

    # Número da CTPS: Tornada obrigatória e única
    numero_ctps = models.CharField(max_length=20, unique=True, verbose_name="Número da CTPS")
    # Série da CTPS: Tornada obrigatória e sem default
    serie_ctps = models.CharField(max_length=20, verbose_name="Série da CTPS")
    # UF da CTPS: Tornada obrigatória e sem default
    uf_ctps = models.CharField(max_length=2, verbose_name="UF da CTPS")

    documento_militar = models.CharField(max_length=50, blank=True, null=True, verbose_name="Documento militar")

    # Grau de instrução: Tornada obrigatória e sem default
    grau_instrucao = models.CharField(max_length=50, verbose_name="Grau de instrução")

    numero_pasep = models.CharField(max_length=30, blank=True, null=True, verbose_name="Número do PASEP")

    # 5. Contato
    # Celular: Tornada obrigatória e sem default
    celular = models.CharField(max_length=20, verbose_name="Celular")
    telefone_fixo = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone fixo")
    # E-mail: Tornada obrigatória e única
    email = models.EmailField(verbose_name="E-mail", unique=True)

    # 6. Endereço
    # CEP: Tornada obrigatória e sem default
    cep = models.CharField(max_length=10, verbose_name="CEP")
    # Endereço: Tornada obrigatória e sem default
    endereco = models.CharField(max_length=150, verbose_name="Logradouro")
    # Número: Tornada obrigatória e sem default
    numero = models.CharField(max_length=10, verbose_name="Número")
    # NOVO CAMPO: Complemento (existente em HTML, adicionado aqui)
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    # Bairro: Tornada obrigatória e sem default
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    # Cidade: Tornada obrigatória e sem default
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    # UF: Tornada obrigatória e sem default
    uf = models.CharField(max_length=2, verbose_name="UF")

    # NOVO CAMPO: Observações
    observacoes = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True, 
        verbose_name="Observações (informações adicionais)"
    )

    def __str__(self):
        return self.nome_completo