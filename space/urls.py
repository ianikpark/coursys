from django.conf.urls import url
from courselib.urlparts import SLUG_RE, ID_RE
from space import views


LOCATION_SLUG = '(?P<location_slug>' + SLUG_RE + ')'
BOOKING_SLUG = '(?P<booking_slug>' + SLUG_RE + ')'
LOCATION_ID = '(?P<location_id>' + ID_RE + ')'
ROOMTYPE_SLUG = '(?P<roomtype_slug>' + SLUG_RE + ')'
BOOKING_ID = '(?P<booking_id>' + ID_RE + ')'
ROOMTYPE_ID = '(?P<roomtype_id>' + ID_RE + ')'
FROM_INDEX = '(?P<from_index>' + ID_RE + ')'


space_patterns = [  # prefix /space/
    url('^$', views.index, name='index'),
    url('^download/$', views.download_locations, name='download_locations'),
    url(r'^new_location/$', views.add_location, name='add_location'),
    url(r'^' + LOCATION_SLUG + '/edit$', views.edit_location, name='edit_location'),
    url(r'^' + LOCATION_SLUG + '/edit/' + FROM_INDEX + '/$', views.edit_location, name='edit_location'),
    url(r'^' + LOCATION_SLUG + '/view$', views.view_location, name='view_location'),
    url(r'^' + LOCATION_ID + '/delete$', views.delete_location, name='delete_location'),
    url(r'^roomtypes/$', views.list_roomtypes, name='list_roomtypes'),
    url(r'^new_roomtype/$', views.add_roomtype, name='add_roomtype'),
    url(r'^roomtypes/' + ROOMTYPE_SLUG + '/edit$', views.edit_roomtype, name='edit_roomtype'),
    url(r'^roomtypes/' + ROOMTYPE_SLUG + '/view$', views.view_roomtype, name='view_roomtype'),
    url(r'^roomtypes/' + ROOMTYPE_ID + '/delete$', views.delete_roomtype, name='delete_roomtype'),
    url(r'^' + LOCATION_SLUG + '/add_booking$', views.add_booking, name='add_booking'),
    url(r'^' + LOCATION_SLUG + '/add_booking/' + FROM_INDEX + '/$', views.add_booking, name='add_booking'),
    url(r'^bookings/' + BOOKING_SLUG + '/edit$', views.edit_booking, name='edit_booking'),
    url(r'^bookings/' + BOOKING_SLUG + '/view$', views.view_booking, name='view_booking'),
    url(r'^bookings/' + BOOKING_ID + '/delete$', views.delete_booking, name='delete_booking'),
    url(r'^bookings/' + BOOKING_SLUG + '/attach$', views.add_booking_attachment, name='add_booking_attachment'),
    url(r'^bookings/' + BOOKING_SLUG + '/send_memo$', views.send_memo, name='send_booking_memo'),
]
