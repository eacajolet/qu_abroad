from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class TripCreateView(CreateView):
    model = Trip
    template_name = "trip/trip_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('trip_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TripCreateView, self).form_valid(form)

class TripListView(ListView):
    model = Trip
    template_name = "trip/trip_list.html"