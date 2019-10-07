from django.test import TestCase
from .models import Image, Location, Category


class ImageTestClass(TestCase):
    def setUp(self):
        