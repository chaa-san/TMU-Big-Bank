class CardReader:
    def __init__(self):
        self.cardInserted = False
    
    def isCardInserted(self):
        return self.cardInserted
    
    def insertCard(self):
        self.cardInserted = True
        print("Card has been inserted.")
    
    def ejectCard(self):
        self.cardInserted = False
        print("Card has been ejected.")