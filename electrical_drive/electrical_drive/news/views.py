from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from .models import AllNews


class AllNewsListView(ListView):
    template_name = "news/news_publication.html"
    context_object_name = "allnews"
    model = models.AllNews
    paginate_by = 12
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsDetailsView(DetailView):
    model = AllNews
    template_name = "news/details_news.html"
    context_object_name = "news"


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = AllNews
    template_name = "news/update_news.html"
    fields = "__all__"
    success_url = reverse_lazy("new news")


class NewsAddView(LoginRequiredMixin, CreateView):

    model = AllNews
    template_name = "news/add_news.html"
    fields = "__all__"
    success_url = reverse_lazy("new news")


class NewsDeleteView(LoginRequiredMixin, DeleteView):

    model = AllNews
    fields = "__all__"
    template_name = "news/delete_news.html"
    success_url = reverse_lazy("new news")

