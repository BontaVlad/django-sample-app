#! /usr/bin/env python2.7
from django.views.generic import TemplateView, ListView, DetailView

from projectname.home.models import CarPart


class HomeView(TemplateView):
    template_name = 'home.html'


class HelpView(TemplateView):
    template_name = 'help.html'


class CarPartsListView(ListView):
    template_name = "list.html"
    model = CarPart


class CarPartDetailView(DetailView):
    template_name = "detail.html"
    model = CarPart
