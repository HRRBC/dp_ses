from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('auth/', include("dp_ses_management.urls")),
]

# Servir arquivos estáticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Servir arquivos de mídia (documentos dos colaboradores)
# Em produção com Nginx, o Nginx serve /media/ diretamente — esta linha vira fallback
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
