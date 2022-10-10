from oop1 import Vehicle

class Bus(Vehicle):
    
    def __init__(self,max_speed,mileage,price):
       super().__init__(max_speed,mileage)
       self.price = price
        
    def fare(self):
        total_fare = self.capacity * 100 
        fare_charge = total_fare + (0.1 * total_fare)
        return fare_charge

bus = Bus(40,50,10000)
print(bus)
print(bus.price)
print(bus.seating_capacity())
print(type(bus))
print(isinstance(bus,Bus))
print(issubclass(Bus,Vehicle))
print(bus.fare())