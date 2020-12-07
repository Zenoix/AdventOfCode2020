import re


def handle_input():
    with open("input.txt", "r") as f:
        rules = f.read().splitlines()
    return rules


def part_1(rules):
    output = set()
    current = set()
    while not output or current:
        previous = current.copy()
        output |= previous
        current = set()

        if not previous:
            previous = ["shiny gold"]
        for rule in rules:
            for a in previous:
                add = re.findall("^(.+) bags .+%s" % a, rule)
                if add:
                    current.add(add[0])

    return len(output)


def part_2(rules):

    return


if __name__ == "__main__":
    rules = handle_input()
    print(part_1(rules))
    print(part_2(rules))
        

