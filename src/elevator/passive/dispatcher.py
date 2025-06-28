from dataclasses import dataclass, field
from typing import List, Optional
from elevator.passive.elevator import Elevator
from elevator.passive.request import Request


@dataclass
class Dispatcher:
    num_elevators: int
    elevators: List[Elevator] = field(init=False)
    requests: List[Request] = field(default_factory=list)

    def __post_init__(self):
        self.elevators = [Elevator(i, self) for i in range(self.num_elevators)]

    def add_elevator_request(self, request: Request):
        self.requests.append(request)

    def remove_elevator_request(self, request: Request):
        if request in self.requests:
            self.requests.remove(request)

    def get_request_to_handle(self) -> Optional[Request]:
        return self.requests[0] if self.requests else None

    def has_unfulfilled_requests(self, request: Request) -> bool:
        return request in self.requests
