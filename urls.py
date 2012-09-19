from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from tal_assembly.conversion import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tal_assembly.views.home', name='home'),
    # url(r'^tal_assembly/', include('tal_assembly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tal_conversion/$', views.tal_conversion),
    (r'^convert/$', views.convert),
   	(r'^$',views.tal_tools),
)
