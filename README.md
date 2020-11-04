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
| Johnson & Johnson | JNJ    |
| Microsoft         | MSFT   |
| Nvidia            | NVDA   |
| Tesla             | TSLA   |

You can either choose to see the recent press releases of all currently implemented companies by running

```console
$ python3 irnewsfetcher/main.py --all
```

or select specific companies by adding their respective stock ticker symbol:

```console
$ python3 irnewsfetcher/main.py --AAPL --TSLA
```

Additionally, you can choose to display only press releases, which were published recently. Default is set to 4 weeks. However, you may change the value by using the weeks argument

```console
$ python3 irnewsfetcher/main.py --all --weeks=1
```
