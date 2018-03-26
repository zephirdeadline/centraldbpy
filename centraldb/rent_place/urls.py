"""supervisorstable URL Configuration

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
from django.conf.urls import url

#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^module_rent_place/admin$', views.admin_rent_place),
    url(r'^module_rent_place/admin/configure/(?P<id_place>[0-9]+)/$', views.admin_configure),
    url(r'^module_rent_place/admin/delete/(?P<id>[0-9]+)/$', views.admin_delete),
    url(r'^module_rent_place/user/$', views.user_rent_place),
    url(r'^module_rent_place/user/rent/(?P<id_place>[0-9]+)$', views.user_rent),

]
