from collections import Counter


def part_1():
    with open("input.txt", "r") as f:
        data = f.read()
        groups = [group.replace("\n", "") for group in data.split("\n\n")]
        distinct_letters = [len(set(group)) for group in groups]
        return sum(distinct_letters)


def part_2():
    with open("input.txt", "r") as f:
        data = f.read()
        groups = data.split("\n\n")
        people = [group.split() for group in groups]
        lis = []
        output = 0
        for group in people:
            a = Counter()
            for person in group:
                a += Counter(person)
            lis.append(a)
        for index, counter in enumerate(lis):
            for v in counter.values():
                if v == len(people[index]):
                    output += 1
        return output


print(part_1())
print(part_2())
