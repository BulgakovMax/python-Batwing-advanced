from abc import ABC, abstractmethod
import random


class Person(ABC):
    def __init__(self, name, age, money, home):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    @abstractmethod
    def person_info(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def make_money(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError("This method is not realized")


class Human(Person):
    def person_info(self):
        if self.home == True:
            real_estate = "Yes"
        else:
            real_estate = "No"
        print(
            f"Person Info:\n Name: {self.name} \n Age: {self.age}\n \
            Account balance: {self.money}$\n \
            Real estate: {real_estate}\n")

    def make_money(self):
        self.money += 1000

    def buy_house(self):
        price = 13000
        if self.money <= price:
            print(
                f"Not enough money to buy a house. You have \
                {self.money}$\n You need to earn \
                {price - self.money}$ \n")
            print("Do you want work?\n Input: 'yes' or 'no'")
            work = str(input())
            if work == "Yes":
                self.make_money()
                self.buy_house()
            else:
                pass
        else:
            self.home = True
            print("Congratulations you buy a house!\n")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def house_info(self):
        print(f"House info:\n Area of house: {self.area}sq.m \
        \n House cost: {self.cost}$\n")


class RieltorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Rieltor(metaclass=RieltorMeta):
    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def info_about_houses(self):
        for i in range(len(self.houses)):
            print(f"House# {i + 1}")
            print(f" {self.houses[i].house_info()} \n")

    def get_discount(self):
        print(f"I'll give you a {self.discount}% discount! \n")

    def cheat(self):
        a = random.randint(0, 9)
        if a == 1:
            print(f"CHEATING SUCCSESSFUL")
        else:
            print("'WASTED' \nI'm not guilty")


cottage = House(50, 13000)
cottage.house_info()
villa = House(220, 33000)
mansion = House(1220, 590000)

mike = Human("Mike", 33, 12444, False)
mike.person_info()
mike.make_money()
mike.person_info()
mike.buy_house()
mike.person_info()

bob = Human("Bob", 20, 11100, False)
bob.person_info()
bob.make_money()
bob.person_info()
bob.buy_house()
bob.person_info()

brown = Rieltor("mr Brown", [cottage, villa, mansion], 10)
brown.info_about_houses
brown.get_discount()
brown.cheat()
