from django.conf.urls import patterns, include, url
from ventureprime.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ventureprime.views.home', name='home'),
    # url(r'^ventureprime/', include('ventureprime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', homepage),
    (r'^email_submit/$', email_submit),

    (r'^time/$', current_datetime),
    (r'^meta/$', display_meta),
    (r'^search/$', search),

    (r'^comic/$', comic),
    (r'^contact/$', contact),
)
