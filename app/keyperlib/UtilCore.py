import keyperlib
import os, sys, string, random, colorama

class UtilCore(object):
	"""
		KeyperLib | UtilCore
	"""

	def __init__(self, *args, **kwargs):
		pass

	# Text Coloring Properties
	# if "win" in sys.platform.lower(): colorama.init() # support for windows
	def print_success(self, string): print(f'{colorama.Style.BRIGHT}{colorama.Fore.GREEN}{colorama.Style.BRIGHT}[+] ' + string + f'{colorama.Style.RESET_ALL}')
	def print_warning(self, string): print(f'{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}[=] ' + string + f'{colorama.Style.RESET_ALL}')
	def print_error(self, string): print(f'{colorama.Style.BRIGHT}{colorama.Fore.RED}[-] ' + string + f'{colorama.Style.RESET_ALL}'); sys.exit(0)
	def print_info(self, string): print(f'{colorama.Style.BRIGHT}{colorama.Fore.CYAN}[i] ' + string + f'{colorama.Style.RESET_ALL}')
	def print_debug(self, string):
		if keyperlib.__verbose__: print(f'{colorama.Fore.MAGENTA}[#] ' + string + f'{colorama.Style.RESET_ALL}')
	def print_divider(self): print('\n' + ('-' * 25) + '\n')

	def randomstr(self, length=32, strength=1):
		letters = (string.ascii_letters + str(string.digits)) * strength + "!@#$%^&*()-_=+[}{]\\|;:'\",<.>/?"
		return ''.join(random.choice(letters) for i in range(length))

	def checkDBExists(self):
		if os.path.isfile(keyperlib.__database__) == False: self.print_error("Database doesn't exist, please create one with '--create'")