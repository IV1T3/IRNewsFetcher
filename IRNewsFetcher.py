import requests
import pprint
from bs4 import BeautifulSoup
from Company import Company

# TODO:
# - implement additional companies
# - implement sorting by date
# - add argparser to only fetch releases from specific companies

# In Process:
# - Refactor each company as class, then only fetch on each class

MAIN_URLS = ["https://ir.tesla.com"]
PRESS_URLS = ["https://ir.tesla.com/press"]

ARR_PRESS_RELEASE_TITLES = []
ARR_PRESS_RELEASE_DATES = []
ARR_PRESS_RELEASE_LINKS = []
ARR_PRESS_RELEASE_CONTENTS = []


def get_content(url: str, selected_element_id: str) -> BeautifulSoup:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id=selected_element_id)

    return results


### New OOP approach ###
tesla = Company("Tesla")

print(tesla.press_releases)


### Old non OOP approach ###
for i in range(len(MAIN_URLS)):

    ARR_PRESS_RELEASE_TITLES.append([])
    ARR_PRESS_RELEASE_DATES.append([])
    ARR_PRESS_RELEASE_LINKS.append([])
    ARR_PRESS_RELEASE_CONTENTS.append([])

    press_url = PRESS_URLS[i]
    results = get_content(press_url, "main-content")

    press_releases = results.find_all("section", {"class": "press-release-teaser"})

    for press_release in press_releases:

        press_release_titles = ARR_PRESS_RELEASE_TITLES[i]
        press_release_dates = ARR_PRESS_RELEASE_DATES[i]
        press_release_links = ARR_PRESS_RELEASE_LINKS[i]
        press_release_contents = ARR_PRESS_RELEASE_CONTENTS[i]

        # Get Press Release Title
        full_title = press_release.find("h4", {"class": "press-release-teaser__title"})
        title = full_title.find("a").contents[0]

        # Get Press Release Link
        URL_press_release = MAIN_URLS[i] + full_title.find("a")["href"]

        # Get Press Release Content
        single_press_release_results = get_content(URL_press_release, "main-content")
        single_press_release_contents = single_press_release_results.find_all(
            "div", {"class": "press-release__body tds-text--body tds--vertical_padding"}
        )
        single_press_release_content = (
            single_press_release_contents[0].find("p").contents[0]
        )

        # Get Press Release Date
        single_press_release_dates = (
            single_press_release_results.find(
                "div", {"class", "press-release__date tds-text_color--35"}
            )
            .find("time")
            .contents[0]
        )

        press_release_titles.append(title)
        press_release_dates.append(single_press_release_dates)
        press_release_links.append(URL_press_release)
        press_release_contents.append(single_press_release_content)


# for i in range(len(ARR_PRESS_RELEASE_TITLES)):
#  for j in range(len(ARR_PRESS_RELEASE_TITLES[i])):
# print(ARR_PRESS_RELEASE_DATES[i][j], "-", ARR_PRESS_RELEASE_TITLES[i][j])
# print(ARR_PRESS_RELEASE_CONTENTS[i][j])
# print("Link:", ARR_PRESS_RELEASE_LINKS[i][j])

# print("-----", end="\n" * 2)
