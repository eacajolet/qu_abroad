from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class TripCreateView(CreateView):
    model = Trip
    template_name = "trip/trip_form.html"
    fields = ['title', 'description', 'rating']
    success_url = reverse_lazy('trip_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TripCreateView, self).form_valid(form)

class TripListView(ListView):
    model = Trip
    template_name = "trip/trip_list.html"

class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip/trip_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TripDetailView, self).get_context_data(**kwargs)
        trip = Trip.objects.get(id=self.kwargs['pk'])
        comments = Comment.objects.filter(trip=trip)
        context['comments'] = comments
        return context

class TripUpdateView(UpdateView):
    model = Trip
    template_name = 'trip/trip_form.html'
    fields = ['title', 'description', 'rating']

    def get_object(self, *args, **kwargs):
            object = super(TripUpdateView, self).get_object(*args, **kwargs)
            if object.user != self.request.user:
                raise PermissionDenied()
            return object

class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'trip/trip_confirm_delete.html'
    success_url = reverse_lazy('trip_list')

    def get_object(self, *args, **kwargs):
            object = super(TripDeleteView, self).get_object(*args, **kwargs)
            if object.user != self.request.user:
                raise PermissionDenied()
            return object

class CommentCreateView(CreateView):
    model = Comment
    template_name = "comment/comment_form.html"
    fields = ['text']

    def get_success_url(self):
        return self.object.trip.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.trip = Trip.objects.get(id=self.kwargs['pk'])
        return super(CommentCreateView, self).form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    pk_url_kwarg = 'comment_pk'
    template_name = 'comment/comment_form.html'
    fields = ['text']

    def get_success_url(self):
        return self.object.trip.get_absolute_url()

    def get_object(self, *args, **kwargs):
            object = super(CommentUpdateView, self).get_object(*args, **kwargs)
            if object.user != self.request.user:
                raise PermissionDenied()
            return object

class CommentDeleteView(DeleteView):
    model = Comment
    pk_url_kwarg = 'comment_pk'
    template_name = 'comment/comment_confirm_delete.html'

    def get_success_url(self):
        return self.object.trip.get_absolute_url()

    def get_object(self, *args, **kwargs):
            object = super(CommentDeleteView, self).get_object(*args, **kwargs)
            if object.user != self.request.user:
                raise PermissionDenied()
            return object

class VoteFormView(FormView):
    form_class = VoteForm

    def form_valid(self, form):
        user = self.request.user
        trip = Trip.objects.get(pk=form.data["trip"])
        try:
            comment = Comment.objects.get(pk=form.data["comment"])
            prev_votes = Vote.objects.filter(user=user, comment=comment)
            has_voted = (prev_votes.count()>0)
            if not has_voted:
                Vote.objects.create(user=user, comment=comment)
            else:
                prev_votes[0].delete()
            return redirect(reverse('trip_detail', args=[form.data["trip"]]))
        except: 
            prev_votes = Vote.objects.filter(user=user, trip=trip)
        has_voted = (prev_votes.count()>0)
        if not has_voted:
            Vote.objects.create(user=user, trip=trip)
        else:
            prev_votes[0].delete()
        return redirect('trip_list')
      
class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'user/user_detail.html'
    context_object_name = 'user_in_view'
    
    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user_in_view = User.objects.get(username=self.kwargs['slug'])
        trips = Trip.objects.filter(user=user_in_view)
        context['trips'] = trips
        comments = Comment.objects.filter(user=user_in_view)
        context['comments'] = comments
        return context