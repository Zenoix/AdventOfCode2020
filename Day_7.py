# import regex
import re


# function to create a list from input
def handle_input() -> list[str]:
    with open("input.txt", "r") as f:
        # read in the input file as create a list without \n
        rules = f.read().splitlines()

    return rules


# create a dictionary for each bag and it's inner bags and amount
# for part 2
def rules_to_dict(rules: list[str]) -> dict:
    # initialise output dictionary
    output = {}

    # loop through the lists
    for rule in rules:
        # the outer bag's description
        outer = re.findall(r"^(.+?) bag", rule)
        # the inner bag's description
        inner = re.findall(r"\d (.+?) bag", rule)
        # the amount that each inner bag can carry converted to ints
        amount = map(int, re.findall(r"(\d+)", rule))
        # the output dictionary has the key as the outer bag's desc and the
        # value as a nested dictionary of the inner bag's desc and num of bags
        output[outer[0]] = {k: v for k, v in zip(inner, amount)}

    return output


# part 1 code (inefficient but can't be bothered optimising)
def part_1(rules: list[str]) -> int:
    # initialise empty output set
    output = set()
    # let outer be the bags that can carry the inner bags
    outer = set()
    # loop while output is empty or if outer has bags in it
    while not output or outer:
        # let inner be the previous outer bags that could carry the previous
        # iteration of inner bags
        inner = outer.copy()
        # add the bags into output
        output |= inner
        # empty the set of bags that can carry the inner bags
        outer = set()

        # if this is the first iteration (output is empty)
        # let the inner bag be "shiny gold"
        if not output:
            inner = ["shiny gold"]
        # loop through each rule
        for rule in rules:
            # loop through each of the inner bags that might be carriable by
            # the current bag we are checking in the rule
            for bag in inner:
                # if the inner bag is in the rule but not at the beginning
                add = re.findall("^(.+) bags .+%s" % bag, rule)
                # add it to outer set
                if add:
                    outer.add(add[0])

    return len(output)


# part 2 code
def part_2(key: str) -> int:
    # initialise the total amount of required inside the shiny gold bag
    output = 0

    # use recursion to find total number of bags inside of each bag
    # (I don't know how to explain this part)
    for inner_color, num_of_bags in bag_dict[key].items():
        output += num_of_bags * (1 + part_2(inner_color))

    return output


# driver code
if __name__ == "__main__":
    # get the rules as a list first
    rules = handle_input()
    # part 1 answer
    print("Part 1:", part_1(rules))

    # convert the list of rules into a dictionary
    bag_dict = rules_to_dict(rules)
    # part 2 answer with starting key as "shiny gold"
    print("Part 2:", part_2("shiny gold"))
