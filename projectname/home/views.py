#! /usr/bin/env python2.7
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from projectname.home.models import CarPart
from projectname.home.parsers import AgmGroupParser


class HomeView(TemplateView):
    template_name = 'home.html'


class HelpView(TemplateView):
    template_name = 'help.html'


class CarPartsListCreateView(ListView):
    template_name = "list.html"
    parser_class = AgmGroupParser
    success_url_name = 'parts_list'
    model = CarPart

    def post(self, request, *args, **kwargs):
        self.model.objects.make_objects(self.parser_class().parse())
        return redirect(self.success_url_name)


class CarPartDetailView(DetailView):
    template_name = "detail.html"
    model = CarPart
