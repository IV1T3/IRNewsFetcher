import time

import argparser
from Company import Company


def display_structured_press_releases(press_releases: list, weeks: int) -> None:
    now = time.time()

    for press_release in press_releases:
        if weeks == -1 or (
            weeks != -1 and (now - press_release[1]) < (60 * 60 * 24 * 7 * weeks)
        ):
            print(press_release[3], "-", press_release[6])
            print(press_release[2])
            print("")
            if press_release[5] != []:
                print(press_release[5])
            print("Link:", press_release[4])
            print("", end="\n")
            # print(press_release)
            print("----", end="\n" * 2)


if __name__ == "__main__":
    args = argparser.get_args()

    valid_companies = [
        "aapl",
        "fb",
        "goog",
        "jnj",
        "msft",
        "nflx",
        "nvda",
        "tsla",
        "ul",
    ]
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

    display_structured_press_releases(all_structured_press_releases, args.weeks)
