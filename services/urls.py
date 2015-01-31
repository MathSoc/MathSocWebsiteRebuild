from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',
    # Examples:
    # url(r'^$', 'mathsocwebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'exambank/', 'exambank'),
    url(r'lockers/', 'lockers'),
    url(r'bookings/', 'bookings')

)
