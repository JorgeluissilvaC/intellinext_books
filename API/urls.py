from django.conf.urls import url, include
from API.views import get_data

app_name = 'API'
urlpatterns = [
    url(r'^getData/$', get_data , name="get")
]