import keyperlib
import os, json, base64, simplecrypt

class DataCore(object):
	"""
		KeyperLib | DataCore
	"""

	def __init__(self, *args, **kwargs):
		self.utilCore = keyperlib.UtilCore()
		"""
		-- Main Functions
		[DataCore->createDatabase(string)] 				create initial database
		[DataCore->changeDBPasswd(string, string)] 		modify master database password
		[DataCore->exportDatabase(string)] 				export database contents (CAUTION)

		-- DB Functions
		[DataCore->pullDBCreds(string, string)]			extract creds for alias:platform
		[DataCore->]
		"""

	""" START MAIN FUNCTIONS """

	# --------------------------------------------------

	def createDatabase(self, tarPasswd):
		"""
		keyperlib -> DataCore -> createDatabase(string)

		This function assumes there is no existing database and will create a new database
		at the 'keyperlib.__database__' location. The file will then be encrypted using the
		chosen password defined by the client.  
		"""

		if os.path.isfile(keyperlib.__database__):
			self.utilCore.print_error("Database already exists - canceling operation.")
		else:
			with open(keyperlib.__database__, "w") as databaseObj:
				cryptDBContents = simplecrypt.encrypt(tarPasswd, json.dumps({"test@example.com": {"Test": "pass123"}}))
				databaseObj.write(base64.b64encode(cryptDBContents).decode())
				return True

	# --------------------------------------------------

	def changeDBPasswd(self, tarCurrentPasswd, tarUpdatedPasswd):
		"""
		keyperlib -> DataCore -> changeDBPasswd(string, string)

		This function decrypts the current database, re-encrypts the contents with a
		new password and then overwrights the existing contents.
		"""

		# open DB and decrypt contents with existing password
		storedDatabaseContents = open(keyperlib.__database__, "r").read()
		try:
			rawDatabaseContents = simplecrypt.decrypt(tarCurrentPasswd, base64.b64decode(storedDatabaseContents)).decode()
		except simplecrypt.DecryptionException: self.utilCore.print_error("Authorization Failed. Please try a different password!")

		# encrypt contents with updated password and overwright contents
		encryptedDatabaseContents = simplecrypt.encrypt(tarUpdatedPasswd, rawDatabaseContents)
		del(rawDatabaseContents) # remove raw database contents from memory
		with open(keyperlib.__database__, "w") as databaseObj:
			databaseObj.write(base64.b64encode(encryptedDatabaseContents).decode())
			databaseObj.close()

		return True

	# --------------------------------------------------

	def exportDatabase(self, tarPasswd):
		"""
		keyperlib -> DataCore -> exportDatabase(string)

		This function decrypts the entire database and exports it in a variable
		"""
		storedDatabaseContents = open(keyperlib.__database__, "r").read()
		try:
			rawDatabaseContents = simplecrypt.decrypt(tarPasswd, base64.b64decode(storedDatabaseContents)).decode()
		except simplecrypt.DecryptionException: self.utilCore.print_error("Authorization Failed. Please try a different password!")

		return rawDatabaseContents

	""" END MAIN FUNCTIONS """

	# ==================================================

	""" START DB FUNCTIONS """

	def pullDBContents(self, masterDBPass, tarAlias, tarPlat):
		cryptStoredDBContents = open(keyperlib.__database__, "r").read()
		print() # create some whitespace in the cli

		try:
			rawDBContents = simplecrypt.decrypt(masterDBPass, base64.b64decode(cryptStoredDBContents)).decode()
		except simplecrypt.DecryptionException: self.print_error("Authorization Failed. Please try a different password!")

		# print(rawDBContents)

		credDBObj = json.loads(rawDBContents)
		if tarAlias in credDBObj:
			if tarPlat in credDBObj[tarAlias]:
				return credDBObj[tarAlias][tarPlat]
			else: self.print_error("Credentials for that platform don't exist.")
		else: print("That alias has not been stored in our database yet, please add it with '--add'.")

	# --------------------------------------------------

	def pushDBContents(self, masterDBPass, databaseContents):
		cryptDBContents = simplecrypt.encrypt(masterDBPass, databaseContents)

		with open(keyperlib.__database__, "w") as dbObj:
			dbObj.write(base64.b64encode(cryptDBContents).decode())
			dbObj.close()

		return True

	""" END DB FUNCTIONS """