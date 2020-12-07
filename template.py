# function to create a list from input
def handle_input() -> list[str]:
    with open("test.txt", "r") as f:
        # read in the input file as create a list without \n
        output = f.read().splitlines()

    return output


# part 1 code
def part_1():
    pass


# part 2 code
def part_2(key: str) -> int:
    pass


# driver code
if __name__ == "__main__":

    foo = handle_input()

    print("Part 1:", part_1())
    print("Part 2:", part_2())
