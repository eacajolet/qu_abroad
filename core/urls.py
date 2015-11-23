from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^trip/create/$', TripCreateView.as_view(), name='trip_create'),
    url(r'trip/$', TripListView.as_view(), name='trip_list'),
    url(r'^trip/(?P<pk>\d+)/$', TripDetailView.as_view(), name='trip_detail'),
)