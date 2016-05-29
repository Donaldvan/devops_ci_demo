from django.test import TestCase
from .models import User

class HomeIntegrationTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_form(self):
        response = self.client.get('/')
        self.assertTrue('your name:' in response.content.lower())

    def test_post_of_new_user(self):
        self.client.post('/register/', {'full_name': 'John Smith'})

        self.assertTrue(User.objects.filter(full_name='John Smith').first().id, 1)

class UserUnitTest(TestCase):

    def setUp(self):
        self.user = User(full_name="john smith")

    def test_uniform_name(self):
        self.assertEqual(self.user.uniform_name(), "John Smith")

    def test_capitalized_name(self):
        self.assertEqual(self.user.capitalize(), "JOHN SMITH")

    def test_slug_name(self):
        self.assertEqual(self.user.slug(), "john-smith")

# class UserIntegrationTest(TestCase):
#     '''Tests the user routes'''
#
#     def test_user_listing_index(self):
#         User(full_name="new user", bio="likes things and stuff").save()
#         User(full_name="newer user", bio="likes other things and other stuff").save()
#
#         response = self.client.get('/users/')
#
#         content = response.content.lower()
#
#         expected_strings = ["new user","likes things and stuff","newer",
#                             "likes other things and other stuff" ]
#
#         for string in expected_strings:
#             self.assertTrue(string in content)
