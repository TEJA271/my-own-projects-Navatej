import time
import json
import os

class Car:
    def __init__(self, horsepower=100, braking_power=5, acceleration=2):
        self.horsepower = horsepower
        self.braking_power = braking_power
        self.acceleration = acceleration
        self.speed = 0
        self.gear = 'P'  # P, R, N, D
        self.fuel = 100  # percentage
        self.engine_temp = 70  # degrees Celsius

    def accelerate(self):
        if self.fuel <= 0:
            print("Out of fuel!")
            return

        if self.gear == 'D':
            self.speed += self.acceleration
        elif self.gear == 'R':
            self.speed -= self.acceleration


        self.speed = max(min(self.speed, self.horsepower), -self.horsepower / 2)

        self.fuel -= 0.5
        self.engine_temp += 1.5

    def brake(self):
        if self.speed > 0:
            self.speed -= self.braking_power
            if self.speed < 0:
                self.speed = 0
        elif self.speed < 0:
            self.speed += self.braking_power
            if self.speed > 0:
                self.speed = 0

        self.engine_temp -= 0.5  

    def set_gear(self, gear):
        if gear in ['P', 'R', 'N', 'D']:
            self.gear = gear
            if gear == 'P':
                self.speed = 0

    def refuel(self):
        self.fuel = 100
        print("Fuel tank refilled.")

    def cool_engine(self):
        self.engine_temp = 70
        print("Engine cooled.")

    def status(self):
        warning = ""
        if self.fuel < 10:
            warning += " [LOW FUEL]"
        if self.engine_temp > 110:
            warning += " [ENGINE OVERHEAT]"

        return (f"Gear: {self.gear} | Speed: {self.speed:.1f} km/h | "
                f"Fuel: {self.fuel:.1f}% | Temp: {self.engine_temp:.1f}°C{warning}")

    def save_settings(self, filename='car_settings.json'):
        with open(filename, 'w') as f:
            json.dump({
                "horsepower": self.horsepower,
                "braking_power": self.braking_power,
                "acceleration": self.acceleration
            }, f)
        print("Settings saved.")

    def load_settings(self, filename='car_settings.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                self.horsepower = data["horsepower"]
                self.braking_power = data["braking_power"]
                self.acceleration = data["acceleration"]
            print("Settings loaded.")
        else:
            print("No saved settings found.")

def main():
    print("🚗 Welcome to PyCar Drive Simulator - Enhanced Version!")

    use_saved = input("Load previous car settings? (y/n): ").lower()
    car = Car()
    if use_saved == 'y':
        car.load_settings()
    else:
        hp = int(input("Enter horsepower: "))
        bp = int(input("Enter braking power: "))
        ac = int(input("Enter acceleration: "))
        car = Car(hp, bp, ac)

    print("\nControls:")
    print("W = Accelerate | S = Brake | 1 = P | 2 = R | 3 = N | 4 = D")
    print("F = Refuel | C = Cool Engine | V = Save Settings | Q = Quit\n")

    while True:
        print(car.status())
        command = input("Enter command: ").lower()

        if command == 'w':
            car.acceler
