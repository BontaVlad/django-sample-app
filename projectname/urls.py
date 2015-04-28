#! /usr/bin/env python2.7
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.views import serve
from django.contrib import admin
from projectname.home.views import (
    HomeView, CarPartsListCreateView, CarPartDetailView, HelpView
)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),    # noqa
    url(r'^parts$', CarPartsListCreateView.as_view(), name='parts_list'),
    url(r'^parts/(?P<pk>\d+)$', CarPartDetailView.as_view(),
        name='part_detail'),
    url(r'^help$', HelpView.as_view(), name='help'),

    # static
    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve,
        {'show_indexes': True, 'insecure': False}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
)

urlpatterns += patterns('', url(r'^silk/', include('silk.urls',
                                                   namespace='silk')))
