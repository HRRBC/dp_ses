from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Colaborador
from django.http import HttpResponse 
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging 
logger = logging.getLogger(__name__)

# --- Importações para manipulação de PDF (Adicionadas/Verificadas) ---
from PyPDF2 import PdfReader, PdfWriter # Certifique-se que PyPDF2 está instalado (pip install pypdf2)
from reportlab.pdfgen import canvas # Certifique-se que reportlab está instalado (pip install reportlab)
from reportlab.lib.pagesizes import A4
from io import BytesIO
import os
from django.conf import settings # Para acessar BASE_DIR


def login(request):
    if request.method == "GET":
        return render(request, 'tarefas/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            messages.success(request, f"Bem-vindo(a) de volta, {user.username}!")
            return redirect('tarefas:home')
        else:
            messages.error(request, "Usuário ou senha inválidos. Por favor, tente novamente.")
            return render(request, 'tarefas/login.html', {'error': 'Usuário ou senha inválidos'})

@login_required(login_url="auth/login/")
def home(request):
    return render(request, 'tarefas/home.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Você foi desconectado(a) com sucesso.")
    return redirect('/auth/login/')

@login_required(login_url='/auth/login/')
def cadastrar_colaborador(request):
    if request.method == 'POST':
        try:
            colaborador = Colaborador(
                matricula=request.POST.get('matricula'),
                nome_completo=request.POST.get('nome_completo'),
                cargo=request.POST.get('cargo'),
                funcao=request.POST.get('funcao'),
                numero_conselho=request.POST.get('numero_conselho').strip() or None,
                uf_conselho=request.POST.get('uf_conselho').strip() or None,
                nome_conselho=request.POST.get('nome_conselho').strip() or None,
                setor_trabalho=request.POST.get('setor_trabalho'),
                turno=request.POST.get('turno'),
                dias_trabalho=request.POST.get('dias_trabalho').strip() or None,
                jornada_trabalho=request.POST.get('jornada_trabalho'),
                tipo_contrato=request.POST.get('tipo_contrato'),
                status=request.POST.get('status'),
                data_admissao=request.POST.get('data_admissao'),
                nome_mae=request.POST.get('nome_mae'),
                nome_pai=request.POST.get('nome_pai').strip() or None,
                data_nascimento=request.POST.get('data_nascimento'),
                naturalidade=request.POST.get('naturalidade'),
                estado_civil=request.POST.get('estado_civil'),
                titulo_eleitor=request.POST.get('titulo_eleitor').strip() or None,
                zona_eleitoral=request.POST.get('zona_eleitoral').strip() or None,
                secao_eleitoral=request.POST.get('secao_eleitoral').strip() or None,
                estado_vota=request.POST.get('estado_vota').strip() or None,
                rg_completo=request.POST.get('rg_completo'),
                cpf=request.POST.get('cpf').replace('.', '').replace('-', ''),
                numero_ctps=request.POST.get('numero_ctps'),
                serie_ctps=request.POST.get('serie_ctps'),
                uf_ctps=request.POST.get('uf_ctps'),
                documento_militar=request.POST.get('documento_militar').strip() or None,
                grau_instrucao=request.POST.get('grau_instrucao'),
                numero_pasep=request.POST.get('numero_pasep').strip() or None,
                celular=request.POST.get('celular').replace('(', '').replace(')', '').replace(' ', '').replace('-', ''),
                telefone_fixo=request.POST.get('telefone_fixo').replace('(', '').replace(')', '').replace(' ', '').replace('-', '') or None,
                email=request.POST.get('email'),
                cep=request.POST.get('cep').replace('-', ''),
                endereco=request.POST.get('endereco'),
                numero=request.POST.get('numero'),
                complemento=request.POST.get('complemento').strip() or None,
                bairro=request.POST.get('bairro'),
                cidade=request.POST.get('cidade'),
                uf=request.POST.get('uf'),
                # NOVO CAMPO: Observações
                observacoes=request.POST.get('observacoes').strip() or None, 
            )
            colaborador.full_clean()
            colaborador.save()
            messages.success(request, f"Colaborador '{colaborador.nome_completo}' cadastrado com sucesso!")
            return redirect('tarefas:listar_colaboradores')
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar colaborador: {e}")
            logger.error(f"Erro ao cadastrar colaborador: {e}", exc_info=True)
            return render(request, 'tarefas/cadastrar_colaborador.html')
            
    return render(request, 'tarefas/cadastrar_colaborador.html')

@login_required(login_url='/auth/login/')
def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, registro=id) 
    
    if request.method == 'POST':
        # Você não precisa editar o 'registro' aqui, pois ele é a primary key
        colaborador.matricula = request.POST.get('matricula')
        colaborador.nome_completo = request.POST.get('nome_completo')
        colaborador.cargo = request.POST.get('cargo')
        colaborador.funcao = request.POST.get('funcao')
        colaborador.numero_conselho = request.POST.get('numero_conselho').strip() or None
        colaborador.uf_conselho = request.POST.get('uf_conselho').strip() or None
        colaborador.nome_conselho = request.POST.get('nome_conselho').strip() or None
        colaborador.setor_trabalho = request.POST.get('setor_trabalho')
        colaborador.turno = request.POST.get('turno')
        colaborador.dias_trabalho = request.POST.get('dias_trabalho').strip() or None
        colaborador.jornada_trabalho = request.POST.get('jornada_trabalho')
        colaborador.tipo_contrato = request.POST.get('tipo_contrato')
        colaborador.status = request.POST.get('status')
        colaborador.data_admissao = request.POST.get('data_admissao')
        colaborador.nome_mae = request.POST.get('nome_mae')
        colaborador.nome_pai = request.POST.get('nome_pai').strip() or None
        colaborador.data_nascimento = request.POST.get('data_nascimento')
        colaborador.naturalidade = request.POST.get('naturalidade')
        colaborador.estado_civil = request.POST.get('estado_civil')
        colaborador.titulo_eleitor = request.POST.get('titulo_eleitor').strip() or None
        colaborador.zona_eleitoral = request.POST.get('zona_eleitoral').strip() or None
        colaborador.secao_eleitoral = request.POST.get('secao_eleitoral').strip() or None
        colaborador.estado_vota = request.POST.get('estado_vota').strip() or None
        colaborador.rg_completo = request.POST.get('rg_completo')
        colaborador.cpf = request.POST.get('cpf').replace('.', '').replace('-', '') 
        colaborador.numero_ctps = request.POST.get('numero_ctps')
        colaborador.serie_ctps = request.POST.get('serie_ctps')
        colaborador.uf_ctps = request.POST.get('uf_ctps')
        colaborador.documento_militar = request.POST.get('documento_militar').strip() or None
        colaborador.grau_instrucao = request.POST.get('grau_instrucao')
        colaborador.numero_pasep = request.POST.get('numero_pasep').strip() or None
        colaborador.celular = request.POST.get('celular').replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        colaborador.telefone_fixo = request.POST.get('telefone_fixo').replace('(', '').replace(')', '').replace(' ', '').replace('-', '') or None
        colaborador.email = request.POST.get('email')
        colaborador.cep = request.POST.get('cep').replace('-', '')
        colaborador.endereco = request.POST.get('endereco')
        colaborador.numero = request.POST.get('numero')
        colaborador.complemento = request.POST.get('complemento').strip() or None
        colaborador.bairro = request.POST.get('bairro')
        colaborador.cidade = request.POST.get('cidade')
        colaborador.uf = request.POST.get('uf')
        # NOVO CAMPO: Observações
        colaborador.observacoes = request.POST.get('observacoes').strip() or None 

        try:
            colaborador.full_clean()
            colaborador.save()
            messages.success(request, f"Colaborador '{colaborador.nome_completo}' atualizado com sucesso!")
            return redirect('tarefas:listar_colaboradores')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar colaborador: {e}")
            logger.error(f"Erro ao atualizar colaborador: {e}", exc_info=True)
            
    return render(request, 'tarefas/editar_colaborador.html', {'colaborador': colaborador})

@login_required(login_url='/auth/login/')
def listar_colaboradores(request):
    filtro_setor = request.GET.get('setor', '')
    filtro_status = request.GET.get('status', '')
    filtro_busca_nome = request.GET.get('busca_nome', '').strip() # NOVO: Captura o termo de busca

    colaboradores = Colaborador.objects.all().order_by('nome_completo')
    
    if filtro_setor:
        colaboradores = colaboradores.filter(setor_trabalho=filtro_setor)
    if filtro_status:
        colaboradores = colaboradores.filter(status=filtro_status)
    
    # NOVO: Aplica o filtro de busca por nome, se houver um termo
    if filtro_busca_nome:
        # __icontains faz uma busca case-insensitive e parcial
        colaboradores = colaboradores.filter(nome_completo__icontains=filtro_busca_nome)
    
    setores_choices = [choice[0] for choice in Colaborador.SETOR_CHOICES]
    status_choices = [choice[0] for choice in Colaborador.STATUS_CHOICES]

    context = {
        'colaboradores': colaboradores,
        'filtro_setor': filtro_setor,
        'filtro_status': filtro_status,
        'filtro_busca_nome': filtro_busca_nome, # NOVO: Passa o termo de busca de volta para o template
        'setores': sorted(list(set(setores_choices))),
        'status_opcoes': status_choices,
    }
    return render(request, 'tarefas/listar_colaboradores.html', context)

@login_required(login_url='/auth/login/')
def folha_de_ponto_selecao(request, id):
    colaborador = get_object_or_404(Colaborador, registro=id)

    meses = [
        {'value': '01', 'name': 'Janeiro'}, {'value': '02', 'name': 'Fevereiro'}, 
        {'value': '03', 'name': 'Março'}, {'value': '04', 'name': 'Abril'}, 
        {'value': '05', 'name': 'Maio'}, {'value': '06', 'name': 'Junho'}, 
        {'value': '07', 'name': 'Julho'}, {'value': '08', 'name': 'Agosto'}, 
        {'value': '09', 'name': 'Setembro'}, {'value': '10', 'name': 'Outubro'}, 
        {'value': '11', 'name': 'Novembro'}, {'value': '12', 'name': 'Dezembro'}, 
    ]
    current_year = timezone.now().year 
    anos = list(range(current_year - 5, current_year + 6))

    context = {
        'colaborador': colaborador,
        'meses': meses,
        'anos': anos,
        'current_year': current_year,
    }
    return render(request, 'tarefas/folha_de_ponto_selecao.html', context)

@login_required(login_url='/auth/login/')
def gerar_folha_ponto_pdf(request):
    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador_id')
        mes_num = request.POST.get('mes') 
        ano = request.POST.get('ano')

        colaborador_obj = get_object_or_404(Colaborador, registro=colaborador_id)
        
        colaborador_nome = colaborador_obj.nome_completo
        matricula = colaborador_obj.matricula
        setor = colaborador_obj.get_setor_trabalho_display() 
        cargo = colaborador_obj.get_cargo_display()       

        meses_nomes = {
            '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
            '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
            '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro',
        }
        mes_nome = meses_nomes.get(mes_num, mes_num)

        caminho_pdf_modelo = os.path.join(settings.BASE_DIR, 'dp_ses_management', 'static', 'documentos', 'folha_de_ponto.pdf')

        if not os.path.exists(caminho_pdf_modelo):
            messages.error(request, "Erro: Arquivo PDF modelo não encontrado no servidor.")
            logger.error(f"Arquivo PDF modelo não encontrado: {caminho_pdf_modelo}")
            return redirect('tarefas:listar_colaboradores')

        try:
            # --- Cria o PDF com o texto (overlay) ---
            packet = BytesIO()
            can = canvas.Canvas(packet, pagesize=A4)

            can.setFont("Helvetica-Bold", 11)
            # Estas são as coordenadas que você precisará ajustar para o seu PDF
            can.drawString(70, 679, colaborador_nome) 
            can.drawString(430, 679, matricula)
            can.drawString(75, 651, cargo)
            can.drawString(405, 651, setor)
            
            can.setFont("Helvetica-Bold", 13)
            can.drawString(500, 172, f"{mes_nome}/{ano}") 
            
            can.save()
            packet.seek(0)
            novo_conteudo = PdfReader(packet) # Variável definida aqui

            # --- DEBUG: Verifique se o overlay tem páginas ---
            print(f"DEBUG: Novo conteúdo (overlay) tem páginas? {len(novo_conteudo.pages) > 0}")

            # --- Abre o PDF Modelo e Mescla ---
            with open(caminho_pdf_modelo, "rb") as f_modelo:
                modelo_pdf = PdfReader(f_modelo)
                
                # VERIFICAÇÃO ADICIONAL: Certifique-se de que o modelo tem páginas
                if not modelo_pdf.pages:
                    messages.error(request, "Erro: O arquivo PDF modelo não contém páginas visíveis para processamento.")
                    logger.error(f"PDF Modelo '{caminho_pdf_modelo}' não tem páginas detectáveis por PyPDF2.")
                    return redirect('tarefas:listar_colaboradores')
                
                # --- DEBUG: Verifique se o modelo tem páginas ---
                print(f"DEBUG: PDF Modelo tem páginas? {len(modelo_pdf.pages) > 0}")

                output = PdfWriter()

                for i in range(len(modelo_pdf.pages)):
                    page = modelo_pdf.pages[i]
                    if i == 0: 
                        # CORRIGIDO AQUI: Usando 'novo_conteudo' (a variável correta)
                        page.merge_page(novo_conteudo.pages[0]) 
                    output.add_page(page)

                response_buffer = BytesIO()
                output.write(response_buffer)
                response_buffer.seek(0)

                filename = f"Folha_Ponto_{colaborador_nome.replace(' ', '_')}_{mes_nome}_{ano}.pdf"
                response = HttpResponse(response_buffer.getvalue(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'

                messages.success(request, f"Folha de Ponto de {colaborador_nome} para {mes_nome}/{ano} gerada com sucesso!")
                return response

        except Exception as e:
            messages.error(request, f"Erro ao gerar a folha de ponto. Detalhes: {e}. Por favor, verifique se o PDF modelo não está corrompido ou protegido.")
            logger.error(f"Erro ao gerar PDF da folha de ponto para {colaborador_nome}: {e}", exc_info=True)
            return redirect('tarefas:folha_de_ponto_selecao', id=colaborador_id) 

    messages.error(request, "Requisição inválida para gerar o PDF da folha de ponto.")
    return redirect('tarefas:listar_colaboradores')