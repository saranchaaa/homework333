import random

class Kovbasa:
    def __init__(self, meat_type, meat_percentage, kind, brand):
        self.meat_type = meat_type
        self.meat_percentage = meat_percentage
        self.kind = kind
        self.brand = brand

    def info(self):
        m = (
             f"Meat type: {self.meat_type}; "
             f"Meat percentage: {self.meat_percentage}; "
             f"Kind of kovbasa: {self.kind}; "
             f"Brand: {self.brand}.")

        return m

class KovbasaManager:
    def create_kovbasa(self):
        mt = input("What kind of meat do you want to put? - ")
        mp = input("How many meat do you want to put (in percents)? - ")
        kd = input("What kind of kovbasa do you want to make? - ")
        bd = input("What is the brand of your kovbasa? - ")
        return Kovbasa(mt, mp, kd, bd)

    def create_random_kovbasa(self):
        meat_types = ["Pork", "Beef", "Chicken", "Turkey"]
        meat_type = random.choice(meat_types)

        meat_percentage = random.randint(50, 90)

        kovbasa_kinds = ["regular", "salami", "doktorska"]
        kind = random.choice(kovbasa_kinds)

        brands = ["kovbasaaaa", "kokovbasa", "asabvok", "kovbasabasabasabasa"]
        brand = random.choice(brands)

        return Kovbasa(meat_type, meat_percentage, kind, brand)


kovbasa_factory = KovbasaManager()

kovbasa = kovbasa_factory.create_kovbasa()
print("\nYour kovbasa:")
print(kovbasa.info())

print("\nRandomly created kovbasa: ")
random_kovbasa = kovbasa_factory.create_random_kovbasa()
print(random_kovbasa.info())
