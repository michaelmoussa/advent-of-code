import re
from typing import List

PATTERN = re.compile(r"^([0-9]+)-([0-9]+) ([a-z]): (.+)$")


def part1(input: List[str]) -> int:
    valid = 0

    for line in input:
        try:
            (min, max, character, password) = PATTERN.findall(line)[0]
            if int(min) <= int(password.count(character)) <= int(max):
                valid += 1
        except IndexError:
            raise Exception("🤷‍♂️")

    return valid


def part2(input: List[str]) -> int:
    valid = 0

    for line in input:
        try:
            (first_pos, second_pos, character, password) = PATTERN.findall(line)[0]

            if (password[int(first_pos) - 1] == character) ^ (
                password[int(second_pos) - 1] == character
            ):
                valid += 1
        except IndexError:
            raise Exception("🤷‍♂️")

    return valid
