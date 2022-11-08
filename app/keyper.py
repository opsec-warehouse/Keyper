#! /usr/bin/env python
""" Keyper - Secure Password Manager """

import keyperlib
import os, git, sys, json, getpass, argparse, consolemenu

mainCore = keyperlib.MainCore()
dataCore = keyperlib.DataCore()
guiCore = keyperlib.GUICore()
utilCore = keyperlib.UtilCore()

argsToParse = argparse.ArgumentParser(description="Keyper - Secure Password Manager | OpSec WareHouse LLC")

switchArgGroup = argsToParse.add_argument_group("[switches]")
switchArgGroup.add_argument("-v", "--verbose", action="store_true", help="stdout DEBUG responses")
switchArgGroup.add_argument("--update", action="store_true", help="pull latest updates from git repo")
switchArgGroup.add_argument("--gui", action="store_true", help="enable and display command line graphic user interface")

funArgGroup = argsToParse.add_argument_group("[main functions]")
funArgGroup.add_argument("--create", action="store_true", help="create a new database (initial run)")
funArgGroup.add_argument("--changepwd", action="store_true", help="change/update master database password")
funArgGroup.add_argument("--export", action="store_true", help="export all account credentials (USE CAUTION)")

dbFunArgGroup = argsToParse.add_argument_group("[db functions]")
dbFunArgGroup.add_argument("--add-alias", help="add a new auth alias (ex: test@example.com or username1)")
dbFunArgGroup.add_argument("--add-plat", help="add a new platform (ex: test@example.com:Proton)")
dbFunArgGroup.add_argument("--creds", help="stdout creds for email:platform (ex: test@example.com:Proton)")

"""
cmdArgGroup = argsToParse.add_argument_group("[stdin]")
cmdArgGroup.add_argument("-e", "--email", help="your email")
cmdArgGroup.add_argument("-w", "--website")
"""

"""
Possible Commands:

# Core
~$ python ./keyper.py --update
~$ python ./keyper.py --gui

# Main Fun
~$ python ./keyper.py --create # creates a new database
~$ python ./keyper.py --changepwd # change master db passwd
~$ python ./keyper.py --export # export all creds stored in db

# DB Fun
~$ python ./keyper.py --add_alias test@example.com | ~$ python ./keyper.py --add_alias username1
"""

argParsedObj = argsToParse.parse_args()

if __name__ == '__main__':
	utilCore.print_success("Welcome to {0} | {1}".format(keyperlib.__name__, keyperlib.__author__))
	utilCore.print_info("Current Version: 0x" + git.Repo(search_parent_directories=True).head.object.hexsha)
	print() # create whitespace

	# Core Functions
	if argParsedObj.verbose:
		keyperlib.__verbose__ = True
		utilCore.print_debug("Verbose is enabled.")
	if argParsedObj.update: utilCore.print_info(git.cmd.Git('./').pull()); sys.exit(utilCore.print_success("Successfully updated Keyper!"))

	# Initiate GUI
	if argParsedObj.gui: guiCore.displayGUI()

	# Main Functions
	if argParsedObj.create: mainCore.create()
	if argParsedObj.changepwd: mainCore.changepwd()
	if argParsedObj.export: mainCore.export()

	# DB Functions
	if argParsedObj.add_alias != None: mainCore.appendAlias(argParsedObj.add_alias)
	if argParsedObj.add_plat != None: mainCore.appendPlatform(argParsedObj.add_plat)
	if argParsedObj.creds != None: mainCore.extractCreds(argParsedObj.creds)