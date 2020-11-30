from typing import List


def part1(input: List[str]) -> int:
    report = sorted(map(int, input))

    for i in report:
        for j in report:
            if i != j and i + j == 2020:
                return i * j
            elif i + j > 2020:
                break

    raise Exception("🤷‍♂️")


def part2(input: List[str]) -> int:
    report = sorted(map(int, input))

    for i in report:
        for j in report:
            for k in report:
                if i != j and j != k and i + j + k == 2020:
                    return i * j * k
                elif i + j + k > 2020:
                    break

    raise Exception("🤷‍♂️")
