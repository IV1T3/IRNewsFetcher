from bs4 import BeautifulSoup
import requests

# TSLA information
tesla_ir_url_main = "https://ir.tesla.com"
tesla_url_press = "https://ir.tesla.com/press"
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

# AAPL information
apple_ir_url_main = "https://www.apple.com"
apple_url_press = "https://www.apple.com/newsroom"
apple_main_id = "main"
apple_press_releases = ["li", "class", "tile-item"]
apple_press_releases_clean = []
apple_press_release_title = ["div", "class", "tile__headline"]
apple_press_release_date = [
    "div",
    "class",
    "tile__timestamp icon-hide icon icon-before icon-clock",
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
            url_press = tesla_url_press
            selected_element_id = tesla_main_id
        elif self.name == "Apple":
            url_press = apple_url_press
            selected_element_id = apple_main_id
        page = requests.get(url_press)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id=selected_element_id)

        return results

    def parse_all_press_releases(self) -> BeautifulSoup:
        page_content = self.page_content

        if self.name == "Tesla":
            html_tag = tesla_press_releases[0]
            html_attr = tesla_press_releases[1]
            html_attr_val = tesla_press_releases[2]
        elif self.name == "Apple":
            html_tag = apple_press_releases[0]
            html_attr = apple_press_releases[1]
            html_attr_val = apple_press_releases[2]

        press_releases = page_content.find_all(html_tag, {html_attr: html_attr_val})

        return press_releases

    def clean_all_press_releases(self) -> BeautifulSoup:
        clean_press_releases = []
        parse_clean = True

        for full_press_release in self.full_press_releases:
            clean_press_release = []

            # Pre-Cleaning
            if self.name == "Tesla":
                html_tag = tesla_press_releases_clean[0]
                html_attr = tesla_press_releases_clean[1]
                html_attr_val = tesla_press_releases_clean[2]

            if self.name == "Apple":
                parse_clean = False

            # Cleaning
            if parse_clean:
                clean_press_release = full_press_release.find(
                    html_tag, {html_attr: html_attr_val}
                )

            if self.name == "Tesla":
                clean_press_release = clean_press_release.find_all("div")[2].contents[0]

            # Post-Cleaning
            clean_press_releases.append(clean_press_release)

        return clean_press_releases

    def parse_titles(self) -> list:
        titles = []
        for press_release in self.full_press_releases:

            # Pre-Parsing
            if self.name == "Tesla":
                html_tag = tesla_press_release_title[0]
                html_attr = tesla_press_release_title[1]
                html_attr_val = tesla_press_release_title[2]
                html_tag_two = tesla_press_release_title[3]

            if self.name == "Apple":
                html_tag = apple_press_release_title[0]
                html_attr = apple_press_release_title[1]
                html_attr_val = apple_press_release_title[2]

            # Parsing
            title = press_release.find(html_tag, {html_attr: html_attr_val})

            if self.name == "Tesla":
                title = title.find(html_tag_two)

            title = title.contents[0]

            # Post-Parsing
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
            elif self.name == "Apple":
                html_tag = apple_press_release_date[0]
                html_attr = apple_press_release_date[1]
                html_attr_val = apple_press_release_date[2]

            date = press_release.find(html_tag, {html_attr: html_attr_val})

            if self.name == "Tesla":
                date = date.find(html_tag_two)

            date = date.contents[0]

            dates.append(date)
        return dates

    def parse_links(self) -> list:
        links = []
        for press_release in self.full_press_releases:
            link = press_release.find("a")["href"]
            if link[0] != "h":
                if self.name == "Tesla":
                    link = tesla_ir_url_main + link
                elif self.name == "Apple":
                    link = apple_ir_url_main + link
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
        return
