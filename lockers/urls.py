from django.conf.urls import patterns, include, url

urlpatterns = patterns('lockers.views',
                       url(r'lockers/', 'lockers', name='resources_lockers'),)