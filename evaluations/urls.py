from django.conf.urls import patterns, include, url

urlpatterns = patterns('evaluations.views',
                       url(r'^$', 'evaluations', name='resources_evaluations'),)
