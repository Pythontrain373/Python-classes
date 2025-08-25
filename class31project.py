class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "250 km/h"
class Ferrari:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "340 km/h"
def car_info(car):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
bmw_car=BMW()
ferrari_car=Ferrari()
print("BMW Information:")
car_info(bmw_car)
print("Ferrari Information:")
car_info(ferrari_car)
#Can you teach me how to do line 11 to 15 as i had to watch a video about it