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

    def get_structured_press_releases(self) -> list:
        structured_press_releases = []
        for press_release in self.full_press_releases:
            press_release_object = PressRelease.PressRelease(
                self.company_data, press_release
            )
            structured_press_release = (
                press_release_object.get_structured_press_release()
            )
            structured_press_releases.append(structured_press_release)

        return structured_press_releases
