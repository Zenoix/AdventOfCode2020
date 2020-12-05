# import regex
import re


# open and split the file into each passport
def handle_input() -> list:
    with open("input.txt", "r") as f:
        data = f.read()
        split_data = data.split("\n\n")
    return split_data


# check if passport contains all required values
def initial_check(values: str) -> bool:
    conditions = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(condition in values for condition in conditions)


# check if birth year is valid
def byr_check(value: str) -> bool:
    year = re.findall(r"\d\d\d\d", value)[0]
    return 1920 <= int(year) <= 2002


# check if issue year is valid
def iyr_check(value: str) -> bool:
    year = re.findall(r"\d\d\d\d", value)[0]
    return 2010 <= int(year) <= 2020


# check if expiration year is valid
def eyr_check(value: str) -> bool:
    year = re.findall(r"\d\d\d\d", value)[0]
    return 2020 <= int(year) <= 2030


# check if height is valid
def hgt_check(value: str) -> bool:
    # if in centimeters
    if value.endswith("cm"):
        height = re.findall(r":(\d\d\d)", value)
        if len(height) > 0:
            return 150 <= int(height[0]) <= 193
    # if in inches
    elif value.endswith("in"):
        height = re.findall(r":(\d\d)", value)
        if len(height) > 0:
            return 59 <= int(height[0]) <= 76
    return False


# check if hair color is valid
def hcl_check(value: str) -> bool:
    color = re.findall(r":#[0-9a-f]{6}", value)
    return len(color) > 0


# check if eye color is valid
def ecl_check(value: str) -> bool:
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for color in colors:
        if color in value:
            return True
    return False


# check if passport id is valid
def pid_check(value: str) -> bool:
    pid = re.findall(r":([0-9]*)", value)

    return len(pid) > 0 and len(pid[0]) == 9


# part 1
def part_1() -> int:
    valid = 0
    passports = handle_input()
    for passport in passports:
        # does passport have all required values?
        if initial_check(passport):
            valid += 1
    return valid


# part 2
def part_2() -> int:
    valid = 0
    passports = handle_input()
    for passport in passports:
        # only do part 2 check if it passes initial check
        if initial_check(passport):
            # split passport again into list of each value
            passport = passport.split()

            # checks will be a list of Trues and/or Falses
            checks = []

            # check each value and see if it's valid
            for value in passport:
                if value.startswith("byr"):
                    checks.append(byr_check(value))
                elif value.startswith("iyr"):
                    checks.append(iyr_check(value))
                elif value.startswith("eyr"):
                    checks.append(eyr_check(value))
                elif value.startswith("hgt"):
                    checks.append(hgt_check(value))
                elif value.startswith("hcl"):
                    checks.append(hcl_check(value))
                elif value.startswith("ecl"):
                    checks.append(ecl_check(value))
                elif value.startswith("pid"):
                    checks.append(pid_check(value))

            # passport is valid if all checks return True
            if all(checks):
                valid += 1

    return valid


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
