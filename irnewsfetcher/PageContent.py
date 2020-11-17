import bs4
import requests


class PageContent(object):
    def __init__(self, ticker, company_data) -> None:
        self._ticker = ticker
        self._company_data = company_data
        self._page_content = self._fetch_page_content()

    def _fetch_page_content(self) -> bs4.BeautifulSoup:
        url_press = self._company_data["url_press"]
        selected_element_id = self._company_data["main_id"]

        header = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url_press, headers=header)
        soup = bs4.BeautifulSoup(page.content, "html.parser")

        if selected_element_id == "":
            results = soup.find("body")
        else:
            results = soup.find(id=selected_element_id)

        return results

    def get_page_content(self) -> bs4.BeautifulSoup:
        return self._page_content