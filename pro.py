from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    @abstractmethod
    def calculate_fee(self, hours):
        pass


class Car(Vehicle):
    def calculate_fee(self, hours):
        return hours * 50


class Bike(Vehicle):
    def calculate_fee(self, hours):
        return hours * 20

class SmartParking:
    def __init__(self, total_slots):
        self.__slots = {}
        self.total_slots = total_slots

    def park_vehicle(self, vehicle):
        if vehicle.vehicle_number in self.__slots:
            print("Vehicle is already parked!")

        elif len(self.__slots) < self.total_slots:
            self.__slots[vehicle.vehicle_number] = vehicle
            print("Vehicle parked successfully!")

        else:
            print("Parking is full!")

    def remove_vehicle(self, vehicle_number, hours):
        if vehicle_number in self.__slots:
            vehicle = self.__slots[vehicle_number]

            fee = vehicle.calculate_fee(hours)

            del self.__slots[vehicle_number]

            print("Vehicle removed successfully!")
            print("Parking Fee:", fee, "Taka")

        else:
            print("Vehicle not found!")

    def show_parked_vehicles(self):
        if not self.__slots:
            print("No vehicles are parked!")

        else:
            print("\nParked Vehicles:")

            for number, vehicle in self.__slots.items():
                print(number, "-", vehicle.__class__.__name__)

    def available_slots(self):
        return self.total_slots - len(self.__slots)

def main():

    parking = SmartParking(5)

    while True:

        print("\n===== SMART PARKING MANAGEMENT =====")
        print("1. Park Car")
        print("2. Park Bike")
        print("3. Remove Vehicle")
        print("4. View Parked Vehicles")
        print("5. Check Available Slots")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = input("Enter car number: ")
            car = Car(number)
            parking.park_vehicle(car)

        elif choice == "2":
            number = input("Enter bike number: ")
            bike = Bike(number)
            parking.park_vehicle(bike)

        elif choice == "3":
            number = input("Enter vehicle number: ")
            hours = int(input("Enter parking hours: "))
            parking.remove_vehicle(number, hours)

        elif choice == "4":
            parking.show_parked_vehicles()

        elif choice == "5":
            print("Available Slots:", parking.available_slots())

        elif choice == "6":
            print("Thank you for using Smart Parking!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
