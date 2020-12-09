# import copy to deepcopy the instructions list in part 2
import copy


# function to create a list from input
def handle_input() -> list[list[str]]:
    with open("input.txt", "r") as f:
        # read in the input file as create a list without \n
        output = f.read().splitlines()
    # create a 2 item list by splitting the instructions into [operation, arg]
    output = list(map(lambda x: x.split(), output))

    return output


# part 1 code
def part_1(instructions: list[list[str]]) -> (bool, int):
    # current index of instruction being run
    index = 0
    accumulate = 0
    # list of indexes that have been run already
    index_seen = []

    # loop until we run into an index we've checked or we've terminated
    while index not in index_seen and index < len(instructions):
        index_seen.append(index)
        # if the instruction is "nop" then just increment index by 1
        if instructions[index][0] == "nop":
            index += 1
        # if instruction is "acc" then add the value of acc and increment index
        elif instructions[index][0] == "acc":
            accumulate += int(instructions[index][1])
            index += 1
        # if instruction is jump then add the arg to index
        else:
            index += int(instructions[index][1])

    # if the game terminated then return True and accumulate
    if index >= len(instructions):
        return True, accumulate
    # else return False and accumulate
    return False, accumulate


# part 2 code
def part_2(instructions: list[list[str]]) -> int:
    # loop through the instructions using their indices
    for index in range(len(instructions)):
        # copy a testing instructions as we will modify it
        test_instr = copy.deepcopy(instructions)
        # if the instruction at index is "jmp", replace "jmp" with "nop"
        if test_instr[index][0] == "jmp":
            test_instr[index][0] = "nop"
        # else if the instruction at index is "nop", replace "nop" with "jmp"
        elif test_instr[index][0] == "nop":
            test_instr[index][0] = "jmp"
        # test the modified instruction using part_1 function
        result = part_1(test_instr)

        # if the instructions terminated then results[0] will be True
        if result[0] is True:
            # so return accumulate
            return result[1]


# driver code
if __name__ == "__main__":
    # handle the input file and create nested lists for the instructions
    instructions = handle_input()
    # part 1 needs [1] as [0] is False (irrelevant to answer)
    print("Part 1:", part_1(instructions)[1])
    print("Part 2:", part_2(instructions))
