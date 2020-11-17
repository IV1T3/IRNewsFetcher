import bs4
import datetime
import dateutil.parser

import PageContent
import PressRelease


class Company(object):
    def __init__(self, ticker: str, company_data: dict) -> None:
        self.ticker = ticker
        self.company_data = company_data
        self.page_content = PageContent.PageContent(ticker, company_data)

        self.full_press_releases = self.parse_all_press_releases()
        self.clean_press_releases = self.clean_all_press_releases()
        self.titles = self.parse_titles()
        self.dates, self.timestamps = self.parse_dates()
        self.links = self.parse_links()

    def parse_all_press_releases(self) -> bs4.BeautifulSoup:
        page_content = self.page_content.get_page_content()

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

    def clean_all_press_releases(self) -> bs4.BeautifulSoup:
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

            press_release_object = PressRelease.PressRelease(
                self.company_data, press_release
            )
            title = press_release_object.title

            # Post-Parsing
            titles.append(title)

        return titles

    def parse_dates(self) -> list:
        dates, timestamps = [], []
        for press_release in self.full_press_releases:
            if not press_release.find("th"):
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

                date = dateutil.parser.parse(date, dayfirst=is_day_first)

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

            press_release_object = PressRelease.PressRelease(
                self.company_data, press_release
            )
            link = press_release_object.link

            links.append(link)
        return links

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
