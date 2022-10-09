from oop3 import Bus
from oop1 import Vehicle
class School_bus(Bus):
    pass


print(issubclass(School_bus,Bus))
print(issubclass(School_bus,Vehicle))
print(isinstance(School_bus,Bus))
print(isinstance(School_bus,Vehicle))