from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index', name='home'),
    url(r'^resources/', 'frontend.views.resources', name='resources'),
    url(r'^governance/', 'frontend.views.governance', name='governance'),
    url(r'^office/', 'frontend.views.office', name='office'),
    url(r'^volunteers/', 'frontend.views.volunteers', name='volunteers'),
    url(r'^clubs/', 'frontend.views.clubs', name='clubs'),
    url(r'^contact/', 'frontend.views.contact', name='contact')
)
