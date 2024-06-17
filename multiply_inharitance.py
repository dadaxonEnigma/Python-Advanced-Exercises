class Vihicle:
    def general_usage(self):
        print('general use: transporation')
    
class Car(Vihicle):
    def __init__(self) -> None:
        print('I am car')
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("specific use: commute to work, vacation with famaly")
    
class MotorCycle(Vihicle):
    def __init__(self):
        print('I am MotorCycle')
        self.wheels = 2
        self.has_proof = False
    def specific_usage(self):
        self.general_usage()
        print("specific use: road to trip, racing")

c = Car()
c.general_usage()
c.specific_usage()
m = MotorCycle()
m.specific_usage()

print(isinstance(c,Car))
print(isinstance(c,MotorCycle))
print(issubclass(Car,Vihicle))
print(issubclass(Car, MotorCycle))
