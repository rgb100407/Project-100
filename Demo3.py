class ATM(object):
    def __init__(self,pin,cardNumber):
        self.pin = pin
        self.cardNumber =cardNumber
        

    def CashWithdraw(self):
        print("CashWithdraw")

    def CashDeposit(self):
        print("CashDeposit")  

      
Atm1=ATM(100407,"2000 4000 5000 4125" )
print(Atm1.pin)