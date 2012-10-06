from django.conf.urls import patterns, include, url
from ventureprime import views
from django.views.generic.simple import direct_to_template
from emailusernames.forms import EmailAuthenticationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('ventureprime.views',
    (r'^$', 'method_splitter', {'GET': views.homepage_get, 
        'POST': views.homepage_post}),
    (r'^confirm_email/$', 'confirm_email'),

    (r'^howvpworks/$', direct_to_template, {'template': 'howvpworks/overview.html'}),
    (r'^howvpworks/(?P<user_type>\w+)/(?P<page>\w+)/$', 'howvpworks_pages'),

    (r'^time/$', 'current_datetime'),
    (r'^meta/$', 'display_meta'),
    (r'^search/$', 'search'),

    (r'^comic/$', 'comic'),
    (r'^contact/$', 'contact'),
    (r'^contact/thanks/$', direct_to_template, {'template': 'footer/thanks.html'}),

    (r'^accounts/home/$', 'login_home'),
    (r'^accounts/signup/$', 'create_account'),
    (r'^accounts/create_successful/$', direct_to_template, 
        {'template': 'registration/create_account_success.html'}),
)

#use this body if using a separate views file
#urlpatterns += patterns('',

#)
urlpatterns += patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login', 
        {'authentication_form': EmailAuthenticationForm}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)

#this uses gunicorn to serve up static files
urlpatterns += patterns('',  
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': ventureprime.settings.STATIC_ROOT}),  
) 