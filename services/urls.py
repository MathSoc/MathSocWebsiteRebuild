from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',
                       url(r'^$', 'home', name='resources_home'),
                       url(r'exambank/$', 'exambank', name='resources_exambank'),
                       url(r'exambank/courses/', 'get_courses', name='get_courses'),
                       url(r'exambank/exams', 'get_exams', name='get_exams'),
                       url(r'exambank/exam/(?P<subject>[a-zA-Z]{2,5})/(?P<course>\d{2,3})', 'get_exam',
                           name='get_exam'),
                       url(r'lockers/', 'lockers', name='resources_lockers'),
                       url(r'bookings/$', 'bookings', name='resources_bookings'),
                       url(r'bookings/equipment', 'equipment_booking_policy', name='equipment_booking_policy'),
                       url(r'bookings/rooms', 'room_booking_policy', name='room_booking_policy'),
                       url(r'evaluations/', 'evaluations', name='resources_evaluations'),)
