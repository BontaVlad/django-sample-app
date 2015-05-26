from django.test import TestCase, RequestFactory

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from home.views import CarPartsListCreateView


class SimpleTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_request_factory_get_request(self):
        request = self.factory.get('')
        graphviz = GraphvizOutput(output_file='get_parts.png')

        with PyCallGraph(output=graphviz):
            response = CarPartsListCreateView.as_view()(request=request)
        self.assertEqual(response.status_code, 200)
