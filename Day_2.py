import re


def handle_string(line, selection):
    a = int(re.findall(r"^(\d+)", line)[0])
    b = int(re.findall(r"-(\d+)\s", line)[0])
    letter = re.findall(r"\s([a-z]):", line)[0]
    password = re.findall(r"[a-z]+$", line)[0]

    if selection == "1":
        check_password1(line, password, letter, a, b)
    elif selection == "2":
        check_password2(line, password, letter, a, b)


def check_password1(line, password, letter, a, b):
    global valid
    if a <= password.count(letter) <= b:
        valid += 1


def check_password2(line, password, letter, a, b):
    global valid
    condition1 = (password[a - 1] == letter) and (password[b - 1] != letter)
    condition2 = (password[b - 1] == letter) and (password[a - 1] != letter)
    if condition1 ^ condition2:
        valid += 1


if __name__ == '__main__':

    selection = input("Part 1 or Part 2: ")

    valid = 0

    with open("input.txt", "r") as f:
        for line in f:
            handle_string(line, selection)

    print(valid)
