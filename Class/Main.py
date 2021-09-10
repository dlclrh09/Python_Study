from Beverage import Beverage
from Coffee import Coffee
from Smoothie import Smoothie

beverage = Beverage("음료", 1000)
coffee = Coffee("콜드브루", 4500)
smoothie = Smoothie("딸기스무디", 5500)

beverageList: list[Beverage] = []
beverageList.append(beverage)
beverageList.append(coffee)
beverageList.append(smoothie)

for beverage in beverageList:
    beverage.printName()
    beverage.printPrice()
    beverage.drink()
    beverage.printTotalPrice(20)
