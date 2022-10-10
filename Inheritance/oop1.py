class Vehicle:
    color = 'white'

    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def fare(self):
        fare_charge = self.capacity * 100
        return fare_charge

    def seating_capacity(self,capacity=50):
        self.capacity = capacity
        return self.capacity

    def __str__(self):
        return f"Cars maximum speed is {self.max_speed} and mileage is {self.mileage} and color is {Vehicle.color}"


