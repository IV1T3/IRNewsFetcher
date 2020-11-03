from bs4 import BeautifulSoup
import helper

# Tesla information
tesla_url_main = "https://ir.tesla.com"
tesl_url_press = "https://ir.tesla.com/press"
tesla_main_id = "main-content"
tesla_press_releases = ["section", "class", "press-release-teaser"]
tesla_press_release_title = ["h4", "class", "press-release-teaser__title", "a"]


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.press_releases = self.fetch_all_press_releases()
        self.titles = self.get_titles()

    def fetch_all_press_releases(self) -> BeautifulSoup:
        contents = BeautifulSoup()

        if self.name == "Tesla":
            contents = helper.get_content(tesl_url_press, tesla_main_id)
            html_tag = tesla_press_releases[0]
            html_attr = tesla_press_releases[1]
            html_attr_val = tesla_press_releases[2]

        press_releases = contents.find_all(html_tag, {html_attr: html_attr_val})

        return press_releases

    def get_titles(self):
        titles = []
        for press_release in self.press_releases:
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

    def display_news(self) -> None:
        for i in range(len(self.press_releases)):
            print(self.titles[i])
            print(self.press_releases[i])
            print("-----", end="\n" * 2)
