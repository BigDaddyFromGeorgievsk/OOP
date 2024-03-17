#!/usr/bin/python3

from parent_class import Vehicle


class Car(Vehicle):
	def __init__(self, vehicle_type, year_of_production):
		super().__init__(vehicle_type, year_of_production)

	def get_rental_price(self):
		print("Parent method")  # Optional (demonstrates parent method call)
		return (2022 - self.year_of_production) * 100 + 500

class Motorcycle(Vehicle):
	def __init__(self, vehicle_type, year_of_production):
		super().__init__(vehicle_type, year_of_production)

	def get_rental_price(self):
		print("Parent method")  # Optional (demonstrates parent method call)
        	return (2022 - self.year_of_production) * 50 + 250


# Example usage
car = Car("Легковой автомобиль", 2018)
motorcycle = Motorcycle("Мотоцикл", 2020)

print(f"Стоимость аренды автомобиля: {car.get_rental_price()}")
print(f"Стоимость аренды мотоцикла: {motorcycle.get_rental_price()}")

