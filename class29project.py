class Vehicle:
    def fare(self):
        return self.seating_capacity*100
class Bus(Vehicle):
    seating_capacity=50
    def fare(self):
        total_fare=super().fare()
        maintenance_charge=total_fare*0.1
        return total_fare+maintenance_charge
bus=Bus()
print(bus.fare())
