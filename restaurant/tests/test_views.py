from django.test import TestCase
from django.test import Client
from restaurant.views import home, BookingsViewSet
from rest_framework.test import force_authenticate, APIRequestFactory
from django.contrib.auth.models import User

class HomeViewTest(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

class BookingsTest(TestCase):
    def test_unauthorized_bookings_view(self):
        factory = APIRequestFactory()
        view = BookingsViewSet.as_view({'get': 'list'})
        request = factory.get('/api/bookings/')
        response = view(request)
        self.assertEqual(response.status_code, 401)