from enum import Enum


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"


class DoorState(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
