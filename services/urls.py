from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',
    # Examples:
    # url(r'^$', 'mathsocwebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='services_home'),
    url(r'exambank/', 'exambank', name='exambank'),
    url(r'lockers/', 'lockers', name='lockers'),
    url(r'bookings/', 'bookings', name='bookings')
)
