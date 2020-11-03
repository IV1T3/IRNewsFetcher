from bs4 import BeautifulSoup
import helper

# Tesla information
tesla_url_main = "https://ir.tesla.com"
tesl_url_press = "https://ir.tesla.com/press"
tesla_main_id = "main-content"
tesla_press_releases = ["section", "class", "press-release-teaser"]
tesla_press_release_title = ["h4", "class", "press-release-teaser__title", "a", 0]


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.press_releases = self.fetch_all_press_releases()

    def fetch_all_press_releases(self):
        contents = BeautifulSoup()
        html_tag = "div"
        html_attr = "class"
        html_attr_val = "main-section"

        if self.name == "Tesla":
            contents = helper.get_content(tesl_url_press, tesla_main_id)
            html_tag = tesla_press_releases[0]
            html_attr = tesla_press_releases[1]
            html_attr_val = tesla_press_releases[2]

        press_releases = contents.find_all(html_tag, {html_attr: html_attr_val})

        return press_releases
