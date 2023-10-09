from Account import Account
from datetime import datetime
import random

class Transaction(object):
    def __init__(self, amount, accountID, dateTime=None, transactionType=None, accountType=None, transferType=None):
        self.id = random.randint(0, 9999999)
        self.amount = amount
        self.accountID = accountID
        self.dateTime = dateTime if dateTime else datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        self.transactionType = transactionType
        self.accountType = accountType
        self.transferType = transferType


    #List of get/set functions
    def getDate(self):
        return self.dateTime
    
    def getID(self):
        return self.id
    
    def getAmount(self):
        return self.amount
    
    def getTransactionType(self):
        return self.transactionType

    def getAccountType(self):
        return self.accountType

    def getTransferType(self):
        return self.transferType

    def executeTransaction(self):
        if self.transactionType.lower() == "withdraw":        # Withdraws cash into the account.
            if (self.getAccountType.lower() == "chequing"):
                if (Account.getChequingBalance() < self.getAmount()):
                    print("Insufficient funds.")
                    return None
                else:
                    Account.updateChequingBalance(Account.getChequingBalance() - self.getAmount())
                    return Account.printReceipt()
            elif (self.getAccountType.lower() == "saving"): 
                if (Account.getSavingBalance() < self.getAmount()):
                    print("Insufficient funds.")
                    return None
                else:
                    Account.updateSavingBalance(Account.getSavingBalance() - self.getAmount())
                    return Account.printReceipt()
        
        if self.transactionType.lower() == "deposit":        # Deposits cash into the account.
            if (self.getAccountType.lower() == "chequing"):
                Account.updateChequingBalance(Account.getChequingBalance() + self.getAmount())
                return Account.printReceipt()
            elif (self.getAccountType.lower() == "saving"): 
                Account.updateSavingBalance(Account.getSavingBalance() + self.getAmount())
                return Account.printReceipt()
        
        if self.transactionType.lower() == "transfer":       #Transfers from 1 account to the other
            if (self.getTransferType() == "chequingtosaving"):
                if (Account.getChequingBalance() < self.getAmount()):
                    print("Insufficient funds.")
                    return None
                else:
                    Account.updateChequingBalance(Account.getChequingBalance() - self.getAmount())
                    Account.updateSavingBalance(Account.getSavingBalance() + self.getAmount())
                    return Account.printReceipt()
            elif (self.getTransferType() == "savingtochequing"):
                if (Account.getSavingBalance() < self.getAmount()):
                    print("Insufficient funds.")
                    return None
                else:
                    Account.updateChequingBalance(Account.getChequingBalance() + self.getAmount())
                    Account.updateSavingBalance(Account.getSavingBalance() - self.getAmount())
                    return Account.printReceipt()
