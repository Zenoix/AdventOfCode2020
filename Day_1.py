# import libraries
import itertools
from functools import reduce
import operator

# create list to hold the numbers
report = []

# open the file and add each number to report
with open("input.txt", "r") as f:
    for x in f:
        report.append(int(x.rstrip()))

# get input for the choice of how many numbers to add/multiply
n = int(input("How many numbers to sum and multiply? "))
# use itertool's combinations to find the combinations of n numbers
combs = list(itertools.combinations(report, n))

# go through each combination
for combination in combs:
    # if the sum of the combination is 2020
    if sum(combination) == 2020:
        # print the multiplication of the combination with reduce
        print(reduce(operator.mul, combination, 1))
        # stop the looping to save time and resources as only 1 answer
        break
# only if the combination of n does not exist for input file
else:
    print("Combination does not exist")
