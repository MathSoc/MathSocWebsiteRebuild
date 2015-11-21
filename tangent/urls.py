from django.conf.urls import patterns, include, url

urlpatterns = patterns('tangent.views',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='tangent_home'),
    url(r'^log/', 'log', name='tangent_log'),
    url(r'^profile/', 'profile', name='tangent_profile'),
    url(r'^HELP$', 'help', name='tangent_help'),
    url(r'^website/', 'website', name='tangent_website'),
    url(r'^(?P<org_id>\d+)/', 'organization', name='tangent_organization'),
    url(r'^bookings/$', 'bookings', name='tangent_bookings'),
    url(r'^bookings/(?P<show_all>all)/$', 'bookings', name='tangent_bookings_all'),
    url(r'^bookings/(?P<booking_id>\d+)/$', 'booking', name='tangent_booking'),
    url(r'^bookings/(?P<booking_id>\d+)/accept/$', 'accept_booking', name='tangent_accept_booking'),
    url(r'^bookings/(?P<booking_id>\d+)/reject/$', 'reject_booking', name='tangent_reject_booking')
)
