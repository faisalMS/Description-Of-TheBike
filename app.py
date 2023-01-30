# OOP

class Bike:
    def __init__(self, description, cost, sale_price, condition):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.sold = False

bike1 = Bike("Univega Alpha, orange", 100, 500, 0.5)

def update_sale_price():
    if bike1.sold == True:
        print("Action not allowed, Bike has already been sold")
    else:
        bike1.sale_price = 500

    update_sale_price(bike1, 350)

def sell():
    bike1.sold = True
    sell(bike1)

# Procedure OP

def update_sale_price(bike, sale_price):
    if bike['sold'] == True:
        print("Action not allowed, Bike has already been sold")
    else:
        bike['sale_price'] = sale_price

def sell(bike):
    bike['sold'] = True

def create_bike(description, cost, sale_price, condition):
    return {
        'description': description,
        'cost': cost,
        'sale_price': sale_price,
        'condition': condition,
        'sold': False
    }

bike1 = create_bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
update_sale_price(bike1, 350)
sell(bike1)