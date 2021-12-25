# import unittest

# class AddTestCase(unittest.TestCase):
from django.test import TestCase
from .models import Stores

class AddTestCase(TestCase):
    def test_fields(self):
        store=Stores()
        store.name='Table'
        store.code='mno'
        store.active=1
        store.quantity=4
        store.type='Wood'
        store.gst=6.00
        store.price=60
        store.save()
        record= Stores.objects.get(pk=11)

        self.assertEqual(record,store)

# from django.test import TestCase
# from .models import Stores

# class AddTestCase(TestCase):
#     def test_fields(self):
#         store=Stores()
#         store.name='Pizza'
#         store.code='mnop'
#         store.active=1
#         store.quantity=67
#         store.type='Junk Food'
#         store.gst=3.00
#         store.price=890
#         store.save()
#         record= Stores.objects.get(pk=12)

#         self.assertEqual(record,store)

    # def setup(self):
    #     Stores.objects.create(name='Pizza',code='mnop', active=1, quantity=67, type='Junk Food', gst=3.00, price=890)

    # def test_store_test(self):
    #     store1=Stores.objects.get(name='Pizza',code='mnop', active=1, quantity=67, type='Junk Food', gst=3.00, price=890)
    #     self.assertEqual(store1.name,"Pizza" )

# # class UpdateTestCase(TestCase):

# # class DeleteTestCase(TestCase):

# # class ShowTestCase(TestCase):

# # Create your tests here.




# from rest_framework.test import APIClient

# class TestModel1Api(unittest.TestCase):

#     def setUp(self):
#         self.client = APIClient()

#     def test_Model1_list(self):
#         response = self.client.get(reverse('Stores-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_Model1_detail(self):
#         mm_objs = Stores.objects.all()
#         if mm_objs:
#             response = self.client.get(reverse('Stores-detail', args=[mm_objs[0].id]))
#             self.assertEqual(response.status_code, status.HTTP_200_OK)