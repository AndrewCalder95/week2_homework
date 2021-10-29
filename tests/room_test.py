import unittest
from classes.rooms import Room
from classes.guests import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Large Room", 18, 90)
        self.room2 = Room("Medium Room", 14, 55)
        self.room3 = Room("Small Room", 10, 40)
        self.room4 = Room('Mini Room', 7, 30)

        self.guest1 = Guest("Alexandrea", "Large Room")
        self.guest2 = Guest("Brenda", "Medium Room")
        self.guest3 = Guest("Callum", "Small Room")
        self.guest4 = Guest("David", "Mini Room")
        self.guest5 = Guest("Eva", "Large Room")
        self.guest6 = Guest("Frank", "Large Room") 

    def test_rooms_have_name(self):
        self.assertEqual("Large Room", self.room1.name)

    def test_rooms_have_capacity(self):
        self.assertEqual(14, self.room2.capacity)
    
    def test_rooms_have_cost(self):
        self.assertEqual(40, self.room3.cost_per_hour)

    def test_guest_checked_in(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest5)
        self.room1.check_in(self.guest6)
        self.assertEqual(3, len(self.room1.guests_in_room))

    def test_guest_checked_out(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest5)
        self.room1.check_in(self.guest6)
        self.room1.check_out(self.guest1)
        self.assertEqual(2, len(self.room1.guests_in_room))