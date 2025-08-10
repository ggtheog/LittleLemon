from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Pizza", price=150, inventory=50)

    def test_get_all_menu_items(self):
        response = self.client.get('/menu-items/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
