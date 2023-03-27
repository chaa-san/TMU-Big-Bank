class Account:
    lastError = "No Error"
    accountType = "N"

    def __init__(self, fname, lname, id, startingBal):
        if type(fname) == str:
            self.firstname = fname

        if type(lname) == str:
            self.lastname = lname
            
        if type(id) == str:
            self.accountNumber = id
        else:
            print("AccountNumber Type Invalid")

        if type(startingBal) == int or type(startingBal) == float:
            self.balance = startingBal
        else:
            print("Starting Balance type Invalid")

    def getBalance(self):
        return self.balance

    def getaccountNumber(self):
        return self.accountNumber

    def getName(self):
        return str(self.firstname) + " " + str(self.lastname)
    
    def getError(self):
        return self.lastError
    
    def getType(self):
        return self.accountType
    
    def setError(self, errorCode):
        self.lastError = str(errorCode)

    def transfer(Transfer):
        print("NOT IMPLEMENTED")
        return False
    
    def updateAccount():
        print("NOT IMPLEMENTED")
        return False
    
class SavingsAccount(Account):
    def __init__(self, fname, lname, id, startingBal):
        super().__init__(fname, lname, id, startingBal)
        self.accountType = "S"

    def enoughFunds(self, amount):
        if amount <= self.balance:
            return True
        return False
    

class ChequingAccount(Account):
    def __init__(self, fname, lname, id, startingBal):
        super().__init__(fname, lname, id, startingBal)
        self.accountType = "C"

    def enoughFunds(self, amount):
        if amount <= self.balance:
            return True
        return False



if __name__ == "__main__":
    print("----TESTING----")

    newSav = SavingsAccount("user", "name", "12345", 10000.0)
    print(newSav.getName())
    print(newSav.getaccountNumber())

    print(newSav.enoughFunds(1000))
    print(newSav.enoughFunds(100000))

    print(newSav.getError())
    print(newSav.getBalance())
    print(newSav.getType())