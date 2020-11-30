import importlib
from functools import lru_cache
from pathlib import Path
from typing import List, Tuple

import pytest


def solve(year: int, day: int, part: int, input: List[str]) -> str:
    solver = getattr(importlib.import_module(f"aoc.{year}.day{day}"), f"part{part}")
    return str(solver(input))


@pytest.mark.parametrize("year", [2020])
@pytest.mark.parametrize("day", range(1, 26))
@pytest.mark.parametrize("part", [1, 2])
def test_aoc(year: int, day: int, part: int) -> None:
    (input, expected) = get_sample(year, day)

    try:
        assert solve(year, day, part, input) == expected[part - 1]
    except ModuleNotFoundError:
        pytest.skip(f"Skipping {year}.{day}.{part} (not solved yet, it seems!)")


@lru_cache
def get_sample(year: int, day: int) -> Tuple[List[str], Tuple[str, str]]:
    try:
        with open(f"{Path().absolute()}/tests/samples/{year}/{day}.txt") as f:
            samples = f.read().split("---------------------\n")
    except FileNotFoundError:
        return ([], ("", ""))
    else:
        return (samples[0].splitlines(), (samples[1].strip(), samples[2].strip()))
