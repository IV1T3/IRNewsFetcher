import datetime
import datetime

from typing import Tuple

from PRTitle import PRTitle
from PRLink import PRLink


class PressRelease(object):
    def __init__(self, company_data, press_release) -> None:
        self.company_data = company_data
        self.press_release = press_release

        self.title = self.__parse_title()
        self.link = self.__parse_link()

        self.date = None
        self.timestamp = None

        self.description = None

    def __parse_title(self) -> str:
        ticker = self.company_data["ticker"]
        title_object = PRTitle(ticker, self.company_data, self.press_release)
        parsed_title = title_object.get_title()

        return parsed_title

    def __parse_link(self) -> str:
        link_object = PRLink(self.company_data, self.press_release)
        parsed_link = link_object.get_link()

        return parsed_link

    # def __parse_date_and_timestamp(self) -> Tuple(str, datetime.datetime.timestamp):
    #    pass
