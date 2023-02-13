from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_create_menu(self):
        # create a new menu object
        menu = Menu.objects.create(title='Menu', price=20, inventory=15, menu_item_description='Menu item')

        # check that the string representation of the object is as expected
        self.assertEqual(str(menu), 'Menu')

        # check that the name, price, and description fields are set correctly
        self.assertEqual(menu.title, 'Menu')
        self.assertEqual(menu.price, 20)
        self.assertEqual(menu.inventory, 15)
        self.assertEqual(menu.menu_item_description, 'Menu item')