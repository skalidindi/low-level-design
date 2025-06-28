from dataclasses import dataclass, field
from typing import List
from elevator.active.elevator import Elevator
from elevator.active.request import Request
from elevator.enums import Direction


@dataclass
class Dispatcher:
    num_elevators: int
    elevators: List[Elevator] = field(init=False)

    def __post_init__(self):
        self.elevators = [Elevator(i) for i in range(self.num_elevators)]

    def request_pickup(self, request: Request):
        best_elevator = self.find_best_elevator(request)
        print(f"Dispatching elevator {best_elevator.id} for request at floor {request.floor}")
        best_elevator.request_floor(request.floor)

    def find_best_elevator(self, request: Request) -> Elevator:
        idle_elevators = [e for e in self.elevators if e.is_idle()]
        if idle_elevators:
            return min(idle_elevators, key=lambda e: abs(e.current_floor - request.floor))

        candidates = []
        for e in self.elevators:
            if e.direction == request.direction:
                if (request.direction == Direction.UP and e.current_floor <= request.floor) or (
                    request.direction == Direction.DOWN and e.current_floor >= request.floor
                ):
                    candidates.append(e)

        if candidates:
            return min(candidates, key=lambda e: abs(e.current_floor - request.floor))

        return min(self.elevators, key=lambda e: len(e.requests))

    def step_all(self):
        for elevator in self.elevators:
            elevator.move()

    def status(self):
        for elevator in self.elevators:
            print(elevator)
