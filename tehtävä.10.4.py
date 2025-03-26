import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


cars = []

for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration_number = f"ABC-{i}"
    car = Car(registration_number, max_speed)
    cars.append(car)

race_over = False
hour = 0

while not race_over:
    hour += 1
for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

for car in cars:
    if car.travelled_distance >= 10000:
            race_over = True
            winner = car
            break

print(f"Race Over! The winner is {winner.registration_number}!")
print("\nFinal standings:")
print(f"{'Registration Number':<15} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<20} {'Travelled Distance (km)'}")

for car in cars:
    print(f"{car.registration_number:<15} {car.max_speed:<15} {car.current_speed:<20} {car.travelled_distance}")