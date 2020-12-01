import itertools
from functools import reduce
import operator

report = []

with open("report.txt", "r") as f:
    for x in f:
        report.append(int(x.rstrip()))

n = int(input("How many numbers to sum and multiply? "))
combs = list(itertools.combinations(report, n))

for combination in combs:
    if sum(combination) == 2020:
        print(reduce(operator.mul, combination, 1))
        break
else:
    print("Combination does not exist")
