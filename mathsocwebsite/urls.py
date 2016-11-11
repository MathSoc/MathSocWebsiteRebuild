from django.conf.urls import patterns, include, url
from django.contrib import admin
from mathsocwebsite import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookings/', include('bookings.urls')),
    url(r'^university/', include('university.urls')),
    url(r'^lockers/', include('lockers.urls')),
    url(r'^resources/', include('services.urls')),
    url(r'^tangent/', include('tangent.urls')),
    url(r'^login/$', 'cas.views.login', name="login"),
    url(r'^logout/$', 'cas.views.logout', name="logout"),
    url(r'^', include('frontend.urls')),
)
