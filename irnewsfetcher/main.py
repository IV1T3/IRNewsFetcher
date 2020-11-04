import argparse
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
        dest="apple",
        help="Fetches new press releases from Apple Inc.",
    )
    my_parser.add_argument(
        "--MSFT",
        action="store_true",
        default=0,
        dest="microsoft",
        help="Fetches new press releases from Microsoft Corporation.",
    )
    my_parser.add_argument(
        "--NVDA",
        action="store_true",
        default=0,
        dest="nvidia",
        help="Fetches new press releases from Nvidia Corporation",
    )
    my_parser.add_argument(
        "--TSLA",
        action="store_true",
        default=0,
        dest="tesla",
        help="Fetches new press releases from Tesla, Inc.",
    )

    args = my_parser.parse_args()

    valid_companies = ["apple", "microsoft", "nvidia", "tesla"]
    all_structured_press_releases = []

    for arg in vars(args):
        if arg in valid_companies and (getattr(args, arg) or args.all):
            company = Company(arg)
            company_struct = company.get_structured_press_releases()
            all_structured_press_releases = [
                *all_structured_press_releases,
                *company_struct,
            ]

    all_structured_press_releases.sort(key=lambda x: x[1])

    display_structured_press_releases(all_structured_press_releases)
