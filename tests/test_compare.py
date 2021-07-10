from unittest import TestCase

import cv2
from PIL import Image

import image_comparer

class TestCompare(TestCase):

    def setUp(self):
        self.image = Image.open("tests/images/kobe.jpg")
        self.image2 = cv2.imread("tests/images/kobe2.jpg")

    def test_compare_success(self):
        assert not image_comparer.is_similar(self.image, self.image2)
        assert image_comparer.is_similar(self.image, self.image)
