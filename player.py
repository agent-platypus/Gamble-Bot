
from horse import Horse

INIT_MONEY = 100
class Player:
    def __init__(self, name: str):
        self.name = name
        self.money = INIT_MONEY
    
    # Assume amount <= self.money
    # And amount > 0
    # Subtracts amount from money
    def subtractMoney(self, amount: int):
        self.money = self.money - amount 

#hi