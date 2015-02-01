from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',
    url(r'^$', 'home', name='resources_home'),
    url(r'exambank/', 'exambank', name='resources_exambank'),
    url(r'lockers/', 'lockers', name='resources_lockers'),
    url(r'bookings/', 'bookings', name='resources_bookings'),
    url(r'evaluations/', 'evaluations', name='resources_evaluations')
)
