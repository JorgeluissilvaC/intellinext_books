"""Biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book/', include('books.urls', namespace='books')),
    url(r'^API/', include('API.urls', namespace='API')),

    #Gestion de usuarios
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),

    #Logouut and Login
    url(r'^accounts/login/', LoginView.as_view(template_name='usuario/index.html'), name='login'),
    url(r'^$', LoginView.as_view(template_name='usuario/index.html'), name='login1'),
    url(r'^logout/', logout_then_login, name='logout'),

    #Restablecer contrasena
    url(r'^reset/password_reset', PasswordResetView.as_view(template_name='registro/password_reset_form.html', email_template_name='registro/password_reset_email.html', success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    url(r'^/reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registro/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done', PasswordResetCompleteView.as_view(template_name='registro/password_reset_complete.html'),name='password_reset_complete'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)