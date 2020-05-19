# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from books.forms import book_form, comments_form
from books.models import books, comments
from django.http import HttpResponseRedirect
from django.views.generic import ListView,UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
# CRUD books

@login_required
def book_new(request):
    if request.method == 'GET':
        form = book_form()
        return render (request,'books/book_new.html',{'form': form})
    elif request.method == 'POST':
        form = book_form(request.POST, request.FILES)
        if form.is_valid():
            new_book = books(   title=form.cleaned_data["title"],
                                publication_date=form.cleaned_data["publication_date"]
                                )
            new_book.save()
    return HttpResponseRedirect('/book/listar_book')

class book_list(ListView):
    model = books
    template_name = 'books/book_list.html'


class book_delete(DeleteView):
    model = books
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:list_book')


class book_edit(UpdateView):
    model = books
    form_class = book_form
    template_name = 'books/book_new.html'
    success_url = reverse_lazy('books:list_book')

# CRUD comments
@login_required
def comments_new(request,id_book):
    if request.method == 'GET':
        form = comments_form()
        return render (request,'comments/comment_new.html',{'form': form})

    elif request.method == 'POST':
        form = comments_form(request.POST)
        if form.is_valid():
            book = books.objects.filter(id = id_book)[0]
            us = User.objects.filter(username=request.user)[0]
            new_comment = comments(   
                                id_book = book,
                                text=form.cleaned_data["text"],
                                created_date=form.cleaned_data["created_date"],
                                id_user = us
                                )
            new_comment.save()
    return HttpResponseRedirect('/book/listar_comments/'+str(id_book))

@login_required
def comments_list(request, id_book):
    if request.method == 'GET':
        book = books.objects.filter(id = id_book)[0]
        comentarios = comments.objects.filter(id_book = book)
        contexto = {'comentarios': comentarios,
                'book': book}
        return render (request,'comments/comment_list.html',contexto)


@login_required
def comments_edit(request,id_book,id_comment):
    comment = comments.objects.get(id = id_comment)
    if request.method == 'GET':
        form = comments_form(instance=comment)
    else:
        form = comments_form(request.POST,instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/book/listar_comments/'+str(id_book))
    return  render(request,'comments/comment_new.html',{'form': form})


@login_required
def comments_delete(request,id_book,id_comment):
    book = books.objects.filter(id = id_book)[0]
    comentarios = comments.objects.filter(id_book = book, id = id_comment)[0]
    if request.method == 'POST':
        comentarios.delete()
        return HttpResponseRedirect('/book/listar_comments/'+str(id_book))
    return  render(request,'comments/comment_delete.html',{'comments': comentarios})
