from django import forms
from books.models import books, comments

class book_form(forms.ModelForm):
    class Meta:
        model = books

        fields = [
                'title',
                'publication_date',
        ]

        labels = {
                'title': 'Nombre del libro',
                'publication_date': 'Fecha de publicacion',

        }

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'publication_date': forms.DateInput(attrs={'class': 'form-control'}),

        }

class comments_form(forms.ModelForm):
    class Meta:
        model = comments

        fields = [
                'text',
                'created_date',
        ]

        labels = {
                'text': 'Comentario',
                'created_date': 'Fecha de creacion',

        }

        widgets = {
                'text': forms.TextInput(attrs={'class': 'form-control'}),
                'created_date': forms.DateInput(attrs={'class': 'form-control'}),

        }
