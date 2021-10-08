
class bank:
    bank_id="BOC123"
    def __init__(self,customer_name,initial_investment):
        self.initial_investment=initial_investment
        self.cutomer_name=customer_name
        print("Bank name is",self.bank_id)
        print("customer name is",customer_name)
        print("investment:",self.initial_investment)

        print("*************************************")

    def method1(self,withrowal):
        self.initial_investment=self.initial_investment-withrowal
        print("bank balance :",self.initial_investment)
        return self.initial_investment


    def method1(self,deposit):
        self.initial_investment=self.initial_investment+deposit
        print("bank balance:",self.initial_investment)
        return self.initial_investment

customer1 = bank("Aman",5000)
customer2 = bank("shi ",6000)

customer1.method1(1000)
customer1.method1(200)
print("........................................")
customer2.method2(300)










