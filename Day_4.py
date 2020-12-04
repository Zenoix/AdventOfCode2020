import re


def handle_input() -> list:
    with open("input.txt", "r") as f:
        data = f.read()
        split_data = data.split("\n\n")
    return split_data


def initial_check(values: str) -> bool:
    conditions = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(condition in values for condition in conditions):
        return True
    return False


def byr_check(value: str) -> bool:
    year = re.findall(r"\d\d\d\d", value)[0]
    return 1920 <= int(year) <= 2002


def iyr_check(value: str) -> bool:
    year = re.findall(r"\d\d\d\d", value)[0]
    return 2010 <= int(year) <= 2020


def eyr_check(value: str) -> bool:
    year = re.findall(r"\d\d\d\d", value)[0]
    return 2020 <= int(year) <= 2030


def hgt_check(value: str) -> bool:
    if value.endswith("cm"):
        height = re.findall(r":(\d\d\d)", value)
        if len(height) > 0:
            return 150 <= int(height[0]) <= 193
    elif value.endswith("in"):
        height = re.findall(r":(\d\d)", value)
        if len(height) > 0:
            return 59 <= int(height[0]) <= 76
    return False


def hcl_check(value: str) -> bool:
    color = re.findall(r":#[0-9a-f]{6}", value)
    return len(color) > 0


def ecl_check(value: str) -> bool:
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for color in colors:
        if color in value:
            return True
    return False


def pid_check(value: str) -> bool:
    pid = re.findall(r":([0-9]*)", value)
    return len(pid) > 0 and len(pid[0]) == 9


def part_1() -> int:
    valid = 0
    passports = handle_input()
    for passport in passports:
        if initial_check(passport):
            valid += 1
    return valid


def part_2() -> int:
    valid = 0
    passports = handle_input()
    for passport in passports:
        if initial_check(passport):
            passport = passport.split()

            checks = []

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

            if all(checks):
                valid += 1

    return valid


if __name__ == "__main__":
    print(part_1())
    print(part_2())
