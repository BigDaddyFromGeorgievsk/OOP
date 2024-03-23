#!/usr/bin/python3

from abc import ABC, abstractmethod


class Vehicle(ABC):
	def __init__(self, vehicle_type, year_of_production):
		self.vehicle_type = vehicle_type
		self.year_of_production = year_of_production
		self.__fuel_consumption = fuel_consumption

	@abstractmethod
	def get_rental_price(self):
		pass


	def print_vehicle(self):
		print(f'Parent method: {type(self).__name__}, do something (optional)')

