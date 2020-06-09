"""opengalactica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home.as_view(), name='home'),
    url(r'^intro', views.intro.as_view(), name='intro'),
    url(r'^index', views.home.as_view(), name='home'),
    url(r'^dictionary', views.dictionary.as_view(), name='dictionary'),
    url(r'^enciklopedia', views.enciklopedia.as_view(), name='enciklopedia'),
    url(r'^history', views.history.as_view(), name='history'),
    url(r'^jobs', views.jobs.as_view(), name='jobs'),
    url(r'^impressum', views.impressum.as_view(), name='impressum'),
    url(r'^logout', views.logout.as_view(), name='logout'),
    url(r'^main', views.main.as_view(), name='main'),
    url(r'^news', views.news.as_view(), name='news'),
    url(r'^registration', views.registration.as_view(), name='registration'),
    url(r'^rules', views.rules.as_view(), name='rules'),
    url(r'^xtendlogin', views.xtendlogin.as_view(), name='xtendlogin'),
    url(r'^screens', views.screens.as_view(), name='screens'),
    url(r'^ships', views.ships.as_view(), name='ships'),
    url(r'^species', views.species.as_view(), name='species'),
    url(r'^terms', views.terms.as_view(), name='terms'),
    url(r'^universe/home', views.universe.home.as_view(), name='universe.home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
