from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit,mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, listado
"""
('url para entrar',nombre de la view)
"""
app_name='apps'
urlpatterns = [

    path('',index, name='index'),
    path('nuevo',login_required(MascotaCreate.as_view()), name='mascota_crear'),
    path('listar',login_required(MascotaList.as_view()), name='mascota_listar'),
    path('editar/<pk>',login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    path('eliminar/<pk>',login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    path('listado',listado,name="listado"),

]