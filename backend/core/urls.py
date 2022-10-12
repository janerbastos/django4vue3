"""
    core URL Configuration
"""

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='starter-adminlte.html'), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)