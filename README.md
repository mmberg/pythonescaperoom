# Python Escape Room Game

Author: Markus M. Berg

These are the first steps for a new a project about learning Python with the help of some programming challenges.
The levels will be created by various contributors.

# How to run

Just start ``EscapeRoomWeb.py`` or use the batch file start.bat (on Windows). This will start a web server on http://localhost:5000. Please open this URL in your web browser to start the game.

# How to create a solution

As a player you will have to develop little algorithms in Python with your favorite editor (which you store locally) to solve the challenges. For every level you have to create a .py-file with a method called ``run`` and one parameter.

	def run(secret):
		pass
		
You can then upload the .py-file and check your solution.
		
# How to create a new room

As a developer you may want to create new rooms and levels. All rooms are Python classes in the 'rooms' folder.
They should be derived from class ``EscapeRoom``:

	class AnotherRoom(EscapeRoom):

And they must have an ``init`` method with the following code:
    
		def __init__(self):
			super().__init__()
			self.set_metadata("Your name", __name__)
			self.add_level(self.create_level1())
			self.add_level(self.create_level2())
			# add more levels like above
		
Have a look at the existing classes as a reference.

