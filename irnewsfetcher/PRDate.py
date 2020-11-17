import dateutil.parser

import time

from datetime import datetime
from typing import Tuple

from CustomExceptions import InvalidPRDateException


class PRDate(object):
    def __init__(self, company_data, press_release) -> None:
        self.company_data = company_data
        self.date, self.timestamp = self.__parse_date_and_timestamp(press_release)

    def __parse_date_and_timestamp(
        self,
        press_release,
    ) -> Tuple[str, datetime.timestamp]:

        # TODO: If no timestamp, PressRelease object can not be build
        new_date = ""
        timestamp = None

        if not press_release.find("th"):
            data_press_release_date = self.company_data["press_release_date"]

            date = None

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

            timestamp = datetime.timestamp(date)
            new_date = datetime.fromtimestamp(timestamp).strftime("%A, %B %d, %Y")

            return new_date, timestamp
        else:
            raise InvalidPRDateException(press_release)

    def get_date_and_timestamp(self) -> Tuple[str, datetime.timestamp]:
        return self.date, self.timestamp