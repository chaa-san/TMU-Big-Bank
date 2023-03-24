class Keypad:
    def __init__(self):
        # reading data from the command line
        self.input = input

    # returning the integer value user inputed to sign-in
    def get_input(self):
        return int(input())