from django.test import TestCase
from .models import User

class HomeIntegrationTest(TestCase):

    def setUp(self):
        self.user = User(full_name="john smith")
        self.user.save()

        self.second_user = User(full_name="jane smith")
        self.second_user.save()


    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_text(self):
        response = self.client.get('/')
        self.assertTrue('jane smith' in response.content.lower())



class UserUnitTest(TestCase):

    def setUp(self):
        self.user = User(full_name="john smith")

    def test_uniform_name(self):
        self.assertEqual(self.user.uniform_name(), "John Smith")

    def test_capitalized_name(self):
        self.assertEqual(self.user.capitalize(), "JOHN SMITH")

    def test_slug_name(self):
        self.assertEqual(self.user.slug(), "john-smith")
