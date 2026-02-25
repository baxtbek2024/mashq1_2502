class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        print(f"{self.brand} {self.model} dvigateli ishga tushdi.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} dvigateli o'chirildi.")

    def honk(self):
        print(f"{self.brand} signal chaldi!")

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}, Rang: {self.color}"


class Car(Vehicle):
    def __init__(self, brand, model, year, color, fuel_type, doors):
        super().__init__(brand, model, year, color)
        self.fuel_type = fuel_type
        self.doors = doors

    def honk(self):
        print(f"{self.brand} mashina : bip bip")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, has_sidecar, engine_type):
        super().__init__(brand, model, year, color)
        self.has_sidecar = has_sidecar
        self.engine_type = engine_type


    def honk(self):
        print(f"{self.brand} motosikl: vruuummm")

class Truck(Vehicle):
    def __init__(self, brand, model, year, color, load_capacity, trailer_attached ):
        super().__init__(brand, model, year, color)
        self.load_capacity = load_capacity
        self.trailer = trailer_attached

    def honk(self):
        print(f"{self.brand} truck: dit dit")


car1 = Car("BMW", "M5", 2010, "blue", "AI 95", 4)
motoskl = Motorcycle("BMW", "Z230", 2000, "dark", True, "norm" )
yuk_mashin = Truck("man", "2", 1995, "white", "7 tonna", True)


Hammasi = [car1, motoskl, yuk_mashin]

for i in Hammasi:
    i.start_engine()
    i.honk()
    print((i.get_info()))
