import keyperlib
import os, sys, json, getpass

class MainCore(object):
	"""
		KeyperLib | MainCore
	"""

	def __init__(self, *args, **kwargs):
		self.dataCore = keyperlib.DataCore()
		self.utilCore = keyperlib.UtilCore()

	""" START MAIN FUNCTIONS """

	def create(self):
		if os.path.isfile(keyperlib.__database__): self.utilCore.print_error("Database already exists - cancelling operation.")

		masterDBPasswd = getpass.getpass("Master Database Password => ")
		masterDBPasswdConf = getpass.getpass("Master Database Password (Confirm) => ")
		
		print()

		if masterDBPasswd == masterDBPasswdConf:
			if self.dataCore.createDatabase(masterDBPasswd):
				utilCore.print_success("Database Created Successfully!")
		
		sys.exit(0)

	def changepwd(self):
		self.utilCore.checkDBExists()
			
		currentPasswd = getpass.getpass("Current Master Database Password => ")
		updatedPasswd = getpass.getpass("Updated Master Database Password => ")
			
		print()
		
		self.utilCore.print_info("Updating password.. this might take a minute...\n")
		if self.dataCore.changeDBPasswd(currentPasswd, updatedPasswd):
			self.utilCore.print_success("Master Database Password Changed Successfully!")
		
		sys.exit(0)

	def export(self):
		self.utilCore.checkDBExists()
		self.utilCore.print_warning("This function will export the ENTIRE DATABASE. Please use with CAUTION!\n")

		masterDBPasswd = getpass.getpass("Master Database Password => "); print()

		print(self.dataCore.exportDatabase(masterDBPasswd))


	""" END MAIN FUNCTIONS """

	# --------------------------------------------------

	""" START DB FUNCTIONS """

	def appendAlias(self, tarAlias):
		self.utilCore.checkDBExists()

		masterDBPasswd = getpass.getpass("Master Database Password => "); print()

		databaseObj = json.loads(self.dataCore.exportDatabase(masterDBPasswd))
		databaseObj[tarAlias] = {} # append alias

		if self.dataCore.pushDBContents(masterDBPasswd, json.dumps(databaseObj)):
			self.utilCore.print_success("Added '{0}' to database successfully!".format(tarAlias))

	# --------------------------------------------------

	def appendPlatform(self, credCombo):
		self.utilCore.checkDBExists()

		masterDBPasswd = getpass.getpass("Master Database Password => "); print()

		databaseObj = json.loads(self.dataCore.exportDatabase(masterDBPasswd))

		tarAlias, tarPlat = credCombo.split(":")

		targetAPCred = getpass.getpass("Password for {0} @ {1} => ".format(tarAlias, tarPlat)); print()
		databaseObj[tarAlias][tarPlat] = targetAPCred # append alias

		if self.dataCore.pushDBContents(masterDBPasswd, json.dumps(databaseObj)):
			self.utilCore.print_success("Added {0} @ {1} to database successfully!".format(tarAlias, tarPlat))

	# --------------------------------------------------

	def extractCreds(self, credsCombo):
		self.utilCore.checkDBExists()

		if ":" in credsCombo:
			tarAlias, tarPlat = credsCombo.split(":")
		else: self.utilCore.print_error("Creds Command Syntax: --creds test@example.com:Proton")

		self.utilCore.print_info("Collecting credentials for {0} @ {1}\n".format(tarPlat, tarAlias))

		masterDBPasswd = getpass.getpass("Master Database Password => "); print()
		
		self.utilCore.print_success("Stored Credential(s) for {0} @ {1}\n=> {2}".format(tarAlias, tarPlat, self.dataCore.pullDBContents(masterDBPasswd, tarAlias, tarPlat)))

	""" END DB FUNCTIONS """


