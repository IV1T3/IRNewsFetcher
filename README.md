# IRNewsFetcher - Lightweight Investor Relation News Fetcher

*IRNewsFetcher* is a CLI tool that helps you to keep up with the most recent press releases of selected companies.

## Installation

The Python *virtualenv* is recommended to use as a Python environment. This project requires Python3.

```console
$ git clone https://github.com/IV1T3/IRNewsFetcher.git
$ cd IRNewsFetcher
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## How to use?

Currently, these companies are added to *IRNewsFetcher*:

| Company           | Ticker |
|-------------------|--------|
| Apple             | AAPL   |
| Facebook          | FB     |
| Alphabet          | GOOG   |
| Johnson & Johnson | JNJ    |
| Microsoft         | MSFT   |
| Netflix           | NFLX   |
| Nvidia            | NVDA   |
| Tesla             | TSLA   |
| Unilever          | UL     |


To see all press releases of all currently implemented companies, run

```console
$ python3 irnewsfetcher/main.py --all --weeks=-1
```

To see only specific press releases in the last two weeks (default: 4 weeks), run

```console
$ python3 irnewsfetcher/main.py --AAPL --TSLA --weeks=2
```