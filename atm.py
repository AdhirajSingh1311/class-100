from xxlimited import new


class Atm(object):
    def __init__(self,cardNumber,pinNumber) :
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def checkBalance (self):
        print ('ur balance is 50k')
    
    def withdraw (self,amount):
        newBalance=50000-amount
        print ("u have widthrawn "+str(amount)+"ur remaining balance"+str(newBalance))
def main():
        cardNumber=input("insert ur card no")
        pinNumber=input("enter ur pin number")
        newUser=Atm(cardNumber,pinNumber)
        print ("choose ur activity")
        print ("1.balance inquiry         2.withdrawl")
        activity=int(input("enter activity number"))
        if (activity==1):
            newUser.checkBalance()
        elif(activity==2):
            amount=int(input("enter the amount"))
            newUser.withdraw(amount)
        else:
            print("enter a valid number")
if __name__=="__main__":
    main()
        
