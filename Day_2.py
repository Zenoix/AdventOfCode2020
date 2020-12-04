# import regex
import re


# handle each line
def handle_string(line, selection):
    # first number
    a = int(re.findall(r"^(\d+)", line)[0])
    # second number
    b = int(re.findall(r"-(\d+)\s", line)[0])
    # letter to verify password on
    letter = re.findall(r"\s([a-z]):", line)[0]
    # the password to check
    password = re.findall(r"[a-z]+$", line)[0]

    # run the password either on the old policy or new one
    if selection == "1":
        check_password1(line, password, letter, a, b)
    elif selection == "2":
        check_password2(line, password, letter, a, b)


# check old policy
def check_password1(line, password, letter, a, b):
    global valid
    if a <= password.count(letter) <= b:
        valid += 1


# check new policy
def check_password2(line, password, letter, a, b):
    global valid
    # define the two conditions
    condition1 = (password[a - 1] == letter) and (password[b - 1] != letter)
    condition2 = (password[b - 1] == letter) and (password[a - 1] != letter)
    # xor condition
    if condition1 ^ condition2:
        valid += 1


if __name__ == '__main__':
    # 1 for the old policy, 2 for the new policy
    selection = input("Part 1 or Part 2: ")
    # number of valid passwords
    valid = 0
    # open the input file
    with open("input.txt", "r") as f:
        for line in f:
            # for each line, run it through the checks
            handle_string(line, selection)
    # print the final result
    print(valid)
