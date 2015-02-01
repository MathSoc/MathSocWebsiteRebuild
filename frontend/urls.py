from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index', name='frontend_home'),
    url(r'^governance/', 'frontend.views.governance', name='frontend_governance'),
    url(r'^office/', 'frontend.views.office', name='frontend_office'),
    url(r'^volunteers/', 'frontend.views.volunteers', name='frontend_volunteers'),
    url(r'^clubs/', 'frontend.views.clubs', name='frontend_clubs'),
    url(r'^contact/', 'frontend.views.contact', name='frontend_contact')
)
