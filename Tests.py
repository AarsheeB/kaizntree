# inventory_app/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item

class ItemAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('item-list-create')

    def test_list_items(self):
        # Create some sample items for testing
        item1 = Item.objects.create(name='Item 1', quantity=10, price=20.0)
        item2 = Item.objects.create(name='Item 2', quantity=15, price=25.0)

        # Make a GET request to the API endpoint
        response = self.client.get(self.url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data contains the created items
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], item1.name)
        self.assertEqual(response.data[1]['name'], item2.name)

    def test_create_item(self):
        # Data for creating a new item
        new_item_data = {
            'name': 'New Item',
            'quantity': 5,
            'price': 15.0,
        }

        # Authenticate the client (if authentication is required)
        # For example, you can use Token authentication:
        # self.client.credentials(HTTP_AUTHORIZATION=f'Token {your_token}')

        # Make a POST request to the API endpoint to create a new item
        response = self.client.post(self.url, new_item_data, format='json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the new item is created in the database
        self.assertEqual(Item.objects.count(), 1)

        # Check if the response data matches the created item
        self.assertEqual(response.data['name'], new_item_data['name'])
        self.assertEqual(response.data['quantity'], new_item_data['quantity'])
        self.assertEqual(response.data['price'], new_item_data['price'])
