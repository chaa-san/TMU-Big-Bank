from CardReader import CardReader
from CashDispenser import CashDispenser
from Display import Display
from Keypad import Keypad

class ATM:
    def __init__(self):
        self.cardReader = CardReader()
        self.cashDispenser = CashDispenser()
        self.display = Display()
        self.keypad = Keypad()

    def start(self):
        # Prompt the user to insert their card
        self.display.showMessageLine("Please insert your card")
        self.cardReader.insertCard()

        # Prompt the user to enter their PIN
        self.display.showMessageLine("Please enter your PIN:")
        pin = self.keypad.get_input()

        # Authenticate the user and start the session if the PIN is correct
 

if __name__ == "__main__":
    atm = ATM()
    atm.start()