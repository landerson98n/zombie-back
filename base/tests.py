# api/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Survivor

class SurvivorAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.survivor_data = {
            'name': 'Jane Doe',
            'age': 25,
            'sex': 'Female',
            'latitude': 40.712776,
            'longitude': -74.005974,
            'infected': False
        }
        self.survivor = Survivor.objects.create(**self.survivor_data)

    def test_add_survivor(self):
        response = self.client.post('/api/survivors/', self.survivor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survivor.objects.count(), 2)

    def test_list_survivors(self):
        response = self.client.get('/api/survivors/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_location(self):
        new_location = {'latitude': 37.774929, 'longitude': -122.419418}
        response = self.client.patch(f'/api/survivors/{self.survivor.id}/', new_location, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['latitude'], 37.774929)
        self.assertEqual(response.data['longitude'], -122.419418)

    def test_mark_infected(self):
        response = self.client.patch(f'/api/survivors/{self.survivor.id}/', {'infected': True}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['infected'], True)
