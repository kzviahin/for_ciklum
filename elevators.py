import random


class Elevator(object):
    """This class creates objects Elevator with all necessary information. Also provides some useful
    methods to interact with it throw facade ElevatorsSystem"""

    def __init__(self, elevator_name, move_to='stay_on_floor', floor=0):
        self.elevator_name = elevator_name
        self.move_to = move_to
        self.floor = floor
        self.stops = []

    def add_stops(self, floor_number):
        self.stops.append(floor_number)

    def _remove_from_stops_if_needed(self, floor):
        if floor in self.stops:
            self.stops.remove(self.floor)
            print("This is one of the stop for {}. The door is opening on {} floor".format(self.elevator_name, floor))
        else:
            print("{} is moving throw {} floor".format(self.elevator_name, floor))

    def move_to_the_next_floor(self):
        if self.stops:
            if self.floor < self.stops[0]:
                self.move_to = 'up'
                self.floor += 1
                self._remove_from_stops_if_needed(self.floor)
            elif self.floor > self.stops[0]:
                self.move_to = 'down'
                self.floor -= 1
                self._remove_from_stops_if_needed(self.floor)
        else:
            self.move_to = 'stay_on_floor'
            print("{} stay on {} floor".format(self.elevator_name, self.floor))

    @property
    def lift_are_moving(self):
        if self.stops:
            return True
        else:
            return False


class Button(object):
    """Just simple class to create and manage buttons"""

    def __init__(self, state):
        self.state = state

    def press_button(self):
        if self.state == 'On':
            print("The button has been already turn on")
            return False
        else:
            self.state = 'On'
            print("Please wait your elevator")
            return True

    def turn_off(self):
        print("The button is turning off")
        self.state = 'Off'


class ElevatorsSystem(object):
    """Facade class to inter"""

    def __init__(self, number_of_elevators, number_of_floors):
        self.elevators = [Elevator(str("Elevator_{}".format(x))) for x in range(number_of_elevators)]
        self.button_on_floors = [Button('Off') for x in range(number_of_floors)]

    def call_lift(self, floor):
        if self.button_on_floors[floor].press_button():
            choose_empty_or_any_flag = True
            for elevator in self.elevators:
                if elevator.stops and ((floor < elevator.floor and elevator.move_to == 'down') or
                                                     (floor > elevator.floor and elevator.move_to == 'down')):
                    elevator.add_stops(floor)
                    choose_empty_or_any_flag = False
                    break
                else:
                    continue
            if choose_empty_or_any_flag:
                for elevator in self.elevators:
                    if not elevator.stops:
                        elevator.add_stops(floor)
                        break
                else:
                    self.elevators[random.randint(0, len(self.elevators)-1)].add_stops(floor)

    def move_all_elevators(self):
        for elevator in self.elevators:
            elevator.move_to_the_next_floor()

    def check_all_buttons(self):
        for elevator in self.elevators:
            if self.button_on_floors[elevator.floor].state == 'On':
                self.button_on_floors[elevator.floor].turn_off()


if __name__ == '__main__':
    our_elevator_system = ElevatorsSystem(2, 6)
    while True:
        flag = input("Do you want to proceed(Y/N): ")
        if flag == 'N':
            print("Bye!")
            break
        elif flag == 'Y':
            lift_press = input("Do you want to press button on floor(Y/N): ")
            if lift_press == 'Y':
                floor = int(input("What floor do you want to press button: "))
                our_elevator_system.call_lift(floor)
                our_elevator_system.move_all_elevators()
                our_elevator_system.check_all_buttons()
            elif lift_press == 'N':
                our_elevator_system.move_all_elevators()
                our_elevator_system.check_all_buttons()
        else:
            print("Please provide correct value")
            continue

