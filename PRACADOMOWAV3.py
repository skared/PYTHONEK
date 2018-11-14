#1 punkt inaczej
class Human:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Somebody(Human):
    def __init__(self, firstname, lastname, age):
        super(Somebody, self).__init__(firstname, lastname)
        self.age = age

    def describe_somebody(self):
        print("Hi! You are {} {}. You are {} years old!".format(self.firstname, self.lastname, self.age))

firstname = input("What's your name?: ")
lastname = input("Whats's your surname?: ")
age = input("How old are u?: ")

somebody = Somebody(firstname, lastname, age)
somebody.describe_somebody()

# 1 punkt
firstname = input("What's your name?: ")
lastname = input("Whats's your surname?: ")
age = input("How old are u?: ")

print("Hi! You are {} {}. You are {} years old!".format(firstname, lastname, age))

# 2 punkt

number = input("Podaj liczbe: ")

number = int(number)
number = float(number)

print("Liczba to {}".format(number))


# 3 punkt

class Flower:
    def __init__(self, name, length):
        self.name = name
        self.length = length


f1 = Flower('Tulipan', 80)

print("Kwiat to {} ma {} cm dlugosci".format(f1.name, f1.length))

f2 = Flower('Roza', 140)

print("Kwiat to {} ma {} cm dlugosci".format(f2.name, f2.length))
