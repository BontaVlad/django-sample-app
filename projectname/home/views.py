#! /usr/bin/env python2.7
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView

from projectname.home.models import CarPart
from projectname.home.parsers import AgmGroupParser


class HomeView(TemplateView):
    template_name = 'home.html'


class HelpView(TemplateView):
    template_name = 'help.html'


class CarPartsListCreateView(CreateView):
    template_name = "list.html"
    parser_class = AgmGroupParser
    success_url = 'parts_list'
    model = CarPart

    def get_context_data(self, *args, **kwargs):
        kwargs['object_list'] = self.model.objects.order_by('id')
        return super(
            CarPartsListCreateView, self).get_context_data(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.model.objects.make_objects(self.parser_class().parse())
        return render(request, self.success_url, self.get_context_data())


class CarPartDetailView(DetailView):
    template_name = "detail.html"
    model = CarPart
