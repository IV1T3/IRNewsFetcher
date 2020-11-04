tesla = {
    "url_main": "https://ir.tesla.com",
    "url_press": "https://ir.tesla.com/press",
    "main_id": "main-content",
    "press_releases": ["section", "class", "press-release-teaser"],
    "press_releases_clean": [
        "div",
        "class",
        "press-release-teaser__body tds-text--body",
    ],
    "press_release_title": ["h4", "class", "press-release-teaser__title", "a"],
    "press_release_date": [
        "div",
        "class",
        "press-release-teaser__date tds-text--caption tds-text_color--35",
        "time",
    ],
}

apple = {
    "url_main": "https://www.apple.com",
    "url_press": "https://www.apple.com/newsroom",
    "main_id": "main",
    "press_releases": ["li", "class", "tile-item"],
    "press_releases_clean": [],
    "press_release_title": ["div", "class", "tile__headline"],
    "press_release_date": [
        "div",
        "class",
        "tile__timestamp icon-hide icon icon-before icon-clock",
    ],
}

nvidia = {
    "url_main": "https://www.nvidia.com",
    "url_press": "https://nvidianews.nvidia.com/news",
    "main_id": "page-content",
    "press_releases": ["article", "class", "index-item"],
    "press_releases_clean": [
        "div",
        "class",
        "index-item-text-description",
    ],
    "press_release_title": ["h3", "class", "index-item-text-title"],
    "press_release_date": ["span", "class", "index-item-text-info-date"],
}

data_dict = {"apple": apple, "nvidia": nvidia, "tesla": tesla}