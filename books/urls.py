from django.conf.urls import url, include
from books.views import *
from django.contrib.auth.decorators import login_required

app_name = 'books'
urlpatterns = [
    #book
    url(r'^listar_book$', login_required(book_list.as_view() ), name='list_book'),
    url(r'^new_book$', book_new , name='new_book'),
    url(r'^delete_book/(?P<pk>\d+)/$', login_required(book_delete.as_view()) , name='delete_book'),
    url(r'^edit_book/(?P<pk>\d+)/$', login_required(book_edit.as_view()) , name='edit_book'),

    #Comentarios
    url(r'^listar_comments/(?P<id_book>\d+)/$', comments_list , name='list_comments'),
    url(r'^new_comments/(?P<id_book>\d+)/$', comments_new , name='new_comments'),
    url(r'^delete_comments/(?P<id_book>\d+)/(?P<id_comment>\d+)/$', comments_delete , name='delete_comments'),
    url(r'^edit_comments/(?P<id_book>\d+)/(?P<id_comment>\d+)/$', comments_edit , name='edit_comments'),
    ] 