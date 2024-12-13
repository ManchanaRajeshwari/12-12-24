class Bank:
    acbal=10000
    def deposit(self):
        d_amount=int(input("Enter deposit amount"))
        if (d_amount>100):
            #self.acbal+=d_amount
            print("Accepted deposit as you entered amount is >100")
            if(d_amount<=50000):
               print("Accepted deposit as You entered amount is below 50k")
            elif(d_amount%100)==0:
               print("Accepted deposit as You entered amount is multiples of 100")
            else:
                print("amount is >50k or not the multiples of 100")
        else:
            print("amount is less than 100")
    def withdraw(self):
        if(self.acbal>500):
           w_amount=int(input("Enter withdraw amount"))
           if(w_amount>100):
              #self.acbal-=w_amount
              print("Accepted withdrawl as you entered w_amount is >100")
              if(w_amount< self.acbal):
                print("Accepted withdrawl as you entered w_amount is <accbal")
              elif(w_amount%100)==0:
                print("Accepted withdrawl as you entered w_amount is multiples of 100")
              else:
                  print("You entered amount is amount is >balance or not multiples of 100")
           else:
               print("Min  balance is 500 not able to execute")
           string=input("Do you want transaction say yes/no")
           if(string=="yes"):
              for i in range(3):
                  transac_amount=int(input("Enter transaction amount"))
                  if (transac_amount == 20000):
                     self.acbal-=transac_amount
                  else:
                     print("Unable to do transaction as amount is less than 20K")
              else:
                  print("You exceeded transaction limit")
           else:
               print("Continue..")
    def display(self):
      while(True):
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance Enquiry")
        print("4.Exit")
        print("Choose your option")
        option=int(input("Enter your option"))
        if(option==1):
            obj.deposit()
        elif(option==2):
            obj.withdraw()
        else:
            exit(0)
    def validate(self):
           print("Welcome to ABC bank")
           pin_num = int(input("Enter pin number"))
           if (pin_num==1234):
             obj.display()
           else:
               for i in range(2):
                   if(pin_num==1234):
                       obj.display()
                       break
                   else:
                       pin_num = int(input(" Re-Enter pin number"))
               print("Your card is blocked for this day")

obj=Bank()
obj.validate()


