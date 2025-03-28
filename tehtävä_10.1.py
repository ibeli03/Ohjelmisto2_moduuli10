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
elevator = Elevator(1, 10)

print("Going to floor 5: ")
elevator.go_to_floor(5)
print("\nGoing to floor: ")
elevator.go_to_floor(1)