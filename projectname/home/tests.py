from django.test import TestCase, RequestFactory

from home.views import CarPartsListCreateView


class SimpleTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_request_factory_get_request(self):
        request = self.factory.get('')
        response = CarPartsListCreateView.as_view()(request=request)
        self.assertEqual(response.status_code, 200)
