import datetime
import requests

from bs4 import BeautifulSoup
from dateutil import parser


class Company:
    def __init__(self, ticker: str, company_data: dict) -> None:
        self.ticker = ticker
        self.company_data = company_data
        self.page_content = self.fetch_page_content()
        self.full_press_releases = self.parse_all_press_releases()
        self.clean_press_releases = self.clean_all_press_releases()
        self.titles = self.parse_titles()
        self.dates, self.timestamps = self.parse_dates()
        self.links = self.parse_links()

    def fetch_page_content(self) -> BeautifulSoup:
        url_press = self.company_data["url_press"]
        selected_element_id = self.company_data["main_id"]

        header = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url_press, headers=header)
        soup = BeautifulSoup(page.content, "html.parser")
        if selected_element_id == "":
            results = soup.find("body")
        else:
            results = soup.find(id=selected_element_id)

        return results

    def parse_all_press_releases(self) -> BeautifulSoup:
        page_content = self.page_content

        data_press_releases = self.company_data["press_releases"]

        if len(data_press_releases) > 1:
            pagedata_tag = data_press_releases[0]
            pagedata_attr = data_press_releases[1]
            pagedata_attr_val = data_press_releases[2]

            press_releases = page_content.find_all(
                pagedata_tag, {pagedata_attr: pagedata_attr_val}
            )
        else:
            pagedata_tag = data_press_releases[0]
            press_releases = page_content.find_all(pagedata_tag)

        return press_releases

    def clean_all_press_releases(self) -> BeautifulSoup:
        clean_press_releases = []

        for full_press_release in self.full_press_releases:
            clean_press_release = []
            pagedata_tag, pagedata_attr, pagedata_attr_val = [], [], []
            no_press_release_teaser = False

            data_press_release_clean = self.company_data["press_release_clean"]

            if len(data_press_release_clean) > 0:
                pagedata_tag = data_press_release_clean[0]

                if len(data_press_release_clean) > 1:
                    pagedata_attr = data_press_release_clean[1]

                    if len(data_press_release_clean) > 2:
                        pagedata_attr_val = data_press_release_clean[2]

                        clean_press_release = full_press_release.find(
                            pagedata_tag, {pagedata_attr: pagedata_attr_val}
                        )
                    else:
                        clean_press_release = full_press_release.find(
                            pagedata_tag
                        ).find(pagedata_attr)
                else:
                    clean_press_release = full_press_release.find(pagedata_tag)

                no_press_release_teaser = True

            if self.ticker == "tsla":
                clean_press_release = clean_press_release.find_all("div")[2].contents[0]
            elif self.ticker == "nvda" or self.ticker == "fb" or self.ticker == "lin":
                clean_press_release = clean_press_release.contents[0]

            if self.ticker == "lin":
                clean_press_release = clean_press_release.split("Linde")[1]
                clean_press_release = "Linde" + clean_press_release

            if no_press_release_teaser:
                clean_press_release = clean_press_release.lstrip().rstrip()

            clean_press_releases.append(clean_press_release)

        return clean_press_releases

    def parse_titles(self) -> list:
        titles = []
        for press_release in self.full_press_releases:
            data_press_release_title = self.company_data["press_release_title"]

            if len(data_press_release_title) > 0:
                pagedata_tag = data_press_release_title[0]

                if len(data_press_release_title) > 1:
                    pagedata_attr = data_press_release_title[1]

                    if len(data_press_release_title) > 2:
                        pagedata_attr_val = data_press_release_title[2]

                        if len(data_press_release_title) > 3:
                            pagedata_tag_two = data_press_release_title[3]

            # Parsing
            if len(data_press_release_title) == 1:
                title = press_release.find(pagedata_tag)
            elif len(data_press_release_title) > 2:
                title = press_release.find(
                    pagedata_tag, {pagedata_attr: pagedata_attr_val}
                )
            else:
                title = list(press_release)[2]

            if self.ticker == "tsla":
                title = title.find(pagedata_tag_two)
            elif self.ticker == "nvda" or self.ticker == "fb":
                title = title.find("a")

            if self.ticker == "jnj":
                title = title.contents[1].contents[0]
            elif self.ticker == "goog":
                carriage_index = title.index("\n")
                title = title[:carriage_index] + title[carriage_index + 18 :]
            elif self.ticker == "lin":
                title = title.contents[0].contents[0]
            else:
                title = title.contents[0]

            title = title.lstrip().rstrip()

            # Post-Parsing
            titles.append(title)

        return titles

    def parse_dates(self) -> list:
        dates, timestamps = [], []
        for press_release in self.full_press_releases:
            data_press_release_date = self.company_data["press_release_date"]

            if len(data_press_release_date) > 0:
                pagedata_tag = data_press_release_date[0]

                if len(data_press_release_date) > 1:
                    pagedata_attr = data_press_release_date[1]

                    if len(data_press_release_date) > 2:
                        pagedata_attr_val = data_press_release_date[2]

                        if len(data_press_release_date) > 3:
                            pagedata_tag_two = data_press_release_date[3]

                            date = press_release.find(
                                pagedata_tag, {pagedata_attr: pagedata_attr_val}
                            ).find(pagedata_tag_two)
                        else:
                            date = press_release.find(
                                pagedata_tag, {pagedata_attr: pagedata_attr_val}
                            )
                    else:
                        date = press_release.find(pagedata_tag).find(pagedata_attr)
                else:
                    date = press_release.find(pagedata_tag)

            if len(date) == 1:
                date = date.contents[0]
            else:
                date = date.contents[1]

            date = date.lstrip().rstrip()

            is_day_first = self.company_data["press_release_date_day_first"]

            if "at" in date:
                date = date.split("at")[0]

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
            init_link = press_release.find("a")["href"]

            if "earnings" in init_link:
                link = self.company_data["url_press_prefix_wAcc"] + init_link
            else:
                link = self.company_data["url_press_prefix_noAcc"] + init_link

            if link[0] == "/":
                link = self.company_data["url_press_prefix_wAcc"] + link

            links.append(link)
        return links

    def display_news(self) -> None:
        for i in range(len(self.full_press_releases)):
            print(self.dates[i], "-", self.titles[i])
            if len(self.clean_press_releases[0]) > 0:
                print(self.clean_press_releases[i] + "\n")
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
            structured_press_release.append(self.company_data["company_name"])

            structured_press_releases.append(structured_press_release)

        return structured_press_releases
