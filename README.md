# IRNewsFetcher - Lightweight Investor Relation News Fetcher

*IRNewsFetcher* is a tool that helps you to keep up with the most recent press releases of selected companies.

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

Currently, there are two companies added to *IRNewsFetcher*:
- Apple
- Tesla

You can either choose to see the recent press releases of all currently implemented companies by running
```console
$ python3 irnewsfetcher/IRNewsFetcher.py --all
```

or select specific companies by adding their respective stock ticker symbol:
```console
$ python3 irnewsfetcher/IRNewsFetcher.py --TSLA
```