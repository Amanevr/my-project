
class bank:
    bank_id="BOC123"
    def __init__(self,customer_name,initial_investment):
        self.initial_investment=initial_investment
        self.cutomer_name=customer_name
        print("Bank name is",self.bank_id)
        print("customer name is",customer_name)
        print("investment:",self.initial_investment)

        print("*************************************")

    def bank_balance(self,withrowal):
        self.initial_investment=self.initial_investment-withrowal
        print("bank balance :",self.initial_investment)
        return self.initial_investment


    def bank_balance1(self,deposit):
        self.initial_investment=self.initial_investment+deposit
        print("bank balance:",self.initial_investment)
        return self.initial_investment

customer1 = bank("Aman",2000)
customer2 = bank("shi ",3000)

customer1.bank_balance(1000)
customer1.bank_balance1(200)
print("........................................")
customer2.bank_balance(300)










