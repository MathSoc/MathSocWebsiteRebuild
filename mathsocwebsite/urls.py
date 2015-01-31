from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', 'frontend.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('external_api.urls')),
    url(r'^elections/', include('elections.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^tangent/', include('tangent.urls'))
)
