from elevator.enums import Direction
from elevator.passive.request import Request
from elevator.passive.dispatcher import Dispatcher


def main():
    dispatcher = Dispatcher(num_elevators=3)

    # External requests
    dispatcher.add_elevator_request(Request(5, Direction.UP))
    dispatcher.add_elevator_request(Request(2, Direction.DOWN))

    # Simulate time
    for _ in range(5):
        dispatcher.get_request_to_handle()
        print("---")


if __name__ == "__main__":
    main()
