import importlib
import os


class EscapeRoom:

    def __init__(self):
        self.levels = []
        self.room_name = "Unknown"
        self.author = "Unknown"
        self.last_solution = None

    def add_level(self, level):
        self.levels.append(level)

    def set_level(self, index, level):
        self.levels[index]=level

    def get_levels(self):
        return self.levels

    def get_level(self, number):
        return self.levels[number]

    def get_name(self):
        return self.room_name

    def set_metadata(self, author, room_name):
        self.room_name = room_name
        self.author = author

    def get_metadata(self):
        return {"author": self.author, "room_name": self.room_name, "levels": len(self.levels)}

    def get_last_solution(self):
        return self.last_solution

    def check_solution(self, solution_filename, correct_function, data):
        solution = self.run_code(solution_filename, data)
        self.last_solution = solution
        correct = solution == correct_function(data)
        return {"correct": correct, "solution": solution}

    def run_code(self, filename, data):
        try:
            mod = importlib.import_module(filename)
            importlib.reload(mod)
            if hasattr(mod, "run") and callable(getattr(mod, "run", None)):
                return mod.run(data)
            else:
                print(f"run() method not found.")
        except ModuleNotFoundError:
            print(f"Couldn't find: {os.getcwd()}/{filename}.")
            return False

