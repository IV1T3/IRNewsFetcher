from bs4 import BeautifulSoup
import requests
import datetime

import pagedata


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.page_content = self.fetch_page_content()
        self.full_press_releases = self.parse_all_press_releases()
        self.clean_press_releases = self.clean_all_press_releases()
        self.titles = self.parse_titles()
        self.dates, self.timestamps = self.parse_dates()
        self.links = self.parse_links()

    def fetch_page_content(self) -> BeautifulSoup:
        url_press = ""
        if self.name == "Tesla":
            url_press = pagedata.tesla_url_press
            selected_element_id = pagedata.tesla_main_id
        elif self.name == "Apple":
            url_press = pagedata.apple_url_press
            selected_element_id = pagedata.apple_main_id
        elif self.name == "Nvidia":
            url_press = pagedata.nvidia_url_press
            selected_element_id = pagedata.nvidia_main_id
        page = requests.get(url_press)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id=selected_element_id)

        return results

    def parse_all_press_releases(self) -> BeautifulSoup:
        page_content = self.page_content

        if self.name == "Tesla":
            pagedata_tag = pagedata.tesla_press_releases[0]
            pagedata_attr = pagedata.tesla_press_releases[1]
            pagedata_attr_val = pagedata.tesla_press_releases[2]
        elif self.name == "Apple":
            pagedata_tag = pagedata.apple_press_releases[0]
            pagedata_attr = pagedata.apple_press_releases[1]
            pagedata_attr_val = pagedata.apple_press_releases[2]
        elif self.name == "Nvidia":
            pagedata_tag = pagedata.nvidia_press_releases[0]
            pagedata_attr = pagedata.nvidia_press_releases[1]
            pagedata_attr_val = pagedata.nvidia_press_releases[2]

        press_releases = page_content.find_all(
            pagedata_tag, {pagedata_attr: pagedata_attr_val}
        )

        return press_releases

    def clean_all_press_releases(self) -> BeautifulSoup:
        clean_press_releases = []
        parse_clean = True

        for full_press_release in self.full_press_releases:
            clean_press_release = []

            # Pre-Cleaning
            if self.name == "Tesla":
                pagedata_tag = pagedata.tesla_press_releases_clean[0]
                pagedata_attr = pagedata.tesla_press_releases_clean[1]
                pagedata_attr_val = pagedata.tesla_press_releases_clean[2]

            if self.name == "Nvidia":
                pagedata_tag = pagedata.nvidia_press_releases_clean[0]
                pagedata_attr = pagedata.nvidia_press_releases_clean[1]
                pagedata_attr_val = pagedata.nvidia_press_releases_clean[2]

            if self.name == "Apple":
                parse_clean = False

            # Cleaning
            if parse_clean:
                clean_press_release = full_press_release.find(
                    pagedata_tag, {pagedata_attr: pagedata_attr_val}
                )

            if self.name == "Tesla":
                clean_press_release = clean_press_release.find_all("div")[2].contents[0]
            elif self.name == "Nvidia":
                clean_press_release = clean_press_release.contents[0]

            # Post-Cleaning
            clean_press_releases.append(clean_press_release)

        return clean_press_releases

    def parse_titles(self) -> list:
        titles = []
        for press_release in self.full_press_releases:

            # Pre-Parsing
            if self.name == "Tesla":
                pagedata_tag = pagedata.tesla_press_release_title[0]
                pagedata_attr = pagedata.tesla_press_release_title[1]
                pagedata_attr_val = pagedata.tesla_press_release_title[2]
                pagedata_tag_two = pagedata.tesla_press_release_title[3]
            elif self.name == "Apple":
                pagedata_tag = pagedata.apple_press_release_title[0]
                pagedata_attr = pagedata.apple_press_release_title[1]
                pagedata_attr_val = pagedata.apple_press_release_title[2]
            elif self.name == "Nvidia":
                pagedata_tag = pagedata.nvidia_press_release_title[0]
                pagedata_attr = pagedata.nvidia_press_release_title[1]
                pagedata_attr_val = pagedata.nvidia_press_release_title[2]

            # Parsing
            title = press_release.find(pagedata_tag, {pagedata_attr: pagedata_attr_val})

            if self.name == "Tesla":
                title = title.find(pagedata_tag_two)
            elif self.name == "Nvidia":
                title = title.find("a")

            title = title.contents[0]

            while title[0] == "\n" or title[0] == " ":
                title = title[1:]

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
            if self.name == "Tesla":
                pagedata_tag = pagedata.tesla_press_release_date[0]
                pagedata_attr = pagedata.tesla_press_release_date[1]
                pagedata_attr_val = pagedata.tesla_press_release_date[2]
                pagedata_tag_two = pagedata.tesla_press_release_date[3]
            elif self.name == "Apple":
                pagedata_tag = pagedata.apple_press_release_date[0]
                pagedata_attr = pagedata.apple_press_release_date[1]
                pagedata_attr_val = pagedata.apple_press_release_date[2]
            elif self.name == "Nvidia":
                pagedata_tag = pagedata.nvidia_press_release_date[0]
                pagedata_attr = pagedata.nvidia_press_release_date[1]
                pagedata_attr_val = pagedata.nvidia_press_release_date[2]

            date = press_release.find(pagedata_tag, {pagedata_attr: pagedata_attr_val})

            if self.name == "Tesla":
                date = date.find(pagedata_tag_two)

            date = date.contents[0]

            if date.split()[0][:-1] in days:
                element = datetime.datetime.strptime(date, "%A, %B %d, %Y")
            elif date[3] == " ":
                element = datetime.datetime.strptime(date, "%b %d, %Y")
            else:
                element = datetime.datetime.strptime(date, "%B %d, %Y")
            timestamp = datetime.datetime.timestamp(element)

            dates.append(date)
            timestamps.append(timestamp)

        return dates, timestamps

    def parse_links(self) -> list:
        links = []
        for press_release in self.full_press_releases:
            link = press_release.find("a")["href"]
            if link[0] != "h":
                if self.name == "Tesla":
                    link = pagedata.tesla_ir_url_main + link
                elif self.name == "Apple":
                    link = pagedata.apple_url_main + link
            links.append(link)
        return links

    def display_news(self) -> None:
        for i in range(len(self.full_press_releases)):
            print(self.dates[i], "-", self.titles[i])
            if len(self.clean_press_releases[0]) > 0:
                print(self.clean_press_releases[i])
            print("Link:", self.links[i])
            print("-----", end="\n" * 2)
        print("------------- #### END ", self.name, "#### -----------------")

    def get_structured_press_releases(self) -> list:
        structured_press_releases = []
        for i in range(len(self.dates)):
            structured_press_release = [self.name, self.timestamps[i]]
            structured_press_release.append(self.titles[i])
            structured_press_release.append(self.dates[i])
            structured_press_release.append(self.links[i])
            structured_press_release.append(self.clean_press_releases[i])

            structured_press_releases.append(structured_press_release)

        return structured_press_releases
