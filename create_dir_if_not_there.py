# Script Name   :	create_dir_if_not_there.py
# Author	    :  Duy khoa
# Created		: 27/06/2017
# Last Modified	: ..
# Version 	    : 1.0.1

import os		# import the Os module
MESSAGE = 'The directory alrady exists '
TESTDIR = 'Testdir'

try:
	home = os.path.expanduser("~") # Set the variable home by expanding the user's set home directory
	print(home)						# Print location
	if not os.path.exists(os.path.join(home,TESTDIR)): #os.path.join() for making a full path safely
		os.makedirs(os.path.join(home, TESTDIR)) # if not directory , inside their home directory
	else:
		print(MESSAGE)
except Exception as e:
	print(e)