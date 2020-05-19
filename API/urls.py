from django.conf.urls import url, include
from API.views import index, search, report_pdf, report_excel
from django.contrib.auth.decorators import login_required

app_name = 'API'
urlpatterns = [
    url(r'^index/$', index  , name="index"),
    url(r'^search/$', search  , name="search"),
    url(r'^report_pdf/$', login_required(report_pdf.as_view())  , name="report_pdf"),
    url(r'^report_excel/$', report_excel , name="report_excel"),
]