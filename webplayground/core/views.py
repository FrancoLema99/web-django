from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'title' : 'Web Django'})



class SamplePageView(TemplateView):
    template_name = 'core/sample.html'