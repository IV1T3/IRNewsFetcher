from datetime import date
import bs4

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
        descriptions = []

        for press_release in self.full_press_releases:

            press_release_object = PressRelease.PressRelease(
                self.company_data, press_release
            )
            description = press_release_object.description

            descriptions.append(description)

        return descriptions

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

            press_release_object = PressRelease.PressRelease(
                self.company_data, press_release
            )

            dates.append(press_release_object.date)
            timestamps.append(press_release_object.timestamp)

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
