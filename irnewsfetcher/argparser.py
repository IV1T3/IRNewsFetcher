import argparse


def init_argparse() -> argparse.ArgumentParser:
    my_parser = argparse.ArgumentParser("Fetch new IR press releases.")

    # General
    my_parser.add_argument(
        "--all",
        action="store_true",
        default=0,
        dest="all",
        help="Fetches all available new press releases.",
    )

    my_parser.add_argument(
        "--weeks",
        type=int,
        default=4,
        dest="weeks",
        help="Displays only press releases in the last weeks specified.",
    )

    # Companies
    my_parser.add_argument(
        "--AAPL",
        action="store_true",
        default=0,
        dest="aapl",
        help="Fetches new press releases from Apple Inc.",
    )
    my_parser.add_argument(
        "--BRK",
        action="store_true",
        default=0,
        dest="brk",
        help="Fetches new press releases from Berkshire Hathaway Inc.",
    )
    my_parser.add_argument(
        "--FB",
        action="store_true",
        default=0,
        dest="fb",
        help="Fetches new press releases from Facebook Inc.",
    )
    my_parser.add_argument(
        "--GOOG",
        action="store_true",
        default=0,
        dest="goog",
        help="Fetches new press releases from Alphabet Inc.",
    )
    my_parser.add_argument(
        "--JNJ",
        action="store_true",
        default=0,
        dest="jnj",
        help="Fetches new press releases from Johnson & Johnson",
    )
    my_parser.add_argument(
        "--LIN",
        action="store_true",
        default=0,
        dest="lin",
        help="Fetches new press releases from Linde plc",
    )
    my_parser.add_argument(
        "--MSFT",
        action="store_true",
        default=0,
        dest="msft",
        help="Fetches new press releases from Microsoft Corporation.",
    )
    my_parser.add_argument(
        "--NFLX",
        action="store_true",
        default=0,
        dest="nflx",
        help="Fetches new press releases from Netflix, Inc.",
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
    my_parser.add_argument(
        "--UL",
        action="store_true",
        default=0,
        dest="ul",
        help="Fetches new press releases from Unilever plc",
    )
    return my_parser


def get_args():
    parser = init_argparse()
    args = parser.parse_args()

    return args
