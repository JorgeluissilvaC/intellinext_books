# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from books.models import books, comments

# Register your models here.

admin.site.register(books)
admin.site.register(comments)