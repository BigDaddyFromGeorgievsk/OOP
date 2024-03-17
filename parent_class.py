#!/usr/bin/python3

from abc import ABC, abstractmethod


class Vehicle(ABC):
	def __init__(self, vehicle_type, year_of_production):
		self.vehicle_type = vehicle_type
		self.year_of_production = year_of_production

	@abstractmethod
	def get_rental_price(self):
		pass


# No changes needed in print_animal method (optional)
	def print_animal(self):
		print(f'Parent method: {type(self).__name__}, do something (optional)')

