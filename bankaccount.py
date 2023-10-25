class BankAccount:
    account_counter = 0
    
    def __init__(self, account_number, account_holder_name, account_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance
        BankAccount.account_counter += 1
        
    def deposit(self, amount):
        self.account_balance += amount
        print("Deposit successful. New balance:", self.account_balance)
        
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient balance.")
        else:
            self.account_balance -= amount
            print("Withdrawal successful. New balance:", self.account_balance)
            
    def display_account_details(self):
        print("Account number:", self.account_number)
        print("Account holder name:", self.account_holder_name)
        print("Account balance:", self.account_balance)
        
    
    def calculate_interest(account_balance, interest_rate):
        return account_balance * interest_rate / 100
    
    
    def calculate_basic_salary(hra, da):
        return 10000 + hra + da
    
    
    def calculate_total_salary(basic_salary, tax):
        return basic_salary - tax
    
    
    def calculate_pf(basic_salary, pf_rate):
        return basic_salary * pf_rate / 100

account1 = BankAccount("756342", "John Wick")
account1.deposit(750)
account1.withdraw(250)
account1.display_account_details()
interest_amount = BankAccount.calculate_interest(account1.account_balance, 5)
account1.account_balance += interest_amount
account1.display_account_details()

basic_salary = BankAccount.calculate_basic_salary(25000, 5000)
total_salary = BankAccount.calculate_total_salary(basic_salary, 3000)
pf_amount = BankAccount.calculate_pf(basic_salary, 12)
print("Basic salary:", basic_salary)
print("Total salary:", total_salary)
print("PF amount:", pf_amount)
