import datetime
import requests

from bs4 import BeautifulSoup
from dateutil import parser

import pagedata


class Company:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self.name = pagedata.company_dict[self.ticker]["company_name"]
        self.page_content = self.fetch_page_content()
        self.full_press_releases = self.parse_all_press_releases()
        self.clean_press_releases = self.clean_all_press_releases()
        self.titles = self.parse_titles()
        self.dates, self.timestamps = self.parse_dates()
        self.links = self.parse_links()

    def fetch_page_content(self) -> BeautifulSoup:
        url_press = pagedata.company_dict[self.ticker]["url_press"]
        selected_element_id = pagedata.company_dict[self.ticker]["main_id"]

        header = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url_press, headers=header)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id=selected_element_id)

        return results

    def parse_all_press_releases(self) -> BeautifulSoup:
        page_content = self.page_content

        pagedata_tag = pagedata.company_dict[self.ticker]["press_releases"][0]
        pagedata_attr = pagedata.company_dict[self.ticker]["press_releases"][1]
        pagedata_attr_val = pagedata.company_dict[self.ticker]["press_releases"][2]

        press_releases = page_content.find_all(
            pagedata_tag, {pagedata_attr: pagedata_attr_val}
        )

        return press_releases

    def clean_all_press_releases(self) -> BeautifulSoup:
        clean_press_releases = []

        for full_press_release in self.full_press_releases:
            clean_press_release = []
            pagedata_tag, pagedata_attr, pagedata_attr_val = [], [], []

            no_press_release_teaser = ["aapl", "jnj", "msft", "ul"]

            if self.ticker not in no_press_release_teaser:
                pagedata_tag = pagedata.company_dict[self.ticker][
                    "press_releases_clean"
                ][0]
                pagedata_attr = pagedata.company_dict[self.ticker][
                    "press_releases_clean"
                ][1]
                pagedata_attr_val = pagedata.company_dict[self.ticker][
                    "press_releases_clean"
                ][2]

            # Cleaning
            if pagedata_tag != []:
                clean_press_release = full_press_release.find(
                    pagedata_tag, {pagedata_attr: pagedata_attr_val}
                )

            if self.ticker == "tsla":
                clean_press_release = clean_press_release.find_all("div")[2].contents[0]
            elif self.ticker == "nvda":
                clean_press_release = clean_press_release.contents[0]

            if self.ticker not in no_press_release_teaser:
                clean_press_release = clean_press_release.lstrip().rstrip()

            # Post-Cleaning
            clean_press_releases.append(clean_press_release)

        return clean_press_releases

    def parse_titles(self) -> list:
        titles = []
        for press_release in self.full_press_releases:
            pagedata_tag = pagedata.company_dict[self.ticker]["press_release_title"][0]
            pagedata_attr = pagedata.company_dict[self.ticker]["press_release_title"][1]
            pagedata_attr_val = pagedata.company_dict[self.ticker][
                "press_release_title"
            ][2]

            if self.ticker == "tsla":
                pagedata_tag_two = pagedata.company_dict[self.ticker][
                    "press_release_title"
                ][3]

            # Parsing
            title = press_release.find(pagedata_tag, {pagedata_attr: pagedata_attr_val})

            if self.ticker == "tsla":
                title = title.find(pagedata_tag_two)
            elif self.ticker == "nvda":
                title = title.find("a")

            if self.ticker == "jnj":
                title = title.contents[1].contents[0]
            else:
                title = title.contents[0]

            title = title.lstrip().rstrip()

            # Post-Parsing
            titles.append(title)

        return titles

    def parse_dates(self) -> list:
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        dates, timestamps = [], []
        for press_release in self.full_press_releases:
            pagedata_tag = pagedata.company_dict[self.ticker]["press_release_date"][0]
            pagedata_attr = pagedata.company_dict[self.ticker]["press_release_date"][1]
            pagedata_attr_val = pagedata.company_dict[self.ticker][
                "press_release_date"
            ][2]

            if self.ticker == "tsla":
                pagedata_tag_two = pagedata.company_dict[self.ticker][
                    "press_release_date"
                ][3]

            date = press_release.find(pagedata_tag, {pagedata_attr: pagedata_attr_val})

            if self.ticker == "tsla":
                date = date.find(pagedata_tag_two)

            if self.ticker == "jnj":
                date = date.contents[1]
            else:
                date = date.contents[0]

            date = date.lstrip().rstrip()

            is_day_first = False
            if self.ticker == "ul":
                is_day_first = True

            date = parser.parse(date, dayfirst=is_day_first)

            timestamp = datetime.datetime.timestamp(date)
            new_date = datetime.datetime.fromtimestamp(timestamp).strftime(
                "%A, %B %d, %Y"
            )

            dates.append(new_date)
            timestamps.append(timestamp)

        return dates, timestamps

    def parse_links(self) -> list:
        links = []
        for press_release in self.full_press_releases:
            link = press_release.find("a")["href"]

            link = pagedata.company_dict[self.ticker]["url_press_prefix_noAcc"] + link

            if link[0] == "/":
                link = (
                    pagedata.company_dict[self.ticker]["url_press_prefix_wAcc"] + link
                )

            links.append(link)
        return links

    def display_news(self) -> None:
        for i in range(len(self.full_press_releases)):
            print(self.dates[i], "-", self.titles[i])
            if len(self.clean_press_releases[0]) > 0:
                print(self.clean_press_releases[i])
            print("Link:", self.links[i])
            print("-----", end="\n" * 2)
        print("------------- #### END ", self.ticker, "#### -----------------")

    def get_structured_press_releases(self) -> list:
        structured_press_releases = []
        for i in range(len(self.dates)):
            structured_press_release = [self.ticker, self.timestamps[i]]
            structured_press_release.append(self.titles[i])
            structured_press_release.append(self.dates[i])
            structured_press_release.append(self.links[i])
            structured_press_release.append(self.clean_press_releases[i])
            structured_press_release.append(self.name)

            structured_press_releases.append(structured_press_release)

        return structured_press_releases
