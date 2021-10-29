import unittest
from classes.songs import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Purple Rain", "Prince")
        self.song2 = Song("Love Shack", "The B-52s")
        self.song3 = Song("Bohemian Rhapsody", "Queen")
        self.song4 = Song("Islands in the Stream", "Kenny Rogers and Dolly Parton")
        self.song5 = Song("Africa", "Toto")
        self.song6 = Song("Someone Like You", "Adele")



    def test_song_has_title(self):
        self.assertEqual("Bohemian Rhapsody", self.song3.title)
        
    def test_song_has_artist(self):
        self.assertEqual("Toto", self.song5.artist)





