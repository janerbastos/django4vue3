"""
    core URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', TemplateView.as_view(template_name='core/base.html'), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
