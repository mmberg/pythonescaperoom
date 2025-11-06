import os
import importlib
import sys
from EscapeRoom import EscapeRoom

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

    def is_room_type(self, room_file):
        """
        Very naive check if file is an Escape Room without inspecting object.
        """
        is_room = False
        with open(room_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file.readlines():
                if "(EscapeRoom):" in line:
                    return True

    def find_rooms(self, root_folder="rooms", recursive=False):
        rooms = []
        if os.path.exists(root_folder):
            if not recursive:
                rooms.extend([f.split(".")[0] for f in os.listdir(root_folder) if f.endswith('.py') and self.is_room_type(os.path.join(root_folder, f))])
                sys.path.append(root_folder)
            else:
                for root, dirs, files in os.walk(root_folder):
                    if "__pycache__" in root: continue
                    room_file_names = [f.split(".")[0] for f in files if f.endswith('.py')]
                    for room in room_file_names:
                        if self.is_room_type(os.path.join(root,room+".py")):
                            rooms.append(room)
                    sys.path.append(root)
        else:
            print(f"Room folder '{root_folder}' does not exist.")

        if len(rooms)==0:
            print("No rooms found.")

        return rooms

    def get_rooms(self):
        return self.rooms

    def get_room(self, number):
        if(number < len(self.rooms)):
            return self.rooms[number]
        else:
            return None
