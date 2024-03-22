#!/usr/bin/python3S
from parent_class import Vehicle


class Car(Vehicle):
    def __init__(self, vehicle_type, year_of_production, seating_capacity):
        super().__init__(vehicle_type, year_of_production, weight=0)
        self.__seating_capacity = seating_capacity

    def get_rental_price(self):
        return (2022 - self.year_of_production) * 100 + 500


class Motorcycle(Vehicle):
    def __init__(self, vehicle_type, year_of_production, horsepower):
        super().__init__(vehicle_type, year_of_production, weight=0)
        self.__horsepower = horsepower

    def get_rental_price(self):
        return (2022 - self.year_of_production) * 50 + 250

    def print_vehicle(self):
        print(f'Child method: {type(self).__name__}, do something (optional)')


if __name__ == "__main__":
    tesla = Car("Car", 2020, 4)
    ducati = Motorcycle("Motorcycle", 2018, 1000)

    print(f'Tesla rental price: {tesla.get_rental_price()}')
    print(f'Ducati rental price: {ducati.get_rental_price()}')

    tesla.print_vehicle()
    ducati.print_vehicle()
