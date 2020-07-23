class BankAccount:
   

    def __init__(self, first_name, last_name, phone_no, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_summary = []
        self.deposit_summary = []
        self.loan_balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name, self.phone_no, self.bank)
        return name

    def deposit(self, amount):
      
      if amount <= 0:
               
          print("You cannot deposit zero or negative")
      else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))
            return 
            
            
          
    def withdraw(self, amount):
         
      if amount <= 0:
          print("You cannot withdraw zero or negative")
          
       
      elif amount > self.balance:
            print("You don't have enough balance")
      else:
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))


    def get_balance(self):
   
        return "The balance for {} is {}".format(self.account_name(), self.balance)
    def show_deposit_statement(self):
      for deposite in self.deposits:
        print(deposit)
        def show_withdrwals_statement():
          for withdrawal in self.withdrawals:
            print(withdrawals)
 # """ write a method to return the witdrawal transactions
  #define a method
  #input amount
  
  #append to empty list
  
    
    def request_loan(self, amount):
      if amount<= 0:
        print("You cannot requet for loan of tht amount")
        
      else: 
        self.loan = amount
        print("You have been given loan of {}".format(amount)
      
    def repay_loan(self, amount):
      if amount<= 0:
        print("You cannot repay with that amount")
      elif self.loan == 0:
        print("You don't have loan at th moment")
        elif amount > self.loan:
          print("your loan is {}, please enter amount that is less or equal to the amount")
        ele:
        print(" You have repayed your loan with {}.your loan balance is{}".format(mount))
       
    def deposit_statement(self, amount):
      self.deposit(self, amount)
      
      return self.deposit_summary.append(amount)
      
      
    def deposit_statement(self, amount):
      self.deposit(self, amount)
      
      return self.deposit_summary.append(amount)
       
      
    
    
acc1 = BankAccount(" irine", "Joy", +254717601136, " Union")
print(acc1.phone_no)
acc1.deposit(50000)
acc1.withdraw(15000)
acc1.withdraw(1200)
acc1.deposit(4000)
acc1.deposit(2400)
acc1.lend_loan(7000)
acc1.lend_loan(20000)
acc1.pay_loan(15000) 
print(acc1.loan_balance)

print(acc1.deposit_summary)



        
        
        
        
        