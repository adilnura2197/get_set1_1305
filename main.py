class Car:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


c1 = Car("BMW", 45000)

print(c1.name)

price = c1.get_price()
print(price)

c1.set_price(50000)

print(c1.get_price())
