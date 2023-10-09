import mysql.connector
#san7890!
class Account(object):
    def __init__(self, card_num, name, pin, chequing_balance=0, saving_balance=0):
        self.card_num = card_num
        self.name = name
        self.pin = pin
        self.chequing_balance = float(chequing_balance)
        self.saving_balance = float(saving_balance)
        self.balance = self.chequing_balance + self.saving_balance
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='atm'
        )

    def __del__(self):
        self.mydb.close()

    @staticmethod
    def get_user(card_num, pin):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='atm'
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT card_num, name, pin, chequing_balance, saving_balance FROM users WHERE card_num=%s AND pin=%s", (card_num, pin))
        user = mycursor.fetchone()
        if user:
            return Account(*user)
        else:
            return None


    def update_chequing_balance(self, amount):
        self.chequing_balance = amount
        self.balance = self.chequing_balance + self.saving_balance
        cursor = self.mydb.cursor(prepared=True)
        query = "UPDATE Users SET chequing_balance = %s WHERE card_num = %s"
        values = (amount, self.card_num)
        cursor.execute(query, values)
        self.mydb.commit()
        

    def update_saving_balance(self, amount):
        self.saving_balance = amount
        self.balance = self.chequing_balance + self.saving_balance
        cursor = self.mydb.cursor()
        query = "UPDATE Users SET saving_balance = %s WHERE card_num = %s"
        values = (amount, self.card_num)
        cursor.execute(query, values)
        self.mydb.commit()

    def get_chequing_balance(self):
        return self.chequing_balance

    def get_saving_balance(self):
        return self.saving_balance
    

    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        self.chequing_balance += amount
        self.update_user()

    def withdrawl(self, amount):
        amount = float(amount)
        print("amount is: " , amount)
        print("balance: " , self.chequing_balance)
        if self.chequing_balance >= amount:
            self.chequing_balance -= amount
            self.update_user()
            return True
        else:
            return False
    
    def transfer(self, amount, accountType):
        amount = float(amount)
        if accountType == 'chequing':
            if self.saving_balance >= amount:
                self.saving_balance -= amount
                self.chequing_balance += amount
                self.balance = self.chequing_balance + self.saving_balance
                self.update_user()
                return True
            else:
                return False
        elif accountType == 'saving':
            if self.chequing_balance >= amount:
                self.chequing_balance -= amount
                self.saving_balance += amount
                self.balance = self.chequing_balance + self.saving_balance
                self.update_user()
                return True
            else:
                return False
            
    def update_user(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("UPDATE users SET chequing_balance=%s, saving_balance=%s WHERE card_num=%s", (self.chequing_balance, self.saving_balance, self.card_num))
        self.mydb.commit()


