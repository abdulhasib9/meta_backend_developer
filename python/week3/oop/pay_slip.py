class pay:
    def __init__(self,input_name,payment,amount) -> None:
        self.name= input_name
        self.payment= payment
        self.amount = amount 

    def pay_now(self):
        self.payment = True

    def pay_status(self):
        if self.payment == True:
            print(self.name + " got payed " + str(self.amount))
        else:
            print(self.name +" has not been payed yet" )

hasib = pay("hasib",False,30000)
noman = pay("Noman","no",4000)

hasib.pay_status()
noman.pay_status()

hasib.pay_now()
hasib.pay_status()