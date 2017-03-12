from django.conf.urls import patterns, include, url

urlpatterns = patterns('tangent.views',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='tangent_home'),
    url(r'^profile/', 'profile', name='tangent_profile'),
    url(r'^organizations/members/(?P<org_id>\d+)/$', 'org_members', name='tangent_org_members'),
    url(r'^clubs/members/(?P<org_id>\d+)/$', 'club_members', name='tangent_club_members'),
    url(r'^announcements/organizations/(?P<org_id>\d+)/$', 'org_announcements', name='tangent_org_announcements'),
    url(r'^announcements/clubs/(?P<org_id>\d+)/$', 'club_announcements', name='tangent_club_announcements'),
    url(r'^announcements/$', 'org_members', name='tangent_announcements'),
    url(r'^bookings/$', 'bookings', name='tangent_bookings'),
    url(r'^bookings/(?P<show_all>all)/$', 'bookings', name='tangent_bookings_all'),
    url(r'^bookings/(?P<booking_id>\d+)/$', 'booking', name='tangent_booking'),
    url(r'^bookings/(?P<booking_id>\d+)/accept/$', 'accept_booking', name='tangent_accept_booking'),
    url(r'^bookings/(?P<booking_id>\d+)/reject/$', 'reject_booking', name='tangent_reject_booking')
)
