from django.conf.urls import patterns, include, url
from django.contrib import admin
from mathsocwebsite import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('external_api.urls')),
    url(r'^elections/', include('elections.urls')),
    url(r'^resources/', include('services.urls')),
    url(r'^tangent/', include('tangent.urls')),
    url(r'^login/', views.user_login, name="login"),
    url(r'^', include('frontend.urls')),
)
