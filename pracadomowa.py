class Food(object):
    def __init__(self):
        print("Creating Food")

    def Helping_In(self):
        print("For how long?")
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
