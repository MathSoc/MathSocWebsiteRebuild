from django.conf.urls import patterns, include, url

urlpatterns = patterns('university.views',
                   url(r'^evaluations$', 'evaluations', name='resources_evaluations'),
                   url(r'^exambank$', 'exambank', name='resources_exambank'),
                   url(r'^courses/', 'get_courses', name='get_courses'),
                   url(r'^exams', 'get_exams', name='get_exams'),
                   url(r'^exam/(?P<subject>[a-zA-Z]{2,5})/(?P<course>\d{2,3})', 'get_exam',
                       name='get_exam'),)
