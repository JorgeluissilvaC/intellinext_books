# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.views.generic import ListView,UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from usuario.forms import registroFormUser

class registar_usuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = registroFormUser
    success_url = reverse_lazy("login")

class eliminar_usuario(DeleteView):
    model = User
    template_name = 'usuario/eliminar.html'
    success_url = reverse_lazy('login')

class editar_usuario(UpdateView):
    model = User
    form_class = registroFormUser
    template_name = 'usuario/edit.html'
    success_url = reverse_lazy('books:list_book')
    