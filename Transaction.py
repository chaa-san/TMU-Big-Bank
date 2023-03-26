from account import Account #update this with actual name
import random

class Transaction(object):


    def __init__(self, amount, dateTime, transactionType):
        self.id = random.randint(0,9999999)     #Assigns random ID number for Transaction
        self.amount = amount
        self.dateTime = dateTime  #Date and time format will be in stored in a string format of MM/DD/YY HH:MM
        self.transactionType = transactionType

    #List of get/set functions
    def getDate(self):
        return self.dateTime
    
    def getID(self):
        return self.id
    
    def getAmount(self):
        return self.amount
    
    def getTransactionType(self):
        return self.transactionType

    def executeTransaction(self, account1, *account2): #update account with actual name
        if self.transactionType.lower() == "withdraw":       #Withdraws Cash from account
            #check account balance with self.amount
            if not account1.balanceCheck(self.amount): 
                return None
            
            account1.balance -= self.amount
            #add something here for the atm to dispense cash
            return "Transaction ID:\t" + self.id + "\n" + "Date and Time:\t" + self.dateTime + "\nTransaction:\tWithdrawal\n"\
                 + "Amount Withdrawn:\t" + self.amount #Returns String for the receipt
        
        if self.transactionType.lower() == "deposit":        #Deposits Cash into the Account
            account1.balance += self.amount

            return "Transaction ID:\t" + self.id + "\n" + "Date and Time:\t" + self.dateTime + "\nTransaction:\tDeposit\n"\
                 + "Amount Deposited:\t" + self.amount   #Returns String for the receipt
        
        if self.transactionType.lower() == "transfer":       #Transfers from 1 account to the other
            if not account1.balanceCheck(self.amount):
                return None
            
            account1 -= self.amount             #Deducts from first account
            account2 += self.amount             #Adds to second account
            return "Transaction ID:\t" + self.id + "\n" + "Date and Time:\t" + self.dateTime + "\nTransaction:\tTransfer\n"\
                 + "Amount Transfered from " + account1.accountName + " to " + account2.accountName + " :\t" + self.amount      #Returns String for the receipt



            

