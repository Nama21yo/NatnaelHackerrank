class Customer:

    def __init__(self, id, name, bdno, bstreet, bcity, bcountry, bpin, sdno, sstreet,scity,scountry,spin):
        self.custid = id
        self.name = name
        self.billingAddress = self.Address(bdno,bstreet,bcity,bcountry,bpin)
        self.shippingAddress = self.Address(sdno, sstreet,scity,scountry,spin)
    class Address:
        def __init__(self, dno, street, city, country, pin):
            self.dno = dno
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin
        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)
