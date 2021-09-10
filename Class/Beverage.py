class Beverage:

    def __init__(self, name: str, price: int) -> None:
        super().__init__()
        self.name = name
        self.price = price

    def printPrice(self):
        print(self.price)

    def printName(self):
        print(self.name)

    def drink(self):
        print("drink")

    def printTotalPrice(self, cnt: int):
        print(self.price * cnt)

