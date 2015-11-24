from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^trip/create/$', login_required(TripCreateView.as_view()), name='trip_create'),
    url(r'trip/$', login_required(TripListView.as_view()), name='trip_list'),
    url(r'^trip/(?P<pk>\d+)/$', login_required(TripDetailView.as_view()), name='trip_detail'),
    url(r'^trip/update/(?P<pk>\d+)/$', login_required(TripUpdateView.as_view()), name='trip_update'),
    url(r'^trip/delete/(?P<pk>\d+)/$', login_required(TripDeleteView.as_view()), name='trip_delete'),
    url(r'^trip/(?P<pk>\d+)/comment/create/$', login_required(CommentCreateView.as_view()), name='comment_create'),
    url(r'^trip/(?P<trip_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', login_required(CommentUpdateView.as_view()), name='comment_update'),
    url(r'^trip/(?P<trip_pk>\d+)/comment/delete/(?P<comment_pk>\d+)/$', login_required(CommentDeleteView.as_view()), name='comment_delete'),
    url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),
    url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
)