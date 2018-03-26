from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'admin/$', views.index_admin),
    url(r'admin/domain/$', views.domain_setting),
    url(r'admin/account/$', views.account_setting),
    url(r'admin/add_new_people/$', views.add_new_people),
    url(r'admin/list_people/$', views.list_people),
    url(r'admin/list_people/delete/(?P<id>[0-9]+)$', views.delete),
    url(r'admin/list_people/block/(?P<id>[0-9]+)$', views.block),
    url(r'admin/list_people/deblock/(?P<id>[0-9]+)$', views.deblock),
    url(r'admin/list_people/contact/(?P<id>[0-9]+)$', views.contact),
    url(r'admin/ask_module/$', views.ask_module),#TODO test
]
