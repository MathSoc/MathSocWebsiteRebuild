from django.conf.urls import patterns, include, url
from django.contrib import admin

from external_api import views

urlpatterns = patterns('',
                       url(r'^students/$', views.students, name='students'),
                       url(r'^faculties/$', views.faculties, name='faculties'),
                       url(r'^interface/$', views.interface, name='interface'),
                       url(r'^student/(<?P<quest_id>\w+)/$', views.student, name='student'),
                       url(r'^faculty/(<?P<faculty_id>\d+)/$', views.faculty, name='faculty'),
)