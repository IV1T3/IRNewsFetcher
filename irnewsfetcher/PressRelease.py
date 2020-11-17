import bs4
import datetime

from typing import Tuple

from PRDate import PRDate
from PRDescription import PRDescription
from PRLink import PRLink
from PRTitle import PRTitle


class PressRelease(object):
    def __init__(self, company_data, press_release) -> None:
        self.company_data = company_data
        self.press_release = press_release

        self.title = self.__parse_title()
        self.link = self.__parse_link()
        self.date, self.timestamp = self.__parse_date_and_timestamp()

        self.description = self.__parse_description()

    def __parse_title(self) -> str:
        ticker = self.company_data["ticker"]
        title_object = PRTitle(ticker, self.company_data, self.press_release)

        return title_object.get_title()

    def __parse_link(self) -> str:
        link_object = PRLink(self.company_data, self.press_release)

        return link_object.get_link()

    def __parse_date_and_timestamp(self) -> Tuple[str, datetime.datetime.timestamp]:
        date_object = PRDate(self.company_data, self.press_release)

        return date_object.get_date_and_timestamp()

    def __parse_description(self) -> bs4.BeautifulSoup:
        description_object = PRDescription(self.company_data, self.press_release)

        return description_object.get_description()

    def get_structured_press_release(self) -> list:
        structured_press_release = [
            self.company_data["ticker"],
            self.timestamp,
            self.title,
            self.date,
            self.link,
            self.description,
            self.company_data["company_name"],
        ]

        return structured_press_release
