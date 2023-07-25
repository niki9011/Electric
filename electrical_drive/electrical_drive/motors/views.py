from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from .models import Bikes


class BikesListView(ListView):
    template_name = "motors/new.html"
    context_object_name = "bikes"
    model = models.Bikes
    paginate_by = 12
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BikeDetailsView(DetailView):
    model = Bikes
    template_name = "motors/details_motorbikes.html"
    context_object_name = "bike"


class BikeUpdateView(LoginRequiredMixin, UpdateView):
    model = Bikes
    template_name = "motors/update_motorbikes.html"
    fields = "__all__"
    success_url = reverse_lazy("new bike")


class BikeAddView(LoginRequiredMixin, CreateView):

    model = Bikes
    template_name = "motors/add_motorbikes.html"
    fields = "__all__"
    success_url = reverse_lazy("new bike")


class BikeDeleteView(LoginRequiredMixin, DeleteView):

    model = Bikes
    fields = "__all__"
    template_name = "motors/delete_motorbikes.html"
    success_url = reverse_lazy("new bike")
