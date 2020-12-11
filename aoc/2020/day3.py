import functools
from typing import List


def part1(input: List[str]) -> int:
    return count_trees_hit(input, 3, 1)


def part2(input: List[str]) -> int:
    return functools.reduce(
        (lambda x, y: x * y),
        map(
            lambda slope: count_trees_hit(input, slope[0], slope[1]),
            [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)],
        ),
    )


def count_trees_hit(input: List[str], slope_x: int, slope_y: int) -> int:
    x_pos = 0
    trees_hit = 0

    for i in range(slope_y, len(input), slope_y):
        row = input[i]
        x_pos = (x_pos + slope_x) % len(row)
        trees_hit += 1 if row[x_pos] == "#" else 0

    return trees_hit
