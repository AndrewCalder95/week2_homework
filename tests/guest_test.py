import unittest
from classes.guests import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Alexandrea", "Large Room", 20)
        self.guest2 = Guest("Brenda", "Medium Room", 40)
        self.guest3 = Guest("Callum", "Small Room", 65)
        self.guest4 = Guest("David", "Mini Room", 20)
        self.guest5 = Guest("Eva", "Large Room", 14)
        self.guest6 = Guest("Frank", "Large Room", 78) 
        self.guest7 = Guest("Gary", "Medium Room", 30)
        self.guest8 = Guest("Hannah", "Mini Room", 48)


    def test_guest_has_name(self):
        self.assertEqual("Brenda", self.guest2.name)

    def test_guest_has_room_choice(self):
        self.assertEqual("Large Room", self.guest1.room_choice)

    def test_guest_has_cash(self):
        self.assertEqual(40, self.guest2.cash)