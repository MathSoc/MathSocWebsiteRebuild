from django.conf.urls import patterns, include, url

urlpatterns = patterns('bookings.views',
                       url(r'^$', 'bookings', name='resources_bookings'),
                       url(r'^equipment', 'equipment_booking_policy', name='equipment_booking_policy'),
                       url(r'^rooms', 'room_booking_policy', name='room_booking_policy'),)
