import os
import importlib
import sys
sys.path.append('rooms')


class EscapeRoomGame:

    def __init__(self):
        self.rooms = []

    def load_room(self, room_classname):
        for room in self.rooms:
            if room.get_name() == room_classname:
                print("Already loaded.")
                return
        try:
            room_module = importlib.import_module(room_classname)
            class_ = getattr(room_module, room_classname)
            room = class_()
            self.rooms.append(room)
        except Exception as e:
            print("Could not load room: "+str(e))

    def load_all_rooms(self):
        self.reset()
        for room_file in self.find_rooms():
            self.load_room(room_file)

    def reset(self):
        self.rooms.clear()

    def find_rooms(self):
        return [f.split(".")[0] for f in os.listdir('rooms') if f.endswith(('.py', '.pyc'))]

    def get_rooms(self):
        return self.rooms

    def get_room(self, number):
        if(number < len(self.rooms)):
            return self.rooms[number]
        else:
            return None
