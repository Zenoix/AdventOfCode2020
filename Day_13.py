# function to create a list from input
def handle_input() -> (int, list[int]):
    with open("input.txt", "r") as f:
        # first line of the input as an int
        arrival_ts = int(f.readline())
        # the second line as a list of ints if not and "x"
        buses = [int(bus) for bus in f.readline().split(",") if bus.isdigit()]

    return arrival_ts, buses


# part 1 code
def part_1() -> int:
    # earliest bus that you can take
    earliest_bus = 0
    # the max mod result
    max_diff = 0
    # loop through the buses
    for bus in buses:
        # find the maximum mod result
        if arrival % bus > max_diff:
            # set the new variable values
            earliest_bus = bus
            max_diff = arrival % bus

    # the wait time can be calculated like this
    wait_time = earliest_bus - max_diff

    # return the result
    return earliest_bus * wait_time


# part 2 code (I was unable to solve)
def part_2() -> int:
    pass


# driver code
if __name__ == "__main__":

    arrival, buses = handle_input()

    print("Part 1:", part_1())
    print("Part 2:", part_2())
