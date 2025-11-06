# Python Escape Room Game

Author: Markus M. Berg

These are the first steps for a new a project about learning Python with the help of some programming challenges.
The levels will be created by various contributors.

# Getting The Code

Download the Escape Room Environment from https://github.com/mmberg/pythonescaperoom by cloning the Git repository ``git clone https://github.com/mmberg/pythonescaperoom.git``

Hint: The Git command line interface for Windows can be downloaded from https://git-scm.com/downloads/win.
Hint: If you need to get updates later (e.g. after I fixed a bug), get them with ``git pull``.

# Prerequisites

Installed Python. Can be downloaded from https://www.python.org/downloads/.
If you already have Python installed, you can check the version with ``python --version``.

The Escape Room was initially created with Python 3.7.1 (64 bit) but should also work the newer versions. Also tested with 3.12.6. Latest tested version is 3.13.7.

If Python is not in your system's path, you might need to use the complete path to Python.
On Windows, it's recommended to set the path to Python (e.g. ``C:\Users\<user>\AppData\Local\Programs\Python\Python312\``) in the PATH environment variable (the installer usually already does that for you).

# Installation Requirements

If you don't already have all the requirements installed, please install them by running ``pip install -r requirements.txt``.
Currently, that's only Flask, so alternatively you can also install it manually via ``pip install flask``.

Hint: You may want to use a virtual environment to manage contradicting module dependencies from different programs (e.g. if you already use Python and have programms that require different versions of the same modules)
Create environment: ``python -m venv venv``
Load envoronment: ``venv\Scripts\activate.bat``

# How To Run

Just start ``EscapeRoomWeb.py`` or use the batch file start.bat (on Windows) or start.sh (Linux). This will start a web server on http://localhost:5000 (not https!). Please open this URL in your web browser to start the game.
This should work with all browsers (tested with Edge, Firefox, and Chrome).

Select the ExampleRoom and play the first level.

# How To Create a Solution (As A Player)

As a player you will have to develop little algorithms in Python with your favorite editor (which you store locally) to solve the challenges. For every level you have to create a .py-file with a method called ``run`` and one parameter. For the sake of simplicity you can use the existing ``solutions`` folder to save your code.

Minimal example without functionality:

	def run(secret):
		pass

The parameter can be called as you like, e.g. ``secret``, ``data`` or ``input_data``. The Escape Room environment will use it to pass the secret information defined in any room (see ``data`` in ExampleRoom) to your solution function. You can then create your algorithm that uses the secret as input and return the solution.

	def run(secret):
		solution = do_some_magic(secret)
		return solution
		

You can then upload the .py-file and check your solution.

		
# How To Create a New Room (As A Developer)

A room can consist of different levels. Consider each room a different game, while each level is a step towards solving the game.
As a developer you need to create new rooms and levels. All rooms are Python classes in the 'rooms' folder (make sure to put any new room into this folder).
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
* hints: the user can request help messages that point him towards the correct solution (hints are revealed one after another upon mouse click)
* solution_function: the function that will be called in order to verify the user's solution
	* Note: this is really just the name of the function, i.e. without parantheses
* data: the secret/data that is passed to the solution_function as first parameter
    * i.e. if the user has to decode a secret, this is the secret that the user should work on
    * e.g. if the user shall extract the first letter of each word within a sentence, then the sentence is the data that the user should work on
    * It makes sense to create these secrets dynamically so that the solution changes every time we run the game.
* When running the game, the framework will call the method defined as solution_function and pass data as first argument, i.e. self.first_letters(secret)

Have a look at the existing classes as a reference.

## Adding Static Content

If you want to display images, put them into folder ``/static`` and include them into the HTML page by adding ``<img src='static/secret.jpg'/>`` to the task_messages.

## Passing Data From One Level to Another

You can call ``self.get_last_solution()`` in order to retrieve the solution from the last level and use it for the current level.
If you want to use this function, please adjust the way how you add levels to the room. Instead of:

	self.add_level(self.create_level1())
	self.add_level(self.create_level2())
	...

... you have to write:

	self.add_level(self.create_level1)
	self.add_level(self.create_level2)
	...

Omitting the parantheses just passes the name of the level/method without directly creating/running it. This way, we make sure that the code only runs at the time when the user actually arrives at the respective level.
With parantheses, the level would be constructed at the time when the game is started, i.e. before the user actually plays the level. At this time, the last_solution would not be available yet.

Please have a look at the DynamicRoom for a working example.

# General Remarks

It is not needed to modify the Escape Room environment (i.e. EscapeRoom.py, EscapeRoomGame.py, EscapeRoomWeb.py, escape.css, escape.js, escape.html), but if you really feel the need to change something, it's not forbidden.
