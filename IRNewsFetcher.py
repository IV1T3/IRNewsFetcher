# TODO:
# - Implement additional companies
# - Add specific industries to choose from

# In Process:
# - Implement NVIDIA

# DONE:
# - 03.11.20: Refactor Company as class, then only fetch on each class
# - 03.11.20: add argparser to only fetch releases from specific companies
# - 03.11.20: Implement Apple
# - 03.11.20: Implement sorting by date

import argparse
import pprint
from Company import Company


def display_structured_press_releases(press_releases: list) -> None:
    for press_release in press_releases:
        print(press_release[3], "-", press_release[0], "-", press_release[2])
        if press_release[5] != []:
            print(press_release[5])
        print("Link:", press_release[4])
        print("", end="\n")
        print("----", end="\n" * 2)


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser("Fetch new IR press releases.")
    my_parser.add_argument(
        "--all",
        action="store_true",
        default=0,
        dest="all",
        help="Fetches all available new press releases.",
    )
    my_parser.add_argument(
        "--AAPL",
        action="store_true",
        default=0,
        dest="aapl",
        help="Fetches new press releases from Apple Inc.",
    )
    my_parser.add_argument(
        "--TSLA",
        action="store_true",
        default=0,
        dest="tsla",
        help="Fetches new press releases from Tesla, Inc.",
    )

    args = my_parser.parse_args()

    all_structured_press_releases = []

    if args.tsla or args.all:
        tesla = Company("Tesla")
        tesla_struct = tesla.get_structured_press_releases()
        all_structured_press_releases = [*all_structured_press_releases, *tesla_struct]

    if args.aapl or args.all:
        apple = Company("Apple")
        apple_struct = apple.get_structured_press_releases()
        all_structured_press_releases = [*all_structured_press_releases, *apple_struct]

    all_structured_press_releases.sort(key=lambda x: x[1])

    display_structured_press_releases(all_structured_press_releases)
