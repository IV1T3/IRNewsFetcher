# TODO:
# - implement additional companies
# - implement sorting by date

# In Process:
# - Implement Apple

# DONE:
# - Refactor Company as class, then only fetch on each class
# - add argparser to only fetch releases from specific companies

import argparse
from Company import Company

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

    if args.tsla or args.all:
        tesla = Company("Tesla")
        tesla.display_news()
