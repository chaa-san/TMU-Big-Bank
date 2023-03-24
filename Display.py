class Display:
    def showMessageLine(self, message):
        print(message)

    # displaying dollar amount
    def showDollarAmount(self, amount):
        print('${:,.2f}'.format(amount)) 