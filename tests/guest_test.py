import unittest
from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Alexandrea", "Large Room", 120, "Bohemian Rhapsody")
        self.guest2 = Guest("Brenda", "Medium Room", 140, "Love Shack")
        self.guest3 = Guest("Callum", "Small Room", 35, "Purple Rain")
        self.guest4 = Guest("David", "Mini Room", 160, "Islands in the Stream")
        self.guest5 = Guest("Eva", "Large Room", 114, "Africa")
        self.guest6 = Guest("Frank", "Large Room", 178, "Someone like you") 
        self.guest7 = Guest("Gary", "Medium Room", 130, "R U Mine")
        self.guest8 = Guest("Hannah", "Mini Room", 190, "Hello")

        self.room1 = Room("Large Room", 4, 90)

        self.song1 = Song("Bohemian Rhapsody")

    def test_guest_has_name(self):
        self.assertEqual("Brenda", self.guest2.name)

    def test_guest_has_room_choice(self):
        self.assertEqual("Large Room", self.guest1.room_choice)

    def test_guest_has_cash(self):
        self.assertEqual(140, self.guest2.cash)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Hello", self.guest8.favourite_song)
    
    def test_guest_reacts_to_favourite_song(self):
        self.room1.add_to_room_playlist(self.song1)
        self.assertEqual("Yes! My favourite!!", self.guest1.check_for_favourite_song(self.room1))