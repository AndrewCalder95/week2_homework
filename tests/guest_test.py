import unittest
from classes.guests import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Alexandrea")
        self.guest2 = Guest("Brenda")
        self.guest3 = Guest("Callum")
        self.guest4 = Guest("David")

    def test_guest_has_name(self):
        self.assertEqual("Brenda", self.guest2.name)
