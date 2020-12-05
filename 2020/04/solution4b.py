import re

passports = open("input.txt").read().split("\n\n")

PARTS = [
    r"\s?byr:(19[2-9][0-9]|200[0-2])\s+",
    r"\s?iyr:(201[0-9]|2020)\s+",
    r"\s?eyr:(202[0-9]|2030)\s+",
    r"\s?hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)\s+",
    r"\s?hcl:(#[0-9a-f]{6})\s+",
    r"\s?ecl:(amb|blu|brn|gry|grn|hzl|oth)\s+",
    r"\s?pid:([0-9]{9})\s+"
]

def valid_passport(passport):
    valid = True

    passport = passport + " "
    for p in PARTS:
        m = re.search(p, passport)
        if m is None:
            valid = False
    
    return valid

valid_passports = 0
for passport in passports:
    if valid_passport(passport):
        valid_passports = valid_passports + 1

print(f"Valid passports: {valid_passports}")