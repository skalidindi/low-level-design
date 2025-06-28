from dataclasses import dataclass
from elevator.enums import Direction


@dataclass(frozen=True)
class Request:
    floor: int
    direction: Direction | int  # Use int for passive (elevator ID)

    def __eq__(self, other):
        if not isinstance(other, Request):
            return False
        return self.floor == other.floor and self.direction == other.direction

    def __repr__(self):
        return f"Request(floor={self.floor}, direction={self.direction})"
