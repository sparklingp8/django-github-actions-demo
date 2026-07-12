from django.test import TestCase


class MathTest(TestCase):

    def test_addition(self):
        self.assertEqual(2 + 2, 4)
