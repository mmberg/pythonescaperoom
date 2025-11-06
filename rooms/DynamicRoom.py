import random
import string
from EscapeRoom import EscapeRoom


class DynamicRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Markus", __name__)
        #self.add_level(self.create_level1())
        #self.add_level(self.create_level2())
        #self.add_level(self.create_level3())

        self.add_level(self.create_level1)
        self.add_level(self.create_level2)
        self.add_level(self.create_level3)

    ### LEVELS ###

    def create_level1(self):
        print("Level 1 created")
        secret = "hallo"
        task_messages = [
            "Level 1"
        ]
        hints = [
            "Nichts"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.double_solution, "data": secret}

    def create_level2(self):
        print("Level 2 created")
        last_solution = self.get_last_solution()
        task_messages = [
            "Level 2"
        ]
        hints = [
            "Nichts"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.double_solution, "data": last_solution}

    def create_level3(self):
        print("Level 3 created")
        last_solution = self.get_last_solution()
        task_messages = [
            "Level 3"
        ]
        hints = [
            "Nichts"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.double_solution, "data": last_solution}

    ### SOLUTIONS ###

    def double_solution(self, secret):
        return secret+secret
