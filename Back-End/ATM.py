from Account import Account
from CardReader import CardReader
from Keypad import Keypad
from CashDispenser import CashDispenser
from Display import Display
from Transaction import Transaction
from datetime import datetime

class ATM(object):
    def __init__(self):
        self.cardReader = CardReader()
        self.keypad = Keypad()
        self.cashDispenser = CashDispenser()
        self.display = Display()
        self.currentAccount = None
        
    def insertCard(self):
        cardNum = input("Enter Card Number: ")
        pin = input("Enter PIN: ")
        self.currentAccount = Account.get_user(cardNum, pin)
        if self.currentAccount:
            print("Welcome, {}!".format(self.currentAccount.name))
            self.makeTransaction()
        else:
            print("Invalid Card Number or PIN. Please try again.")
            self.insertCard()

    # Menu option 
    def makeTransaction(self):
        menu = """
        [1] Make a deposit in Chequing
        [2] Make a withdrawal in Chequing
        [3] Transfer funds
        [4] Check balance in Chequing
        [5] Check balance in Saving
        [6] Quit
    
        Enter your choice: """
        choice = self.keypad.get_input(menu)
        if choice == '1':
            self.makeDeposit()
        elif choice == '2':
            self.makeWithdrawl()
        elif choice == '3':
            self.makeTransfer()
        elif choice == '4':
            self.display.displayMessage("Your Chequing account balance is: {}".format(self.currentAccount.chequing_balance))
        elif choice == '5':
            self.display.displayMessage("Your Saving account balance is: {}".format(self.currentAccount.saving_balance))
        elif choice == '6':
            self.quit()
            self.display.displayMessage("Thank you for using TMU Big Bank!")
        else:
            self.display.displayMessage("Invalid choice.")
            self.makeTransaction()
    
    def quit(self):
        self.currentAccount = None

    def makeDeposit(self):
        amount = self.keypad.get_input("Enter deposit amount: ")
        self.currentAccount.deposit(float(amount))
        self.currentAccount.update_chequing_balance(self.currentAccount.chequing_balance)
        self.display.displayMessage("Deposit Accepted")
    
    def makeWithdrawl(self):
        amount = self.keypad.get_input("Enter withdrawl amount: ")
        if self.currentAccount.withdrawl(amount):
            self.cashDispenser.dispense_cash(amount)
            self.currentAccount.update_chequing_balance(self.currentAccount.chequing_balance)
            self.display.displayMessage("Please take your cash")
        else:
            self.display.displayMessage("Insufficient funds.")

    def makeTransfer(self):
        amount = self.keypad.get_input("Enter the amount to be transfered: ")
        accountType = self.keypad.get_input("Enter the account you wish to transfer to ('chequing' or 'saving'): ")
        if self.currentAccount.transfer(amount, accountType):
            if accountType == 'chequing':
                self.messenger.send("Transfer successful. Amount: {} transferred to Chequing account.".format(amount))
        elif accountType == 'saving':
                self.messenger.send("Transfer successful. Amount: {} transferred to Saving account.".format(amount))
        else:
            self.messenger.send("Transfer unsuccessful. Insufficient funds.")

    def run(self):
        self.insertCard()
        while self.currentAccount is not None:
            self.makeTransaction()
        self.cardReader.ejectCard()
        if self.currentAccount:
            return Transaction(self.currentAccount.balance, self.currentAccount.id, dateTime=datetime.now())
        else:
            return None


if __name__ == "__main__":
    atm = ATM()
    atm.run()




