from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mathsocwebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('external_api.urls')),
    url(r'^elections/', include('elections.urls')),
    url(r'^bookings/', include('bookings.urls')),
    url(r'^tangent/', include('tangent.urls'))
)
