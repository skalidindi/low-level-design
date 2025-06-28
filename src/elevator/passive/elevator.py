from dataclasses import dataclass, field
from typing import List, Optional, TYPE_CHECKING
from elevator.enums import Direction
from elevator.passive.request import Request

if TYPE_CHECKING:
    from elevator.passive.dispatcher import (
        Dispatcher,
    )  # avoid circular import at runtime


@dataclass
class Elevator:
    id: int
    dispatcher: "Dispatcher"
    current_floor: int = 0
    direction: Direction = Direction.IDLE
    requests: List[int] = field(default_factory=list)

    def move(self):
        if not self.requests:
            new_request: Optional[Request] = self.dispatcher.get_request_to_handle()
            if new_request:
                self.requests.append(new_request.floor)
            return

        next_floor: int = self.requests.pop(0)

        while self.current_floor != next_floor:
            self.current_floor += 1 if next_floor > self.current_floor else -1
            req = Request(self.current_floor, self.id)

            if self.dispatcher.has_unfulfilled_requests(req):
                self.dispatcher.remove_elevator_request(req)

            if self.current_floor in self.requests:
                self.requests.remove(self.current_floor)

    def __repr__(self):
        return f"Elevator({self.id}): Floor {self.current_floor}, Dir {self.direction}, Requests {self.requests}"
