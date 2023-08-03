from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from .models import Scooters


class ScootersListView(ListView):
    template_name = "scooters/scooter_catalog.html"
    context_object_name = "scooters"
    model = models.Scooters
    paginate_by = 12
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ScooterDetailsView(DetailView):
    model = Scooters
    template_name = "scooters/details_scooters.html"
    context_object_name = "scooter"


class ScooterUpdateView(LoginRequiredMixin, UpdateView):
    model = Scooters
    template_name = "scooters/update_scooters.html"
    fields = "__all__"
    success_url = reverse_lazy("new scooter")


class ScooterAddView(LoginRequiredMixin, CreateView):

    model = Scooters
    template_name = "scooters/add_scooters.html"
    fields = "__all__"
    success_url = reverse_lazy("new scooter")


class ScooterDeleteView(LoginRequiredMixin, DeleteView):

    model = Scooters
    fields = "__all__"
    template_name = "scooters/delete_scooters.html"
    success_url = reverse_lazy("new scooter")
