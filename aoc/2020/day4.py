import re
from typing import Iterator, List, Pattern

passport_fields = {
    "byr": r"(192[0-9]|19[3-9][0-9]|200[0-2])",
    "iyr": r"(201[0-9]|2020)",
    "eyr": r"(202[0-9]|2030)",
    "hgt": r"(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)",
    "hcl": r"#[0-9a-f]{6}",
    "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)",
    "pid": r"[0-9]{9}",
}


def part1(input: List[str]) -> int:
    return count_valid(input, re.compile(f"({'|'.join(passport_fields.keys())}):"))


def part2(input: List[str]) -> int:
    return count_valid(
        input,
        re.compile(
            f"({'|'.join([field[0] + ':' + field[1] + '( |$)' for field in passport_fields.items()])})"  # noqa: E501
        ),
    )


def count_valid(input: List[str], validator: Pattern[str]) -> int:
    return sum(
        [
            1 if len(validator.findall(passport)) == len(passport_fields) else 0
            for passport in passports(input)
        ]
    )


def passports(input: List[str]) -> Iterator[str]:
    position = 0

    for sep_idx in [i for i, line in enumerate(input) if line == ""] + [len(input)]:
        yield " ".join(input[position:sep_idx])
        position = sep_idx + 1
