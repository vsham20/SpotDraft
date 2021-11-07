# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Movies.objects.create(title="Movie1", created="2014-12-10T14:23:31.880Z",
#                               edited="2014-12-20T19:49:45.256Z", release_date="1977-05-25",
#                               url="https://swapi.dev/api/films/1/")
#         Movies.objects.create(title="Movie2", created="2014-11-10T14:23:31.880Z",
#                               edited="2014-11-20T19:49:45.256Z", release_date="1975-05-25",
#                               url="https://swapi.dev/api/films/2/")
#
#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Mo.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Movies


# Create your tests here.

class MoviesTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('MoviesView-get')
        data = {
            "title":"Test",
            "created":"2014-12-09T13:50:51.644000Z",
            "edited":"2014-12-10T13:52:43.172000Z",
            "url":"https://swapi.dev/api/movies/2/"
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movies.objects.count(), 1)
        self.assertEqual(Movies.objects.get().title, 'Test')