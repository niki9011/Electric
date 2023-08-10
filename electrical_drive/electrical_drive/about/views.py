from django.views import View
from django.shortcuts import render


class AboutView(View):
    template_name = 'about/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
