from pathlib import Path
from typing import List
from urllib import request

INPUT_URL = r"https://adventofcode.com/{year}/day/{day}/input"


def get_input(year: int, day: int, force: bool = False) -> List[str]:
    """
    Reads the input file for the puzzle of the given year and day and
    returns it as a list of strings with newlines stripped. If input
    file does not exist, it will download it from adventofcode.com.

    You must have a valid cookie configured. See README for details.
    """
    year_input_dir = Path(f"{Path().absolute()}/input/{year}")
    year_input_dir.mkdir(exist_ok=True)
    input_file = Path(f"{year_input_dir}/{day}.txt")

    if force or not input_file.is_file() or input_file.stat().st_size == 0:
        with open(f"{Path().absolute()}/.cookie") as cookie:
            response = request.urlopen(
                request.Request(
                    f"{INPUT_URL}".format(year=year, day=day),
                    headers={"Cookie": cookie.read().strip()},
                )
            )

        with open(input_file, "w") as input:
            input.write(response.read().decode())

    with open(input_file, "r") as input:
        return input.read().splitlines()
