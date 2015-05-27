from django.test import TestCase, RequestFactory

from home.views import CarPartsListCreateView


class SimpleTest(TestCase):
    fixtures = ['database_dump', ]

    def setUp(self):
        self.factory = RequestFactory()

    def test_parts_page_get_request(self):
        request = self.factory.get('')
        response = CarPartsListCreateView.as_view()(request=request)
        self.assertEqual(response.status_code, 200)

    def test_parts_page_post_request(self):
        request = self.factory.post('')
        response = CarPartsListCreateView.as_view()(request=request)
        self.assertEqual(response.status_code, 302)
