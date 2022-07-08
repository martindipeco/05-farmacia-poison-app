from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('horarios', views.horarios, name='horarios'),
    path('registro', views.registro, name='registro'),
    path('chango', views.chango, name='chango'),
    path('proximamente', views.proximamente, name='proximamente'),
    path('listado', views.listado, name='listado'),
    path('crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
