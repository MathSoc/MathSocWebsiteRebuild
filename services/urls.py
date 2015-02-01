from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',
    url(r'^$', 'home', name='resources_home'),
    url(r'exambank/', 'exambank', name='resources_exambank'),
    url(r'lockers/', 'lockers', name='resources_lockers'),
    url(r'bookings/', 'bookings', name='resources_bookings'),
    url(r'evaluations/', 'evaluations', name='resources_evaluations')

    url(r'courses', 'get_courses', name='get_courses'),
    url(r'exams/(?P<subject>)/(?P<course>)', 'get_exams', name='get_exams'),
    url(r'exam/(?P<subject>)/(?P<course>)', 'get_exam', name='get_exam'),
)
