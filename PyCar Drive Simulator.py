import time

class Car:
    def __init__(self, horsepower=100, braking_power=5, acceleration=2):
        self.horsepower = horsepower
        self.braking_power = braking_power
        self.acceleration = acceleration
        self.speed = 0
        self.gear = 'P'  # Gears: P, R, N, D

    def accelerate(self):
        if self.gear == 'D':
            self.speed += self.acceleration
        elif self.gear == 'R':
            self.speed -= self.acceleration

        
        self.speed = max(min(self.speed, self.horsepower), -self.horsepower / 2)

    def brake(self):
        if self.speed > 0:
            self.speed -= self.braking_power
            if self.speed < 0:
                self.speed = 0
        elif self.speed < 0:
            self.speed += self.braking_power
            if self.speed > 0:
                self.speed = 0

    def set_gear(self, gear):
        if gear in ['P', 'R', 'N', 'D']:
            self.gear = gear
            if gear == 'P':
                self.speed = 0

    def status(self):
        return f"Gear: {self.gear} | Speed: {self.speed:.1f} km/h"

# Setup
print("Welcome to PyCar Drive Simulator (Terminal Edition)!")
hp = int(input("Enter horsepower: "))
bp = int(input("Enter braking power: "))
ac = int(input("Enter acceleration: "))

car = Car(hp, bp, ac)

print("\nControls:")
print("W = Accelerate | S = Brake")
print("1 = Park | 2 = Reverse | 3 = Neutral | 4 = Drive")
print("Q = Quit\n")

# Main loop
while True:
    print(car.status())
    command = input("Enter command: ").lower()

    if command == 'w':
        car.accelerate()
    elif command == 's':
        car.brake()
    elif command == '1':
        car.set_gear('P')
    elif command == '2':
        car.set_gear('R')
    elif command == '3':
        car.set_gear('N')
    elif command == '4':
        car.set_gear('D')
    elif command == 'q':
        print("Exiting PyCar Simulator. Drive safe!")
        break
    else:
        print("Invalid input.")

    time.sleep(0.2)
    print("-" * 40)
