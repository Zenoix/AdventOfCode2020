# import Counter
from collections import Counter


# function to handle the input into a initially unclean list
def handle_input():
    with open("input.txt", "r") as f:
        data = f.read()
        # seperate the groups
        groups_list = data.split("\n\n")
    return groups_list


# part 1 function
def part_1() -> int:
    unclean_groups = handle_input()
    # remove "\n" characters in the list elements
    groups = [group.replace("\n", "") for group in unclean_groups]
    # find number of destinct letters
    distinct_letters = [len(set(group)) for group in groups]
    return sum(distinct_letters)


# part 2 function
def part_2() -> int:
    unclean_groups = handle_input()
    # seperate the each group into arrays of people's ans
    people = [group.split() for group in unclean_groups]

    # list to store the number of yeses to a qu for each group
    group_yes = []
    # output variable
    output = 0

    # loop through the groups
    for group in people:
        # create a counter for the number of yeses to a question
        yes_ans = Counter()
        # loop through each person in the group
        for person in group:
            # add the occurances of the yeses to a question
            yes_ans += Counter(person)
        # append the total number of yeses for each question
        group_yes.append(yes_ans)

    # loop through total number of yeses for each question per group
    for idx, counter in enumerate(group_yes):
        # check the number of yeses for each question
        for v in counter.values():
            # if the number of yeses == number of people in group
            if v == len(people[idx]):
                # add 1 to output
                output += 1
    return output


# driver code
if __name__ == "__main__":
    print("Part 1", part_1())
    print("Part 2", part_2())
