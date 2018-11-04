class Food(object):
    def __init__(self):
        print("Creating Food")

    def Helping_In(self):
        print("For how long I won't be hungry?")
    def Duration_Time(self):
        print("We will see..")

food = Food()
food.Helping_In()
food.Duration_Time()

class Kebab(Food):
    def __init__(self):
        print("Creating Kebab")
    def Helping_In(self):
        print("For a short period of time.. u will be hungry soon..")
class Meal_From_Mom(Food):
    def __init__(self):
        print("Creating Meal from mom")
    def Helping_In(self):
        print("This satisfy my hunger!!")

Kebab = Kebab()
meal_from_mom = Meal_From_Mom()

Kebab.Helping_In()
meal_from_mom.Helping_In()

Kebab.Duration_Time()
meal_from_mom.Duration_Time()

class Dog(object):
    def __init__(self,breed_of_dog,origin,length_of_life):
        self.breed_of_dog = breed_of_dog
        self.origin = origin
        self.lenth_of_life = length_of_life
        print("Breed of dog is {} comes from {} and his life expectancy is {} years. HES A MEMBER OF YOUR FAMILY! Welcome!".format(self.breed_of_dog, self.origin, self.lenth_of_life))

    def __del__(self):
        print("Breed of dog is {} comes from {} and his life expectancy is {} years. It's dangerous dog breed, He bited your mother and run away..".format(self.breed_of_dog, self.origin, self.lenth_of_life))
        self.breed_of_dog = ""
        self.origin = ""
        self.lenth_of_life = ""

American_pitbulterier = Dog("American Pitublterier", "United States","8 – 15")
del American_pitbulterier

class Maltese(Dog):
    def __init__(self,breed_of_dog,origin,length_of_life):
        super(Maltese, self).__init__(breed_of_dog,origin,length_of_life)
        print("It's gentle dog, he won't bite ur mom")
        self.breed_of_dog = breed_of_dog

    def __del__(self):
        print("You will hug him all day,all night")
        self.breed_of_dog = ""

Maltese = Maltese("Maltese", "Mediterranean zone", "12-15")





