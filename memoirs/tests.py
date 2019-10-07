from django.test import TestCase
from .models import Image, Location, Category


class ImageTestClass(TestCase):
    def setUp(self):
        self.pic1=Image(photo = 'pic1', name = 'nice')

    def test_instance(self):
        self.assertTrue(isinstance(self.pic1,Image))

    def test_save_method(self):
        self.pic1.save_image()
        images = Image.objects.all.save()

    def tearDown(self):
        Image.objects.all.delete()


class LocationTest(TestCase):
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Location))
        

    def setUp(self):
        self.new_location.save()

    def tearDown(self):
        Location.objects.all.delete()


class CategoryTest(TestCase):
    def instance(self):
        self.assertTrue(isinstance(self.name, Category))

    def tearDown(self):
        Category.objects.all.delete()