from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- IMPORTANTE!
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('auth/', include("dp_ses_management.urls")),
    
]

# Servir arquivos estáticos em modo de desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
