def calc_trees(right=3, down=1) -> int:
    # initialise variables
    trees = 0
    x = 0

    with open("input.txt", "r") as f:   # open the input file

        for n, line in enumerate(f):    # loop through the lines
            if n % down == 0:   # to skip lines based on slope's down
                line = line.strip()   # remove newline character
                x = x % 31   # x back to the start if past end of line
                if line[x] == "#":
                    trees += 1
                x += right

    return trees


def part_2() -> int:
    return calc_trees(1, 1) * calc_trees() * calc_trees(5, 1) * calc_trees(7, 1) * calc_trees(1, 2)


if __name__ == "__main__":
    print("Part 1:", calc_trees())
    print("Part 2:", part_2())
