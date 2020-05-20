# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from API.services import find_book
import json
#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse
from books.models import books
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

import xlwt

# Create your views here.


def index(request):
    results = find_book(params={'category':'libros_programacion',
                                'criteria':'most_viewed'})
    context = { 'results': results }
    return render(request, 'API/index.html',context)

def search(request):
    context = {}
    if request.method == 'POST':
        q = request.POST["q"]
        results = find_book(params={'book_title':q})
        context = { 'results': results,
                    'q':q }

    return render(request, 'API/index.html',context)

class report_pdf(View):  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/PDF/head.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)                
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"APP - Biblioteca")
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 770, u"Reporte de resultados")


    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)

        i = 750

        for book in find_book(params={'book_title':self.request.GET["q"]}):
            
            pdf.setFont("Helvetica", 16)
            pdf.drawString(10, i,'Libro:'+ book["title"])

            pdf.setFont("Helvetica", 16)
            pdf.drawString(10, i - 20, "Publica:" + book["publisher"])

            pdf.setFont("Helvetica", 16)
            pdf.drawString(10, i - 40, "Contenido:" + book["content_short"])

            i = i - 100

        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

def report_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Resultados.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Resultados')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['title', 'publisher', 'content', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = []
    for book in find_book(params={'book_title':request.GET["q"]}):
        rows.append([book["title"], book["publisher"],book["content"]])

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
