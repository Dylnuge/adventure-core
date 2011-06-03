#! /usr/bin/env python3
# A simple shell interface for Adventure Core
# This software is licensed under the NCSA License. Details in LICENSE.txt
# Copyright 2011 Dylan Nugent. All rights reserved.

import textwrap

# Declares whether debugging signals should be used within shell.py
# For semantic reasons, a -O compile will override DEBUG to false
DEBUG = True
if __debug__ == False:
	DEBUG = False

class ShellInterface:

	"""Class for a very simple shell interface."""

	shellname = "Adventure Core Testing Shell ver. NaN"
	initmessage = """\
		Copyright (c) 2011 Dylan Nugent. All Rights Reserved.
		This program is licensed freely under the NCSA license.
		Source code is available, and a copy of the license should be included.
	"""
	initmessage = textwrap.dedent(initmessage)
	prompt = "command> "
	case_insensitive = True
	command_list = {}
	alias_list = {}

	def __init__(self):
		"""Initializes the shell interface.

		Loads shell builtins and prints the initialization (welcome)
		message for the shell.
		"""

		print(self.shellname)
		print(self.initmessage)
		if DEBUG:
			print("Debug mode is active. Bumpy road ahead.")
		
		self.load()
		self.running = False

	def run(self):
		"""Begins running the shell interface.

		Note that this will take over an application until run terminates.
		"""

		self.running = True

		while(self.running):
			indata = self.get_command()
			try:
				self.process_command(indata)
			except NotImplementedError:
				print("Error: Command not yet implemented")
			except KeyError as e:
				print("Error: {}".format(e))

	def load(self):
		"""Load up the commands for the shell interface."""

		# TODO: Come up with a better way to do this than hardcoded commands
		self.command_list["help"] = "Display this help message"
		self.command_list["quit"] = "Exit the shell"
		self.command_list["load"] = "Load an Adventure Core game into the shell"
		self.alias_list["q"] = "quit"
		self.alias_list["exit"] = "quit"

	def get_command(self):
		"""Display a shell prompt and get the command from it"""

		command = input(self.prompt)
		if self.case_insensitive:
			command = command.lower()

		return command

	def process_command(self, linein):
		"""Process a command on the active shell
		
		Arguments:
		linein - The command to be processed
		"""

		# For now, it's a hard coded limitation that a command must be
		# distinguished by its first word alone, and all following data
		# is to be treated as an argument to the command
		command = linein.split()[0]
		args = linein.split()[1:]
		if(command in self.alias_list):
			command = self.alias_list[command]

		if(command in self.command_list):
			# Process the command, currently manual
			if(command == "help"):
				if args == []:
					self.print_help()
				else:
					self.print_help(args[0])
			elif(command == "quit"):
				self.running = False
			else:
				raise NotImplementedError()
		else:
			raise KeyError("No such command")

	def print_help(self, command="shell"):
		"""Access the help system and print the requested help to the shell.

		Arguments:
		command - (default: shell) The command to get help on. If command is
			'shell', prints help on all shell commands.
		"""
		if command == "shell":
			print()
			print(self.shellname)
			print("Shell commands:")
			for command in self.command_list:
				print(command, ": ", self.command_list[command], sep="")
			print()
		elif command in self.command_list:
			print(command, ": ", self.command_list[command], sep="")
		else:
			print("No help for that command")


# For current testing purposes, allow the shell to be run directly
if __name__ == '__main__':
	if DEBUG:
		print("WARNING: Running non fully implemented shell")
		print("Quit with 'quit'")
		print()
	
	shell = ShellInterface()
	shell.run()
