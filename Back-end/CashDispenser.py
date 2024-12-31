class CashDispenser:
    # Stores the total amount of money (in dollars) that the ATM has available in bills -- $10,000
    # Take note of what bills the customer can take out, i.e., $5, $10, $20, $50, $100
    initial_bill_count = 10000

    # Represents the number of bills remaining in the ATM
    def init(self):
        self.count = CashDispenser.initial_bill_count

    # 'amount' - represents the amount of cash that the user wants to withdraw
    def dispense_cash(self, amount):
        remaining_amount = int(amount)
        bill_values = [100, 50, 20, 10, 5]
        bill_counts = [0, 0, 0, 0, 0]

        for i in range(len(bill_values)):
            if remaining_amount >= bill_values[i]:
                bill_counts[i] = remaining_amount // bill_values[i]
                remaining_amount = remaining_amount % bill_values[i]

        if remaining_amount > 0:
            print("Sorry, the ATM does not have enough bills to dispense the requested amount.")
        else:
            print("Dispensing cash:")
            for i in range(len(bill_values)):
                if bill_counts[i] > 0:
                    print(str(bill_counts[i]) + " x $" + str(bill_values[i]))

