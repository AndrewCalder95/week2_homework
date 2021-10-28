import unittest
from classes.rooms import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Large Room", 18, 90)
        self.room2 = Room("Medium Room", 14, 55)
        self.room3 = Room("Small Room", 10, 40)
        self.room4 = Room('Mini Room', 7, 30)

    def test_rooms_have_name(self):
        self.assertEqual("Large Room", self.room1.name)

    def test_rooms_have_capacity(self):
        self.assertEqual(14, self.room2.capacity)
    
    def test_rooms_have_cost(self):
        self.assertEqual(40, self.room3.cost_per_hour)