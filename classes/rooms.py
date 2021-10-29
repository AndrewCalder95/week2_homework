from classes.guests import Guest
from classes.songs import Song

class Room:

    def __init__(self, name, capacity, cost_per_hour):
        self.name = name
        self.capacity = capacity
        self.cost_per_hour = cost_per_hour
        self.playlist = []
        self.guests_in_room = []

    def check_in(self, guest):
        if guest.room_choice == self.name:
            return self.guests_in_room.append(guest.name)

    def check_out(self, guest):
        for x in self.guests_in_room:
            if x == guest.name:
                return self.guests_in_room.remove(guest.name)

    def add_to_room_playlist(self,song):
        return self.playlist.append(song)

    # def check_capacity(self):
    #     if self.capacity > self.guests_in_room:
    #         return ("Sorry there are too many people to fit in this room")
    #     else

    def check_in_with_capacity_check(self, guest):
        if guest.room_choice == self.name:
            if len(self.guests_in_room) > self.capacity:
                return "Sorry there are too many people in this room!"
            else:
                return self.guests_in_room.append(guest.name)