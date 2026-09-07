# object = a "bundle" of related attributes (variables) and methods (functions) ex. phone, cup, book. You need a "class" to create many objects

class Car:

    num_of_wheels = 4
    
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car!")


car1 = Car("Mustang", "2026", "Red", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print(car1.num_of_wheels)

car1.drive()