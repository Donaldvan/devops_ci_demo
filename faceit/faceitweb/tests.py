from django.test import TestCase

class RouteTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_text(self):
        response = self.client.get('/')
        self.assertTrue('coming soon' in response.content.lower())
