class Shop():
    def __init__(self, shopName, productType, customers = 0):
        self.shopName = shopName
        self.productType = productType
        self.customers = customers

    def describe_shop(self):
        print(f'The name of the store is  {self.shopName}. {self.productType} are sold in this store')

    def open_shop(self):
        print('The store is open')

    def incremet_customer(self):
        self.customers += 1

    def set_customers(self, valueCustomers):
        self.customers = valueCustomers


class BookShop(Shop):
    def __init__(self, shopName, productType, customers = 0, *kargsBookStyle):
        super().__init__(shopName, productType, customers = 0)
        self.bookStyle = list(kargsBookStyle)

    def show_book_Style(self):
        strBookStyle ='This store have books next styles: '
        for val in self.bookStyle:
            strBookStyle = strBookStyle + val + ', '
        print(strBookStyle)

bookShop = BookShop('Magick Paper', 'books',0,"фантастика", "детектав", "фентези", "журналы")
bookShop.show_book_Style()