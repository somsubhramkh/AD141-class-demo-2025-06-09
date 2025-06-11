#!/usr/bin/env python3
class Car:

    quantity = 0  # Class variable shared by all instances

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0
        Car.quantity += 1

    def __del__(self):
        Car.quantity -= 1

    def drive(self, miles):
        self.odometer += miles

    def __str__(self):
        data = [self.make, self.model, " ~ Odometer:", str(self.odometer)]
        return " ".join(data)
    

def main():
    malibu = Car("Chevy", "Malibu")
    miata = Car("Mazda", "Miata")
    mustang = Car("Ford", "Mustang")
    soul = Car("Kia", "Soul")
    print("# of existing Cars:", Car.quantity)

    malibu.drive(miles=10000)
    miata.drive(500)
    print(malibu, miata, mustang, soul, sep="\n")
    print("Deleting Malibu")
    del malibu

    print("# of existing Cars:", Car.quantity)


if __name__ == "__main__":
    main()