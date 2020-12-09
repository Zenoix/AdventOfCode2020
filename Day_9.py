# import combinations for part 1
from itertools import combinations


# function to create a list from input
def handle_input() -> list[int]:
    with open("input.txt", "r") as f:
        # read in the input file as create a list without \n
        lines = f.read().splitlines()
        # convert the string numbers in the list to ints
        output = list(map(int, lines))

    return output


# part 1 code
def part_1(nums: list[int], preamble: int) -> int:
    # the indexes of the previous numbers
    start, end = 0, preamble
    for idx, number in enumerate(nums):
        # list of the previous numbers that need 2 to sum to the next num
        prev_nums = nums[start:end]

        # skip the preamble as those don't need to be checked (in prev_nums)
        if idx >= end:
            # list of the sums of the combinations of 2 nums from prev_nums
            sums_of_nums = map(sum, combinations(prev_nums, 2))

            # if the next number is the sum of a combination
            if number in sums_of_nums:
                # move the prev_nums across by one
                start += 1
                end += 1
            # if the next number is not the sum of a combination return
            else:
                return number


# part 2 code
def part_2(nums: list[int], value_to_sum: int) -> int:
    # iterate through the list using their indices
    for start, _ in enumerate(nums):
        # start iterating away from the current number
        for end in range(start, len(nums)):
            # list for the contiguous set to test
            cont_set = nums[start:end]

            # if the contiguous set to test is over the sum we want
            if sum(cont_set) > value_to_sum:
                # skip to next starting number
                break
            # if the sum is what we want then return min and max of the set
            if sum(cont_set) == value_to_sum:
                return min(cont_set) + max(cont_set)


# driver code
if __name__ == "__main__":
    # handle the input into a list of integers
    data = handle_input()

    # call part 1 on the data and save the result for part 2
    part_1_result = part_1(data, 25)

    print("Part 1:", part_1_result)
    print("Part 2:", part_2(data, part_1_result))
