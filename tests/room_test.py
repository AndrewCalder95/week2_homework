import unittest
from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guest("Alexandrea", "Large Room", 120, "Bohemian Rhapsody")
        self.guest2 = Guest("Brenda", "Medium Room", 140, "Love Shack")
        self.guest3 = Guest("Callum", "Small Room", 35, "Purple Rain")
        self.guest4 = Guest("David", "Mini Room", 160, "Islands in the Stream")
        self.guest5 = Guest("Eva", "Large Room", 114, "Africa")
        self.guest6 = Guest("Frank", "Large Room", 178, "Someone like you") 
        self.guest7 = Guest("Gary", "Medium Room", 130, "R U Mine")
        self.guest8 = Guest("Hannah", "Mini Room", 190, "Hello")

        self.song1 = Song("Purple Rain")
        self.song2 = Song("Love Shack")
        self.song3 = Song("Bohemian Rhapsody")
        self.song4 = Song("Islands in the Stream")
        self.song5 = Song("Africa")
        self.song6 = Song("Someone Like You")


        self.room1 = Room("Large Room", 4, 90)
        self.room2 = Room("Medium Room", 3, 55)
        self.room3 = Room("Small Room", 2, 40)
        self.room4 = Room('Mini Room', 1, 30)

    def test_rooms_have_name(self):
        self.assertEqual("Large Room", self.room1.name)

    def test_rooms_have_capacity(self):
        self.assertEqual(3, self.room2.capacity)
    
    def test_rooms_have_cost(self):
        self.assertEqual(40, self.room3.cost)

    def test_guest_checked_in(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest5)
        self.room1.check_in(self.guest6)
        self.assertEqual(3, len(self.room1.guests_in_room))

    def test_guest_checked_out(self):
        self.room2.check_in(self.guest1)
        self.room1.check_in(self.guest5)
        self.room1.check_in(self.guest6)
        self.room1.check_out(self.guest1)
        self.assertEqual(2, len(self.room1.guests_in_room))

    def test_guest_checked_out2(self):
        self.room2.check_in(self.guest2)
        self.room2.check_in(self.guest7)
        self.room2.check_out(self.guest2)
        self.assertEqual(1, len(self.room2.guests_in_room))

    def test_add_song_to_playlist(self):
        self.room1.add_to_room_playlist(self.song1)
        self.assertEqual(1, len(self.room1.playlist))

    def test_guest_rejected_if_room_too_busy(self):
        self.room4.check_in(self.guest4)
        self.room4.check_in(self.guest8)
        self.assertEqual("Sorry this room is full.", self.room4.check_in(self.guest8))
    
    def test_takes_payment_from_guest(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(30, self.guest1.cash)

    def test_adds_payment_to_till(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(90, self.room1.till)

    def test_insufficent_funds_warning(self):
        self.room3.check_in(self.guest3)
        self.assertEqual("You have insufficient funds", self.room3.check_in(self.guest3))