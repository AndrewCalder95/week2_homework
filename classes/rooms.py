from classes.guests import Guest

class Room:

    def __init__(self, name, capacity, cost_per_hour):
        self.name = name
        self.capacity = capacity
        self.cost_per_hour = cost_per_hour
        self.guests_in_room = []

    def check_in(self, guest):
        if guest.room_choice == self.name:
            return self.guests_in_room.append(guest.name)

    def check_out(self, guest):
        for x in self.guests_in_room:
            if x == guest.name:
                return self.guests_in_room.remove(guest.name)

