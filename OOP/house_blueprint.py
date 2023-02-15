
class Vehicle():
    def __init__(self, model, price, color, owner):
        self.model =model
        self.price = price
        self.color = color
        self.owner = owner


vehicle_owner_one = Vehicle("Toyota", "1.2M", "Beige", "Mercy")
print(vehicle_owner_one.model)
print(vehicle_owner_one.price)
print(vehicle_owner_one.color)
print(vehicle_owner_one.owner)

print("-----End of owner 1-----")

vehicle_owner_two = Vehicle("BMW", "2.5M", "Pink", "Christine")
print(vehicle_owner_two.model)
print(vehicle_owner_two.price)
print(vehicle_owner_two.color)
print(vehicle_owner_two.owner)

print("----End of owner 2----")

vehicle_owner_three =Vehicle("Volkswagen", "3.5M", "Black", "Susan")
print(vehicle_owner_three.model)
print(vehicle_owner_three.price)
print(vehicle_owner_three.color)
print(vehicle_owner_three.owner)