from dataclasses import dataclass, field
from typing import List
from elevator.enums import Direction, DoorState


@dataclass
class Elevator:
    id: int
    current_floor: int = 0
    direction: Direction = Direction.IDLE
    door_state: DoorState = DoorState.CLOSED
    requests: List[int] = field(default_factory=list)

    def request_floor(self, floor: int):
        if floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort(reverse=self.direction == Direction.DOWN)

    def move(self):
        if not self.requests:
            self.direction = Direction.IDLE
            return

        next_floor: int = self.requests[0]
        if self.current_floor == next_floor:
            print(f"Elevator {self.id} opening doors at floor {self.current_floor}")
            self.door_state = DoorState.OPEN
            self.requests.pop(0)
            self.door_state = DoorState.CLOSED
        elif self.current_floor < next_floor:
            self.direction = Direction.UP
            self.current_floor += 1
        else:
            self.direction = Direction.DOWN
            self.current_floor -= 1

    def is_idle(self) -> bool:
        return self.direction == Direction.IDLE and not self.requests
