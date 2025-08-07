from django.db import models

class Colaborador(models.Model):
    # 1. Identificação
    registro = models.AutoField(primary_key=True)
    # A matrícula deve continuar sendo única para cada VÍNCULO de trabalho
    matricula = models.CharField(max_length=255, unique=True, verbose_name="Matrícula (código funcional)", blank=True, null=True)
    nome_completo = models.CharField(max_length=255, verbose_name="Nome completo", blank=True, null=True)

    # 2. Dados Profissionais
    CARGO_CHOICES = [
        ('medico', 'Médico'),
        ('analista', 'Analista em Saúde'),
        ('assistente', 'Assistente em Saúde'),
        ('auxiliar', 'Auxiliar em Saúde'),
    ]
    cargo = models.CharField(max_length=255, choices=CARGO_CHOICES, verbose_name="Cargo", default='aux_admin', blank=True, null=True)
    funcao = models.CharField(max_length=255, verbose_name="Função Específica", blank=True, null=True)
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
        ('plantonista', 'Plantonista'),
        ('evolucionista', 'Evolucionista'),
    ]
    setor_trabalho = models.CharField(max_length=255, choices=SETOR_CHOICES, verbose_name="Setor de trabalho", default='enfermaria', blank=True, null=True)

    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
        ('integral', 'Integral'),
        ('diarista', 'Diarista'),
        ('segunda', 'Segunda-Feira'),
        ('terca', 'Terça-Feira'),
        ('quarta', 'Quarta-Feira'),
        ('quinta', 'Quinta-Feira'),
        ('sexta', 'Sexta-Feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    turno = models.CharField(max_length=255, choices=TURNO_CHOICES, verbose_name="Turno", default='manha', blank=True, null=True)

    dias_trabalho = models.CharField(max_length=255, verbose_name="Dias de trabalho", blank=True, null=True)
    jornada_trabalho = models.CharField(max_length=255, verbose_name="Jornada de trabalho (Ex: 8h/dia)", blank=True, null=True)
    tipo_contrato = models.CharField(max_length=255, verbose_name="Tipo de contrato", blank=True, null=True)

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
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, verbose_name="Status", default='ativo', blank=True, null=True)
    data_admissao = models.DateField(verbose_name="Data de admissão", blank=True, null=True)

    # 3. Informações Familiares
    nome_mae = models.CharField(max_length=255, verbose_name="Nome da mãe", blank=True, null=True)
    nome_pai = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome do pai")

    # 4. Dados Pessoais
    data_nascimento = models.DateField(verbose_name="Data de nascimento", blank=True, null=True)
    naturalidade = models.CharField(max_length=255, verbose_name="Naturalidade (cidade/estado)", blank=True, null=True)

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'),
    ]
    estado_civil = models.CharField(max_length=255, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado civil", default='solteiro', blank=True, null=True)

    titulo_eleitor = models.CharField(max_length=255, blank=True, null=True, verbose_name="Título de eleitor")
    zona_eleitoral = models.CharField(max_length=255, blank=True, null=True, verbose_name="Zona eleitoral")
    secao_eleitoral = models.CharField(max_length=255, blank=True, null=True, verbose_name="Seção eleitoral")
    estado_vota = models.CharField(max_length=255, blank=True, null=True, verbose_name="Estado onde vota")

    rg_completo = models.CharField(max_length=255, verbose_name="RG (Número e órgão emissor)", blank=True, null=True)
    # CPF não é mais único para permitir múltiplos vínculos
    cpf = models.CharField(max_length=255, verbose_name="CPF", blank=True, null=True)

    # Número da CTPS não é mais único para permitir múltiplos vínculos
    numero_ctps = models.CharField(max_length=255, verbose_name="Número da CTPS", blank=True, null=True)
    serie_ctps = models.CharField(max_length=255, verbose_name="Série da CTPS", blank=True, null=True)
    uf_ctps = models.CharField(max_length=255, verbose_name="UF da CTPS", blank=True, null=True)

    documento_militar = models.CharField(max_length=255, blank=True, null=True, verbose_name="Documento militar")

    grau_instrucao = models.CharField(max_length=255, verbose_name="Grau de instrução", blank=True, null=True)
    numero_pasep = models.CharField(max_length=255, blank=True, null=True, verbose_name="Número do PASEP")

    # 5. Contato
    celular = models.CharField(max_length=255, verbose_name="Celular", blank=True, null=True)
    telefone_fixo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telefone fixo")
    # E-mail não é mais único para permitir múltiplos vínculos
    email = models.EmailField(verbose_name="E-mail", blank=True, null=True)

    # 6. Endereço
    cep = models.CharField(max_length=255, verbose_name="CEP", blank=True, null=True)
    endereco = models.CharField(max_length=255, verbose_name="Logradouro", blank=True, null=True)
    numero = models.CharField(max_length=255, verbose_name="Número", blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=255, verbose_name="Bairro", blank=True, null=True)
    cidade = models.CharField(max_length=255, verbose_name="Cidade", blank=True, null=True)
    uf = models.CharField(max_length=255, verbose_name="UF", blank=True, null=True)

    observacoes = models.TextField(
        max_length=10000,
        blank=True,
        null=True,
        verbose_name="Observações (informações adicionais)"
    )

    def __str__(self):
        return self.nome_completo if self.nome_completo else f"Colaborador {self.registro}"


# Esta classe deve ser um modelo separado, não aninhado
class Ferias(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
        ('cancelada', 'Cancelada'),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='ferias')
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_solicitacao = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Férias de {self.colaborador.nome_completo} ({self.data_inicio} a {self.data_fim})"