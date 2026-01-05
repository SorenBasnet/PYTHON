from abc import ABC, abstractmethod
from dataclasses import dataclass
from helpers import format_currency

# 1. ABSTRACTION: The template for all vehicles
class Vehicle(ABC):
    @abstractmethod
    def calculate_shipping(self):
        pass

# 2. DATACLASS: Simple container for package info
@dataclass
class Package:
    weight: float
    description: str

# 3. INHERITANCE: Different types of shipping
class Truck(Vehicle):
    def calculate_shipping(self):
        return 10.0  # Flat rate for trucks

class Plane(Vehicle):
    def calculate_shipping(self):
        return 50.0  # Expensive!

# 4. REPR: Let's add a nice representation to our delivery
class Delivery:
    def __init__(self, vehicle, package):
        self.vehicle = vehicle
        self.package = package

    def __repr__(self):
        cost = format_currency(self.vehicle.calculate_shipping())
        return f"Delivery({self.package.description} via {self.vehicle.__class__.__name__} - Cost: {cost})"

# --- Using the system ---
my_package = Package(weight=1.5, description="Vintage Camera")
my_delivery = Delivery(Plane(), my_package)

print(my_delivery) 
# Output: Delivery(Vintage Camera via Plane - Cost: $50.00)


"""
Why this is "Pro" code:
Scalable: Want to add a Drone delivery? Just inherit from Vehicle.

Clean: The format_currency isn't cluttering up your logic; it's in a helper.

Readable: The __repr__ tells you exactly what is happening when you print.

"""