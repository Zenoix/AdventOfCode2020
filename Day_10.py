# function to create a list from input
def handle_input():
    with open("input.txt", "r") as f:
        # read in the input file as create a list without \n
        input_strings = f.read().splitlines()
        # convert each item into an int
        input_ints = list(map(int, input_strings))
        # sort them in ascending order
        input_sorted = sorted(input_ints)

        # add the charging outlet and device joltages
        output = [0] + input_sorted + [max(input_sorted)+3]

    return output


# part 1 code
def part_1() -> int:
    # counters for differences of 1's and 3's
    diff_one = 0
    diff_three = 0
    # the lower joltage
    lower = 0

    # loop through each adapter
    for adapter in adapters:
        if adapter - lower == 1:
            diff_one += 1
        elif adapter - lower == 3:
            diff_three += 1
        # replace lower with the adapter we just checked
        lower = adapter

    return diff_one * diff_three


# part 2 code
# uses recursion and memoization
# (idk too much about memoization so these will be bad comments)
def part_2(index_1: int) -> int:
    # if function parameter has already been run, return its cached value
    if ways[index_1] != 0:
        return ways[index_1]
    # if the index to check is the last adapter, there is only one way
    if index_1 == len(adapters)-1:
        return 1

    # if the parameters have not been run before
    total = 0

    # loop through the remaining adapter chain
    for index_2 in range(index_1 + 1, len(adapters)):
        # if the difference is valid then recursively call the function
        if adapters[index_2] - adapters[index_1] <= 3:
            # add the return values to total
            total += part_2(index_2)

    # store the result for the index_1 parameter
    ways[index_1] = total

    return total


# driver code
if __name__ == "__main__":
    # process the input
    adapters = handle_input()

    print("Part 1:", part_1())

    # create a list of 0's to cache the return values of part 2
    ways = [0] * len(adapters)
    print("Part 2:", part_2(0))
