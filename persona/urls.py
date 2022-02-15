from django.urls import path
from . import views
from .CRUD import documentos

urlpatterns = [
    path('', views.index, name='index'),
    path('tipodocumento/', documentos.obtener_documentos, name='obtener_documentos'),
    path('tipodocumento/creardocumento/', documentos.crear_documento, name='crear_documento'),
    path('tipodocumento/actualizardocumento/<int:id>/', documentos.actualizar_documento, name='actualizar_documento'),
    path('tipodocumento/eliminardocumento/<int:id>/', documentos.eliminar_documento, name='eliminar_documento'),
]