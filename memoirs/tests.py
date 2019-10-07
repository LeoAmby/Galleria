from django.test import TestCase
from .models import Image, Location, Category


class ImageTestClass(TestCase):
    def setUp(self):
        self.pic1=Image(photo = 'pic1', name = 'nice')

    def test_instance(self):
        self.assertTrue(isinstance(self.pic1,Image))