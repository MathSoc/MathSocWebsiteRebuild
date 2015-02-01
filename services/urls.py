from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',
    # Examples:
    # url(r'^$', 'mathsocwebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='resources_home'),
    url(r'exambank/', 'exambank', name='resources_exambank'),
    url(r'lockers/', 'lockers', name='resources_lockers'),
    url(r'bookings/', 'bookings', name='resources_bookings')
)
