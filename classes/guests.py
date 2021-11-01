import pdb 

class Guest:
    def __init__(self,name, room_choice, cash, favourite_song):
        self.name = name
        self.room_choice = room_choice
        self.cash = cash
        self.favourite_song = favourite_song

    def check_for_favourite_song(self, room):
        for x in room.playlist:
            if x.title == self.favourite_song:
                return "Yes! My favourite!!"