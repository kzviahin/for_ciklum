import pytest
from elevators import Elevator


def pytest_generate_tests(metafunc):
    """Pytest hook to generate button fixture with one or two values, depends on command line parameter"""
    if 'elevator' in metafunc.fixturenames:
        if metafunc.config.option.smoke:
            elevators = [Elevator(elevator_name="ElevatorUP", floor=0)]
        else:
            elevators = [Elevator(elevator_name="ElevatorUP", floor=0),
                         Elevator(elevator_name="ElevatorDown", floor=10)]
        metafunc.parametrize("elevator", elevators, ids=['up', 'down'])


def test_elevator_movement(elevator):
    if elevator.elevator_name == 'ElevatorUP':
        elevator.add_stops(1)
        elevator.move_to_the_next_floor()
        assert elevator.floor == 1
    else:
        elevator.add_stops(9)
        elevator.move_to_the_next_floor()
        assert elevator.floor == 9
