#! /usr/bin/env python2.7
from django.views.generic import TemplateView, CreateView, DetailView

from projectname.home.models import CarPart
from projectname.home.parsers import AgmGroupParser


class HomeView(TemplateView):
    template_name = 'home.html'


class HelpView(TemplateView):
    template_name = 'help.html'


class CarPartsListCreateView(CreateView):
    template_name = "list.html"
    form_class = None
    parser_class = AgmGroupParser
    success_url = 'parts_list'
    model = CarPart

    def get_context_data(self, *args, **kwargs):
        kwargs['object_list'] = self.model.objects.order_by('id')
        return super(
            CarPartsListCreateView, self).get_context_data(*args, **kwargs)



class CarPartDetailView(DetailView):
    template_name = "detail.html"
    model = CarPart
