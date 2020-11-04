import argparse
import argparser
from Company import Company


def display_structured_press_releases(press_releases: list) -> None:
    company_names = {
        "aapl": "Apple, Inc.",
        "jnj": "Johnson & Johnson",
        "msft": "Microsoft Corporation",
        "nvda": "NVIDIA Corporation",
        "tsla": "Tesla, Inc.",
    }

    for press_release in press_releases:
        print(press_release[3], "-", company_names[press_release[0]])
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

    valid_companies = ["appl", "jnj", "msft", "nvda", "tsla"]
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
