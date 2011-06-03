#! /usr/bin/env python3
# Initial workings of the shell interface
# This software is licensed under the NCSA License. Details in LICENSE.txt
# Copyright 2011 Dylan Nugent. All rights reserved.

# Declares whether debugging signals should be used within shell.py
# For semantic reasons, a -O compile will override DEBUG to false
DEBUG = True
if __debug__ == False:
	DEBUG = False

class ShellInterface:

	"""Class for a very simple shell interface."""

	initmessage = """\
Adventure Core Testing Shell
Copyright (c) 2011 Dylan Nugent. All Rights Reserved.
This program is licensed freely under the NCSA license.
Source code is available, and a copy of the license should be included.
	"""
	prompt = "command> "
	case_insensitive = True

	def __init__(self):
		"""Initializes the shell interface.

		Prints the initialization (welcome) message for the shell.
		"""

		print(self.initmessage)
		if DEBUG:
			print("Debug mode is active. Bumpy road ahead.")
		
		self.running = False

	def run(self):
		"""Begins running the shell interface.

		Note that this will take over an application until run terminates.
		"""
		self.running = True

		exit = False
		while(not exit):
			command = self.get_command()
			# TODO: Replace this with logic in process_command()
			if(command == "quit"):
				exit = True
			self.process_command(command)

	def get_command(self):
		"""Display a shell prompt and get the command from it"""
		command = input(self.prompt)
		if self.case_insensitive:
			command = command.lower()

		return command

	def process_command(self, command):
		"""Process a command on the active shell
		
		Arguments:
		command - The command to be processed"""
		pass


# For current testing purposes, allow the shell to be run directly
if __name__ == '__main__':
	if DEBUG:
		print("WARNING: Running non fully implemented shell")
		print("Quit with 'quit'")
		print()
	
	shell = ShellInterface()
	shell.run()
