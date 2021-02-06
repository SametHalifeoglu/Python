from Car import Car
from Mercedes import Mercedes

car = Car()
mycar = Mercedes()

deneme = car.model()
print("deneme", deneme)

print("My car's model is " + mycar.model() + " and its gearbox is " + car.gearbox() + " btw it has " + car.wheel() + " wheel.")



