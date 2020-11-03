from bs4 import BeautifulSoup
import requests

# Tesla information
tesla_url_main = "https://ir.tesla.com"
tesl_url_press = "https://ir.tesla.com/press"
tesla_main_id = "main-content"
tesla_press_releases = ["section", "class", "press-release-teaser"]
tesla_press_releases_clean = [
    "div",
    "class",
    "press-release-teaser__body tds-text--body",
]
tesla_press_release_title = ["h4", "class", "press-release-teaser__title", "a"]
tesla_press_release_date = [
    "div",
    "class",
    "press-release-teaser__date tds-text--caption tds-text_color--35",
    "time",
]


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.page_content = self.fetch_page_content()
        self.full_press_releases = self.parse_all_press_releases()
        self.clean_press_releases = self.clean_all_press_releases()
        self.titles = self.parse_titles()
        self.dates = self.parse_dates()
        self.links = self.parse_links()

    def fetch_page_content(self) -> BeautifulSoup:
        url_press = ""
        if self.name == "Tesla":
            url_press = tesl_url_press
            selected_element_id = tesla_main_id
        page = requests.get(url_press)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id=selected_element_id)

        return results

    def parse_all_press_releases(self) -> BeautifulSoup:
        if self.name == "Tesla":
            page_content = self.page_content
            html_tag = tesla_press_releases[0]
            html_attr = tesla_press_releases[1]
            html_attr_val = tesla_press_releases[2]

        press_releases = page_content.find_all(html_tag, {html_attr: html_attr_val})

        return press_releases

    def clean_all_press_releases(self) -> BeautifulSoup:
        clean_press_releases = []
        for full_press_release in self.full_press_releases:
            if self.name == "Tesla":
                html_tag = tesla_press_releases_clean[0]
                html_attr = tesla_press_releases_clean[1]
                html_attr_val = tesla_press_releases_clean[2]

            clean_press_release = full_press_release.find(
                html_tag, {html_attr: html_attr_val}
            )

            if self.name == "Tesla":
                clean_press_release = clean_press_release.find_all("div")[2]

            clean_press_releases.append(clean_press_release)

        return clean_press_releases

    def parse_titles(self) -> list:
        titles = []
        for press_release in self.full_press_releases:
            if self.name == "Tesla":
                html_tag = tesla_press_release_title[0]
                html_attr = tesla_press_release_title[1]
                html_attr_val = tesla_press_release_title[2]
                html_tag_two = tesla_press_release_title[3]

            title = (
                press_release.find(html_tag, {html_attr: html_attr_val})
                .find(html_tag_two)
                .contents[0]
            )
            titles.append(title)

        return titles

    def parse_dates(self) -> list:
        dates = []
        for press_release in self.full_press_releases:
            if self.name == "Tesla":
                html_tag = tesla_press_release_date[0]
                html_attr = tesla_press_release_date[1]
                html_attr_val = tesla_press_release_date[2]
                html_tag_two = tesla_press_release_date[3]
            date = (
                press_release.find(html_tag, {html_attr: html_attr_val})
                .find(html_tag_two)
                .contents[0]
            )
            dates.append(date)
        return dates

    def parse_links(self) -> list:
        links = []
        for press_release in self.full_press_releases:
            link = press_release.find("a")["href"]
            if link[0] != "h":
                if self.name == "Tesla":
                    link = tesla_url_main + link
            links.append(link)
        return links

    def display_news(self) -> None:
        for i in range(len(self.full_press_releases)):
            print(self.dates[i], "-", self.titles[i])
            print(self.clean_press_releases[i])
            print("Link:", self.links[i])
            print("-----", end="\n" * 2)
