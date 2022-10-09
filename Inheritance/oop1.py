class Vehicle:
    color = 'white'
    seating_capacity = 50

    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def fare(self):
        fare_charge = Vehicle.seating_capacity * 100
        return fare_charge

    def __str__(self):
        return f"Cars maximum speed is {self.max_speed} and mileage is {self.mileage} and color is {Vehicle.color}"


