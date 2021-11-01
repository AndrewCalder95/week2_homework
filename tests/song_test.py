import unittest
from classes.songs import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Purple Rain")
        self.song2 = Song("Love Shack")
        self.song3 = Song("Bohemian Rhapsody")
        self.song4 = Song("Islands in the Stream")
        self.song5 = Song("Africa")
        self.song6 = Song("Someone Like You")



    def test_song_has_title(self):
        self.assertEqual("Bohemian Rhapsody", self.song3.title)