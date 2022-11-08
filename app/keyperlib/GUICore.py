import keyperlib
import keyperlib
import git, json, consolemenu

class GUICore(object):
    """
        KeyperLib | GUICore
    """

    def __init__(self, *args, **kwargs):
        self.dataCore = keyperlib.DataCore()
        self.utilCore = keyperlib.UtilCore()

    def displayGUI(self):
        conMenu = consolemenu.ConsoleMenu("Keyper - Secure Password Manager", ("Current Version: 0x" + git.Repo(search_parent_directories=True).head.object.hexsha), prologue_text="", epilogue_text="by OpSec WareHouse LLC, see more at opsec.sh/market")

        passwdVerifyScreen = consolemenu.PromptUtils(consolemenu.Screen())
        masterDBPasswd = passwdVerifyScreen.input("Master Database Password => ")
        rawDatabaseContents = self.dataCore.exportDatabase(masterDBPasswd.input_string)

        keyringObj = json.loads(rawDatabaseContents)
        mailList = []
        for storedMail in keyringObj:
            mailList.append(storedMail)
            # print(mailList)

        mailListMenuItem = consolemenu.SelectionMenu(mailList)
        accountViewItem = consolemenu.items.SubmenuItem("View Accounts", mailListMenuItem, conMenu)
        changeDBPasswdItem = consolemenu.items.FunctionItem("Modify Master Passwd", self.changeDBPasswd)
        # backToCryptobinItem = consolemenu.items.FunctionItem("Backup Credentials to Cryptobin", self.backToCryptobin)
        
        conMenu.append_item(accountViewItem)
        conMenu.append_item(changeDBPasswdItem)
        # conMenu.append_item(backToCryptobinItem)

        conMenu.show()

    def changeDBPasswd(self):
        changeDBPasswdConsole = consolemenu.PromptUtils(consolemenu.Screen())
        # PromptUtils.input() returns an InputResult
        
        currentMasterDBPasswd = changeDBPasswdConsole.input("current master passwd")
        # changeDBPasswdConsole.println("\nYou entered:", result.input_string, "\n")

        # check input passwd for verification

        newMasterDBPasswd = changeDBPasswdConsole.input("new master passwd")
        confirmNewMasterDBPasswd = changeDBPasswdConsole.input("confirm new master passwd")

        if newMasterDBPasswd == confirmNewMasterDBPasswd:
            changeDBPasswdConsole.println("new passwords match!\n")
            changeDBPasswdConsole.enter_to_continue()
        else:
            changeDBPasswdConsole.println("passwords don't match. please retry!\n")
            changeDBPasswd()