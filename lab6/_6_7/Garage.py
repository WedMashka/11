print('-----------------------------------------------6----------------------------------------------------------------------')
class Garage():
    def __init__(self,garage_name, product_type):
        self.garage_name = garage_name
        self.product_type = product_type
    def describe_garage(self):
        print('Garage name = ', self.garage_name, ' product_type = ', self.product_type)

    def open_garage(self):
        print("Garage open")

spanner = Garage('Spanner', 'baggi')

print(spanner.garage_name)
print(spanner.product_type)

spanner.describe_garage()
spanner.open_garage()

print('-----------------------------------------------7----------------------------------------------------------------------')

g1 = Garage('Сверкающий колпак','шины и диски')
g2 = Garage('Боченок с маслом','капитальный ремонт двигателя')
g3 = Garage('Баранка с маком','перетяжка салона')
g1.describe_garage()
g2.describe_garage()
g3.describe_garage()

