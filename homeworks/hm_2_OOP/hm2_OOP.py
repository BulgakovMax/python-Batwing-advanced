from abc import ABC, abstractmethod
from datetime import datetime

print(" \n-------------Task #1-----------------")
"""Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
"""

class Animals:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print("Yam, yam!")


    def sleep(self):
        print ("Zzzzzz")

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print("I want eat \n")


    def sleep(self):
        print ("Zzzzzz")
        
    def study(self):
        print(f"{self.name} one more task")

    def work(self):
        print ("Yes, today is Friday!")


class Centaur(Human, Animals):
    def __init__(self, name, age , clan):
        Animals.__init__(self, name)
        Human.__init__(self, name, age)
        self.clan = clan

    def get_info(self):
        print(f"My name is {self.name}, my age is {self.age} and I`m from {self.clan} clan \n")    

    def teach(self):
        print("Hello Harry Potter")


class Dog(Animals):
    def fetch(self):
        print("Catched a branch\n")


class Cat(Animals):
    def purring(self):
        print("Mrrrr trrrr mrrrr\n") 


class Honey_badger(Animals):
    def atack(self):
        print("You're a dead man!\n")


class Horse(Animals):
    def galop(self):
        print("Yehaaaa!\n")


class Cow(Animals):
    def to_milk(self):
        print("Oh milk!\n")


maylo = Dog("Maylo")
maylo.eat()
maylo.fetch()

fry = Cat("Fry")
fry.sleep()
fry.purring()

killer = Honey_badger("Killer")
killer.atack()

spirit = Horse("Spirit")
spirit.galop()

sunrise = Cow("Sunrise")
sunrise.to_milk()
print(f"Does Sunrise is instance from Animals class? {isinstance(sunrise, Animals)}")

fred = Human("Fred", 22)
fred.eat()
fred.study()

firenze = Centaur("Firenze", 129, "Dark Forest")
firenze.eat()
firenze.teach()
firenze.get_info()

print(" \n-------------Task #2-----------------")
#Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:
    def __init__(self, name):        
        self.name = name
        right = Arm(' "shake your hand"')
        now = datetime.now()        
        left = Arm(now.strftime("%H:%M"))
        self.arm_left = left.arm
        self.arm_right = right.arm
    
    def info(self):
        print(f"Hi, my name is {self.name}, nice to meet you {self.arm_right}, time is {self.arm_left} \n")


class Arm:
    def __init__(self, arm):
        self.arm = arm


piter = Person("Piter")
piter.info()



class CellPhone:
    def __init__(self, screen):
        self.screen = screen

    def info(self):
        print(f"This Cell phone with {self.screen} display")    

         

class Screen:
    def __init__(self, type):
        self.type = type

oled = Screen("OLED")
ips = Screen("IPS")
samsung = CellPhone(oled.type)
samsung.info()
mi = CellPhone(ips.type)
mi.info()

print(" \n -------------Task #3-----------------")
"""
Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
Override a printable string representation of Profile class and return: list of the params mentioned above
"""
class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        list = []
        for value in self.__dict__.values():
            list.append(value)
        return list.__repr__()

man = Profile("Bob", 'McCalister', 12314214912, "Dublin", "12@g.com", "12.12.88", 33, "male" )
print(man)

print(" \n-------------Task #4-----------------")
""" Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.
"""

class Laptop(ABC):
    
    @abstractmethod
    def screen(self):
        pass
    
    @abstractmethod
    def keyboard(self):
        pass
    
    @abstractmethod
    def touchpad(self):
        pass
    
    @abstractmethod
    def webcam(self):
        pass
    
    @abstractmethod
    def ports(self):
        pass
    
    @abstractmethod
    def dynamics(self):
        pass


class HPLaptop(Laptop):
    def __init__(self, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics


    def screen(self):
        return self.screen
    

    def keyboard(self):
        return self.keyboard
    

    def touchpad(self):
        return self.touchpad
    

    def webcam(self):
        return self.webcam
    

    def ports(self):
        return self.ports
    

    def dynamics(self):
        return self.dynamics

    def get_info(self):
        print(f"Screen: {self.screen}, keyboard: {self.keyboard}, touchpad: {self.touchpad}, webcam: {self.webcam}, ports: {self.ports}, dynamics: {self.dynamics}")


hp = HPLaptop("IPS", "Multi", "Yes", "720", "HDMI", "Atmos")
hp.get_info()