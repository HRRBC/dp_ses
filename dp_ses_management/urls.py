# seu_app/urls.py (dp_ses_management/urls.py)
from django.urls import path
from . import views

app_name = 'tarefas' 

urlpatterns = [
    # REMOVIDO o "auth/" do início de cada path
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('colaboradores/cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    path('colaboradores/editar/<int:id>/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/folha-de-ponto-selecao/<int:id>/', views.folha_de_ponto_selecao, name='folha_de_ponto_selecao'),
    path('gerar-folha-ponto-pdf/', views.gerar_folha_ponto_pdf, name='gerar_folha_ponto_pdf'),
    path('aniversariantes/', views.listar_aniversariantes, name='listar_aniversariantes'),
    path('aniversariantes/pdf/<str:mes>/', views.gerar_aniversariantes_pdf, name='gerar_aniversariantes_pdf'),
    path('aniversariantes/', views.listar_aniversariantes, name='listar_aniversariantes'),
    path('aniversariantes/pdf/<str:mes>/', views.gerar_aniversariantes_pdf, name='gerar_aniversariantes_pdf'),
    # NOVO: Rotas para férias
    path('ferias/', views.listar_ferias, name='listar_ferias'),
    path('ferias/solicitar/', views.solicitar_ferias, name='solicitar_ferias'),
    path('ferias/aprovar/<int:ferias_id>/', views.aprovar_ferias, name='aprovar_ferias'),
    path('ferias/excluir/<int:ferias_id>/', views.excluir_ferias, name='excluir_ferias'),
]