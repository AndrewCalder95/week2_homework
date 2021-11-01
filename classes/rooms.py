class Room:

    def __init__(self, name, capacity, cost):
        self.name = name
        self.capacity = capacity
        self.cost = cost
        self.playlist = []
        self.guests_in_room = []
        self.till = 0

    def check_in(self, guest):
        if guest.room_choice == self.name:
            if len(self.guests_in_room) > self.capacity:
                return "Sorry this room is full."
            else:
                if guest.cash >= self.cost:
                    guest.cash -= self.cost
                    self.till += self.cost
                    self.guests_in_room.append(guest.name)
                else:
                    return "You have insufficient funds"

    def check_out(self, guest):
        for x in self.guests_in_room:
            if x == guest.name:
                return self.guests_in_room.remove(guest.name)

    def add_to_room_playlist(self,song):
        return self.playlist.append(song)

    
