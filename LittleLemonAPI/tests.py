from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import MenuItem
from django.contrib.auth.models import User

class MenuItemTests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)  # Auto login for tests

        # Create a sample menu item
        MenuItem.objects.create(title="Pizza", price=9.99, inventory=10)

    def test_get_menu_items(self):
        url = reverse('menuitems')  # Use the correct name of the route if available
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Pizza')

    def test_post_menu_item(self):
        url = '/api/menu-items/'
        data = {
            'title': 'Burger',
            'price': 5.99,
            'inventory': 20
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 2)
        self.assertEqual(MenuItem.objects.last().title, 'Burger')

