from elevator.enums import Direction
from elevator.active.request import Request
from elevator.active.dispatcher import Dispatcher


def main():
    dispatcher = Dispatcher(num_elevators=3)

    # External requests
    dispatcher.request_pickup(Request(5, Direction.UP))
    dispatcher.request_pickup(Request(2, Direction.DOWN))

    # Simulate time
    for _ in range(5):
        dispatcher.step_all()
        dispatcher.status()
        print("---")


if __name__ == "__main__":
    main()
