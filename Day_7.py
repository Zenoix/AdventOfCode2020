import re


def handle_input():
    with open("test.txt", "r") as f:
        rules = f.read().splitlines()
    return rules


def rules_to_dict(rules):
    output = {}
    for rule in rules:
        outer = re.findall(r"^(.+?) bag", rule)
        print(outer)
        inner = re.findall(r"\d (.+?) bag", rule)
        amount = re.findall(r"(\d+)", rule)
        output[outer[0]] = {k: v for k, v in zip(inner, amount)}
        
    return output


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


def part_2(rules: dict):
    if len(rules[next(iter(rules))]) == 0:
        return
    return


if __name__ == "__main__":
    rules = handle_input()
    rules_to_dict(rules)
    #print(part_1(rules))
    #print(part_2(rules))
        

