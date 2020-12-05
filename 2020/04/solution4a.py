import re

passports = open("input.txt").read().split("\n\n")

PARTS = [
    r".*byr:(\S+).*",
    r".*iyr:(\S+).*",
    r".*eyr:(\S+).*",
    r".*hgt:(\S+).*",
    r".*hcl:(\S+).*",
    r".*ecl:(\S+).*",
    r".*pid:(\S+).*",
    #r".*cid:(\S+).*"
]

def valid_passport(passport):
    valid = True

    for p in PARTS:
        m = re.match(p, passport, re.DOTALL)
        if m == None:
            valid = False
            break

    return valid

valid_passports = 0
for passport in passports:
    if valid_passport(passport):
        valid_passports = valid_passports + 1

print(f"Valid passports: {valid_passports}")

