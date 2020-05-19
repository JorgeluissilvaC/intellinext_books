from django.conf.urls import url, include
#from django.contrib import admin
#from django.urls import path
from usuario.views import registar_usuario,editar_usuario,eliminar_usuario
app_name = 'usuario'
urlpatterns = [
    url(r'^nuevo$',registar_usuario.as_view() , name="new"),
    url(r'^edit_book/(?P<pk>\d+)/$',editar_usuario.as_view() , name="edit"),
    url(r'^delete_book/(?P<pk>\d+)/$',eliminar_usuario.as_view() , name="delete"),
]