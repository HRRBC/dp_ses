from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    # 1. Identificação
    registro = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=255, unique=True, verbose_name="Matrícula (código funcional)")
    nome_completo = models.CharField(max_length=255, verbose_name="Nome completo")

    # 2. Dados Profissionais
    CARGO_CHOICES = [
        ('medico', 'Médico'),
        ('analista', 'Analista em Saúde'),
        ('assistente', 'Assistente em Saúde'),
        ('auxiliar', 'Auxiliar em Saúde'),
    ]
    cargo = models.CharField(max_length=255, choices=CARGO_CHOICES, verbose_name="Cargo", default='aux_admin')
    funcao = models.CharField(max_length=255, verbose_name="Função Específica")
    numero_conselho = models.CharField(max_length=255, blank=True, null=True, verbose_name="Número do conselho profissional")
    uf_conselho = models.CharField(max_length=255, blank=True, null=True, verbose_name="UF do conselho")
    nome_conselho = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome do conselho")

    SETOR_CHOICES = [
        ('almoxarifado', 'Almoxarifado'),
        ('ambulatorio', 'Ambulatório'),
        ('bloco_cirurgico', 'Bloco Cirúrgico'),
        ('ccih', 'CCIH'),
        ('clinica_cirurgica', 'Clínica Cirúrgica'),
        ('clinica_ortopedica', 'Clínica Ortopédica'),
        ('epidemiologia', 'Epidemiologia'),
        ('farmacia', 'Farmácia'),
        ('imobilizacao', 'Imobilização'),
        ('maternidade', 'Maternidade'),
        ('recepcao', 'Recepção'),
        ('same', 'SAME'),
        ('uti', 'UTI'),
        ('dp', 'Departamento Pessoal'),
    ]
    setor_trabalho = models.CharField(max_length=255, choices=SETOR_CHOICES, verbose_name="Setor de trabalho", default='enfermaria')

    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
        ('integral', 'Integral'),
        ('diarista', 'Diarista'),
    ]
    turno = models.CharField(max_length=255, choices=TURNO_CHOICES, verbose_name="Turno", default='manha')

    dias_trabalho = models.CharField(max_length=255, verbose_name="Dias de trabalho", blank=True, null=True)
    jornada_trabalho = models.CharField(max_length=255, verbose_name="Jornada de trabalho (Ex: 8h/dia)")
    tipo_contrato = models.CharField(max_length=255, verbose_name="Tipo de contrato")

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('ferias', 'Férias'),
        ('afastado', 'Afastado'),
        ('licencan', 'Licença Nojo'),
        ('licencag', 'Licença Gala'),
        ('licencam', 'Licença Maternidade'),
        ('licencap', 'Licença Paternidade'),
        ('licencae', 'Licença Eleitoral'),
        ('licencat', 'Licença de Trato e Interesse Particular'),
        ('licencaedu', 'Licença Estudo'),
        ('licencapremio', 'Licença Prêmio'),
        ('demitido', 'Demitido'),
        ('exonerado', 'Exonerado'),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, verbose_name="Status", default='ativo')

    data_admissao = models.DateField(verbose_name="Data de admissão")

    # 3. Informações Familiares
    nome_mae = models.CharField(max_length=255, verbose_name="Nome da mãe")
    nome_pai = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome do pai")

    # 4. Dados Pessoais
    data_nascimento = models.DateField(verbose_name="Data de nascimento")
    naturalidade = models.CharField(max_length=255, verbose_name="Naturalidade (cidade/estado)")

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'),
    ]
    estado_civil = models.CharField(max_length=255, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado civil", default='solteiro')

    titulo_eleitor = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título de eleitor")
    zona_eleitoral = models.CharField(max_length=255, blank=True, null=True, verbose_name="Zona eleitoral")
    secao_eleitoral = models.CharField(max_length=255, blank=True, null=True, verbose_name="Seção eleitoral")
    estado_vota = models.CharField(max_length=255, blank=True, null=True, verbose_name="Estado onde vota")

    rg_completo = models.CharField(max_length=255, verbose_name="RG (Número e órgão emissor)")
    cpf = models.CharField(max_length=255, unique=True, verbose_name="CPF")

    numero_ctps = models.CharField(max_length=255, unique=True, verbose_name="Número da CTPS")
    serie_ctps = models.CharField(max_length=255, verbose_name="Série da CTPS")
    uf_ctps = models.CharField(max_length=255, verbose_name="UF da CTPS")

    documento_militar = models.CharField(max_length=255, blank=True, null=True, verbose_name="Documento militar")

    grau_instrucao = models.CharField(max_length=255, verbose_name="Grau de instrução")
    numero_pasep = models.CharField(max_length=255, blank=True, null=True, verbose_name="Número do PASEP")

    # 5. Contato
    celular = models.CharField(max_length=255, verbose_name="Celular")
    telefone_fixo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telefone fixo")
    email = models.EmailField(verbose_name="E-mail", unique=True)

    # 6. Endereço
    cep = models.CharField(max_length=255, verbose_name="CEP")
    endereco = models.CharField(max_length=255, verbose_name="Logradouro")
    numero = models.CharField(max_length=255, verbose_name="Número")
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=255, verbose_name="Bairro")
    cidade = models.CharField(max_length=255, verbose_name="Cidade")
    uf = models.CharField(max_length=255, verbose_name="UF")

    observacoes = models.TextField(
        max_length=10000,
        blank=True,
        null=True,
        verbose_name="Observações (informações adicionais)"
    )

    def __str__(self):
        return self.nome_completo
