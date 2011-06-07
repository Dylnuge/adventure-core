# Game Object for storing individual game data
# This software is licensed under the NCSA License. Details in LICENSE.txt
# Copyright 2011 Dylan Nugent. All rights reserved.

from adventure.room import Room

class Game:
	"""Simple game control object.

	Attributes:
	name - The name of the current game
	current - The current room object for the player
	"""
	def __init__(self, name="Sample Game"):
		self.name = name
		self.roomlist = ()
		# Testing, let's init a few sample rooms in our sample game
		# This is hardcoded for *testing* purposes only
		# TODO: Remove at next revision checkin
		mainroom = Room(title="Main Room", desc="A pretty bare room")
		secondroom = Room(title="Another Room", desc="Not much more to see.")
		mainroom.exits["north"] = secondroom
		# secondroom.exits["south"] = mainroom
		self.current = mainroom
		self.roomlist = (mainroom, secondroom)

	def display_room(self, room="current"):
		"""Returns a string for displaying the given room.

		Arguments:
		room - (default: the current room) Room to display
		"""
		if(room == "current"):
			room = self.current
		roomstr = ""
		roomstr += room.title + '\n' + '\n' + room.desc
		roomstr += '\n' + "Exits are:"
		for exit in room.exits:
			roomstr += ' ' + exit
		return roomstr
