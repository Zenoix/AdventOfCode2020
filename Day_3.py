def part_1(right=3, down=1):
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


def part_2():
    return part_1(1, 1) * part_1() * part_1(5, 1) * part_1(7, 1) * part_1(1, 2)


print(part_1())
print(part_2())
