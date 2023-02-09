##
#  Define the portfolio class.
#
from bankaccount import BankAccount

## A class that contains a financial portfolio with checking and savings
#  accounts.
#
class Portfolio :
   ## Constructs a new portfolio with a zero balance.
   #
   def __init__(self) :
      self._checking = BankAccount()
      self._savings = BankAccount()

   ## Make a deposit into an account in the portfolio.
   #  @param amount the amount of the deposit
   #  @param account the account, either "S" or "C"
   #
   def deposit(self, amount, account) :
      if account == "C" :
         self._checking.deposit(amount)
      elif account == "S" :
         self._savings.deposit(amount)

   ## Make a withdrawal from an account in the portfolio.
   #  @param amount the amount of the withdrawal
   #  @param account the account, either "S" or "C"
   #
   def withdraw(self, amount, account) :
      if account == "C" :
         self._checking.withdraw(amount)
      elif account == "S" :
         self._savings.withdraw(amount)

   ## Make a transfer from one account to the other.
   #  @param amount the amount of the transfer
   #  @param account the account the transfer is coming from, either "S" or "C"
   #
   def transfer(self, amount, account) :
      if account == "C" :
         self._checking.withdraw(amount)
         self._savings.deposit(amount)
      elif account == "S" :
         self._savings.withdraw(amount)
         self._checking.deposit(amount)

   ## Get the balance of an account.
   #  @param account the account, either "S" or "C"
   #  @return the balance of the account
   # 
   def getBalance(self, account) :
      if account == "C" :
         return self._checking.getBalance()
      elif account == "S" :
         return self._savings.getBalance()

