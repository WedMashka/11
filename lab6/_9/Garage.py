class Garage():
    def __init__(self, garage_name, product_type, number_customer=0):
        self.garage_name = garage_name
        self.product_type = product_type
        self.number_customer = number_customer
    def describe_garage(self):
        print('Garage name = ', self.garage_name, ' product_type = ', self.product_type)

    def open_garage(self):
        print("Garage open")

    def set_number_customer(self, valueCustomers):
        self.number_customer = valueCustomers



garageN1 = Garage("GArage №1", "Услуги по ремонту автомобиля")
print(garageN1.number_customer)

garageN2 = Garage("Garage №2", "Услуги по ремонту автобусов")
garageN2.set_number_customer(14)
print(garageN2.number_customer)

