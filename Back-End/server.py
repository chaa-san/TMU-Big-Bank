from flask import Flask, request, jsonify, send_from_directory
from CardReader import CardReader
from CashDispenser import CashDispenser
from Display import Display
from Keypad import Keypad
from Transaction import Transaction
from Account import Account
import mysql.connector

app = Flask(__name__)

global currentAccount

@app.route("/submit", methods=["POST"])
def submit():
    global currentAccount
    data = request.get_json()
    input1 = data['input1'] #pin OR depost / withdrawal / transfer amount
    input2 = data['input2'] #account nummber 
    input3 = data['input3'] #state / type of action to do 
    pin = int(input1)
    acc = int(input2)
    state = int(input3)
    
    
    if state == 0:
          currentAccount = Account.get_user(acc, pin)
          if currentAccount:
               return jsonify({"result": "Welcome to Big Bank, " + currentAccount.name + "!"})
          else:
               return jsonify({"result": "Invalid Credentials!"}) 
    elif state == 1:
         currentAccount.deposit(float(pin))
         currentAccount.update_chequing_balance(currentAccount.chequing_balance)
         return jsonify({"result": "Successfully deposited: $" + str(pin) + " Into Chequing"}) 
    elif state == 2:
         if currentAccount.withdrawl(pin):
            currentAccount.update_chequing_balance(currentAccount.chequing_balance)
            return jsonify({"result": "Withdraw Complete, Please take your cash: $" + str(pin)}) 
         else:
            return jsonify({"result": "Insufficient Funds."}) 
    elif state == 3: #should transfer to savings 
         if currentAccount.transfer(pin, 'saving'):
             return jsonify({"result": "$" + str(pin) + " Transferred to savings account"}) 
    elif state == 4: #shoudl to chequing 
         if currentAccount.transfer(pin, 'chequing'):
             return jsonify({"result": "$" + str(pin) + " Transferred to chequing account"}) 
    else:
         return jsonify({"result": "Error, Please Refresh!"}) 
         

@app.route("/account", methods=["POST"])
def account():
     global currentAccount
     data = request.get_json()
     input_var = data["input"]
     output_var = input_var
     if output_var == 'Chequing':
          return jsonify({"result": "Chequing Balance is: $" + str(currentAccount.chequing_balance)})
     elif output_var == 'Savings':
          return jsonify({"result": "Savings Balance is: $"  + str(currentAccount.saving_balance)})  
     
     
    
    


if __name__ == "__main__":
    app.run(debug=True)
