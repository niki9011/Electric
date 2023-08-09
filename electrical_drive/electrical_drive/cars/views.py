from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from .models import Cars


class CarsListView(ListView):
    template_name = "cars/cars_catalog.html"
    context_object_name = "cars"
    model = models.Cars
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarDetailsView(DetailView):
    model = Cars
    template_name = "cars/details_cars.html"
    context_object_name = "car"


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Cars
    template_name = "cars/update_cars.html"
    fields = "__all__"
    success_url = reverse_lazy("new car")


class CarAddView(LoginRequiredMixin, CreateView):

    model = Cars
    template_name = "cars/add_cars.html"
    fields = "__all__"
    success_url = reverse_lazy("new car")


class CarDeleteView(LoginRequiredMixin, DeleteView):

    model = Cars
    fields = "__all__"
    template_name = "cars/delete_cars.html"
    success_url = reverse_lazy("new car")
