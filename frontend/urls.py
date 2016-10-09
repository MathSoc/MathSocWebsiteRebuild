from django.conf.urls import patterns, include, url

urlpatterns = patterns('frontend.views',
                       url(r'^$', 'index', name='frontend_home'),
                       url(r'^governance/', 'governance', name='frontend_governance'),
                       url(r'^organization/(?P<org_id>\d+)/', 'organization', name='frontend_organization'),
                       url(r'^office/', 'office', name='frontend_office'),
                       url(r'^volunteers/', 'volunteers', name='frontend_volunteers'),
                       url(r'^position/(?P<pos_id>\d+)/', 'position', name='frontend_position'),
                       url(r'^clubs/', 'clubs', name='frontend_clubs'),
                       url(r'^contact/', 'contact', name='frontend_contact'),
)
