class Elevator:
    def __init__(self,bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor:
            print("Target floor is not possible to reach")
            return
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor +=1
            print(f"Elevator is now at floor {self.current_floor}.")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            print(f"Elevator is now at floor {self.current_floor}.")
class Building:
    def __init__(self, num_top, num_bottom, num_elevators):
        self.num_top = num_top
        self.num_bottom = num_bottom
        self.elevators = [Elevator(num_bottom, num_top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Invalid elevator number: {elevator_number}. Choose between 1 and {len(self.elevators)}.")
            return
        elevator = self.elevators[elevator_number - 1]
        print(f"Runnin elevator {elevator_number} to floor {target_floor}: ")
        elevator.go_to_floor(target_floor)
    def fire_alarm(self):
        for elevator in self.elevators:
            print("All elevator moving to the bottom floor.")
            elevator.go_to_floor(self.num_bottom)

building = Building(1, 5, 3)
building.run_elevator(1,4)
building.run_elevator(3, 5)
building.run_elevator(3, 6)
building.fire_alarm()


