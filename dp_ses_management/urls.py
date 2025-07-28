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
]