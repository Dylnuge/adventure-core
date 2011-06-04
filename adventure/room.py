# Room Object for storing rooms and their data
# This software is licensed under the NCSA License. Details in LICENSE.txt
# Copyright 2011 Dylan Nugent. All rights reserved.

class Room:
	"""Simple room container.
	
	Persistent Variables:
	title - The title of the room
	desc - The description of the room
	exits - A dictionary mapping exit names to linked rooms
	items - A list of items in the room
	"""
	def __init__(self, title="Empty Room", desc="", exits={}, items=()):
		"""Initialize a room container

		Arguments:
		title - (default "Empty Room") Title for the room being created
		desc - (default "") Description for the room being created
		exits - (default empty) Dictionary mapping exit names to linked rooms
		items - (default empty) List of items in the room
		"""
		self.title = title
		self.desc = desc
		self.exits = exits
		self.items = items
