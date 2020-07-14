class Car:
    def __init__(self, brand, model, color, fuel):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel = fuel

    def start(self):
        pass

    def halt(self):
        pass

    def drift(self):
        print("Am from drift method")
        pass

    def speedup(self):
        pass

    def turn(self):
        pass

blackverna=Car('Hyundai','Verna','Black','Diesel')

blackverna.drift()
print(blackverna.fuel)


