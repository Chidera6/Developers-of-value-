from oop1 import Vehicle

class Bus(Vehicle):
    seating_capacity = 50
    def __init__(self,max_speed,mileage,price):
       super().__init__(max_speed,mileage)
       self.price = price
        
    def fare(self):
        total_fare = Bus.seating_capacity * 100 
        fare_charge = total_fare + (0.1 * total_fare)
        return fare_charge

chidera = Bus(40,50,10000)
print(chidera)
print(chidera.price)
print(chidera.seating_capacity)
print(type(chidera))
print(isinstance(chidera,Bus))
print(issubclass(Bus,Vehicle))
print(chidera.fare())