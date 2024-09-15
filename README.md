# Python Escape Room Game

Author: Markus M. Berg

These are the first steps for a new a project about learning Python with the help of some programming challenges.
The levels will be created by various contributors.

# How to run

Just start ``EscapeRoomWeb.py`` or use the batch file start.bat (on Windows) or start.sh (Linux). This will start a web server on http://localhost:5000 (not https!). Please open this URL in your web browser to start the game.

If Python is not in your system's path, you might need to use the complete path to python.
On Windows, it's recommended to set the path to Python (e.g. ``C:\Users\<user>\AppData\Local\Programs\Python\Python312\``) in the PATH environment variable.

# Install requirements

If you don't already have all the requirements installed, please do so by running ``pip install -r requirements.txt``.
Currently, that's only Flask, so you can also install it manually via ``pip install flask``.

Note: The Escape Room was initially created with Python 3.7.1 (64 bit) but should also work the newer versions. Latest tested version is 3.12.6.
Hint: You may want to use a virtual environment to manage contradicting dependencies of different programs.

# How to create a solution

As a player you will have to develop little algorithms in Python with your favorite editor (which you store locally) to solve the challenges. For every level you have to create a .py-file with a method called ``run`` and one parameter.

Minimal example without functionality:

	def run(secret):
		pass

The parameter can be called as you like, e.g. ``secret``, ``data`` or ``input_data``. The Escape Room environment will use it to pass the secret information defined in any room (see ``data`` in ExampleRoom) to your solution function. You can then create your algorithm and return the solution.

	def run(secret):
		solution = do_some_magic(secret)
		return solution
		
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
		
Every level needs to return the following data structure:

 	return {"task_messages": task_messages, "hints": hints, "solution_function": self.first_letters, "data": secret}

* task_messages: description of the task the user has to work on; can consist of several steps
* hints: the user can request help messages that point him towards the correct solution
* solution_function: the function that will be called in order to verify the user's solution
* data: the secret/data that is passed to the solution_function as first parameter (e.g. if the user has to decode a secret, this is the secret that the user should work on. It makes sense to create these secrets dynamically so that the solution changes every time we run the game.)

Have a look at the existing classes as a reference.

