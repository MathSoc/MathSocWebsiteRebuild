from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',
                       url(r'^$', 'home', name='resources_home'),)