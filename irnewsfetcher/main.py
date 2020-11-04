import argparse
import pprint
from Company import Company


def display_structured_press_releases(press_releases: list) -> None:
    for press_release in press_releases:
        print(press_release[3], "-", press_release[0].capitalize())
        print(press_release[2])
        print("")
        if press_release[5] != []:
            print(press_release[5])
        print("Link:", press_release[4])
        print("", end="\n")
        # print(press_release)
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
        "--NVDA",
        action="store_true",
        default=0,
        dest="nvda",
        help="Fetches new press releases from Nvidia Corporation",
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

    if args.aapl or args.all:
        apple = Company("apple")
        apple_struct = apple.get_structured_press_releases()
        all_structured_press_releases = [*all_structured_press_releases, *apple_struct]

    if args.nvda or args.all:
        nvidia = Company("nvidia")
        nvidia_struct = nvidia.get_structured_press_releases()
        all_structured_press_releases = [*all_structured_press_releases, *nvidia_struct]

    if args.tsla or args.all:
        tesla = Company("tesla")
        tesla_struct = tesla.get_structured_press_releases()
        all_structured_press_releases = [*all_structured_press_releases, *tesla_struct]

    all_structured_press_releases.sort(key=lambda x: x[1])

    display_structured_press_releases(all_structured_press_releases)
