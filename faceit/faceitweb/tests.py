from django.test import TestCase
from .models import User

class HomeIntegrationTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_form(self):
        response = self.client.get('/')
        self.assertTrue('Your name:' in response.content.lower())

    def test_post_of_new_user(self):
        self.client.post('/register/', {'full_name': 'John Smith'})

        self.assertTrue(User.objects.first().filter(full_name='John Smith').id, 1)



class UserUnitTest(TestCase):

    def setUp(self):
        self.user = User(full_name="john smith")

    def test_uniform_name(self):
        self.assertEqual(self.user.uniform_name(), "John Smith")

    def test_capitalized_name(self):
        self.assertEqual(self.user.capitalize(), "JOHN SMITH")

    def test_slug_name(self):
        self.assertEqual(self.user.slug(), "john-smith")
