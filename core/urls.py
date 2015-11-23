from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^trip/create/$', TripCreateView.as_view(), name='trip_create'),
    url(r'trip/$', TripListView.as_view(), name='trip_list'),
    url(r'^trip/(?P<pk>\d+)/$', TripDetailView.as_view(), name='trip_detail'),
    url(r'^trip/update/(?P<pk>\d+)/$', TripUpdateView.as_view(), name='trip_update'),
    url(r'^trip/delete/(?P<pk>\d+)/$', TripDeleteView.as_view(), name='trip_delete'),
    url(r'^trip/(?P<pk>\d+)/comment/create/$', CommentCreateView.as_view(), name='comment_create'),
)