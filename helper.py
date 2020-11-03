import requests
from bs4 import BeautifulSoup


def get_content(url: str, selected_element_id: str) -> BeautifulSoup:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id=selected_element_id)

    return results