# Python Escape Room Game

These are the first steps for a new a project about learning Python with the help of some programming challenges.

# How to run



# How to create a new room

All rooms are Python classes in the 'rooms' folder.
They should all have an init method with the following code:

    def __init__(self):
        super().__init__()
        self.set_metadata("Your name", __name__)
        self.add_level(self.create_level1())
		self.add_level(self.create_level2())
		# add more levels like above
		
Have a look at the existing classes as a reference.