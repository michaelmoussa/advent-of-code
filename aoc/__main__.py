import importlib
import re
import time

import click

from aoc.input import get_input

PUZZLE_ID_REGEX = re.compile(r"^(?:(20[0-9]{2})(?:\:))?([0-9]{1,2})\.([12])?$")


@click.command(
    help=(
        "Runs the specified Advent of Code solution. The PUZZLE_ID uses the form "
        '"<YEAR>.<DAY><PART>" where YEAR is the 4-digit year, DAY is the 1 or 2 digit '
        'day and "<PART>" is the number "1" or "2". The year is optional and defaults '
        "to the current year."
    )
)
@click.argument("puzzle_id", type=str)
@click.option(
    "--refresh-input",
    is_flag=True,
    default=False,
    help="If the input file for the puzzle already exists, download it anyway.",
)
def main(puzzle_id: str, refresh_input: bool) -> None:
    try:
        (year, day, part) = PUZZLE_ID_REGEX.findall(puzzle_id)[0]
    except IndexError:
        raise IndexError(
            f'PUZZLE_ID must match regex {PUZZLE_ID_REGEX}, got "{puzzle_id}"'
        )

    year = int(time.strftime("%Y") if year is None else year)
    day = int(day)
    part = int(part)

    print(
        getattr(importlib.import_module(f"aoc.{year}.day{day}"), f"part{part}")(
            get_input(year, day, refresh_input)
        )
    )
