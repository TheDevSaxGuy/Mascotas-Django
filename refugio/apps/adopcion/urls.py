from django.urls import path, include
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate,PersonaView, SolicitudUpdate,PersonaUpdate, PersonaDelete, SolicitudDelete
"""
('url para entrar',nombre de la view)
"""
app_name = 'apps'
urlpatterns = [
     path('index', index_adopcion),
     path('solicitud/listar', SolicitudList.as_view(),name='solicitud_listar'),
     path('solicitud/nueva', SolicitudCreate.as_view(),name='solicitud_crear'),
     path('solicitud/editar/<pk>', SolicitudUpdate.as_view(),name='solicitud_editar'),
     path('solicitud/eliminar/<pk>', SolicitudDelete.as_view(),name='solicitud_eliminar'),
     path('persona/listar', PersonaView.as_view(),name='persona_listar'),
     path('persona/editar/<pk>', PersonaUpdate.as_view(),name='persona_editar'),
     path('persona/eliminar/<pk>', PersonaDelete.as_view(),name='persona_eliminar'),

]