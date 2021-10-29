import unittest
from classes.guests import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Alexandrea", "Large Room")
        self.guest2 = Guest("Brenda", "Medium Room")
        self.guest3 = Guest("Callum", "Small Room")
        self.guest4 = Guest("David", "Mini Room")

    def test_guest_has_name(self):
        self.assertEqual("Brenda", self.guest2.name)

    def test_guest_has_room_choice(self):
        self.assertEqual("Large Room", self.guest1.room_choice)

    
