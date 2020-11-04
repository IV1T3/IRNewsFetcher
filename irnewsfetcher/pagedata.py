apple = {
    "url_press": "https://www.apple.com/newsroom",
    "url_press_prefix_noAcc": "https://www.apple.com",
    "url_press_prefix_wAcc": "https://www.apple.com",
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

johnson_and_johnson = {
    "url_press": "https://johnsonandjohnson.gcs-web.com/press-releases",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "",
    "main_id": "block-nir-pid2893-content",
    "press_releases": ["tr", "id", "noAcc"],
    "press_releases_clean": [],
    "press_release_title": [
        "div",
        "class",
        "nir-widget--field nir-widget--news--headline",
    ],
    "press_release_date": [
        "div",
        "class",
        "nir-widget--field nir-widget--news--date-time",
    ],
}

microsoft = {
    "url_press": "https://news.microsoft.com/category/press-releases/",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "",
    "main_id": "content",
    "press_releases": [
        "div",
        "class",
        "m-preview-content",
    ],
    "press_releases_clean": [],
    "press_release_title": ["a", "class", "f-post-link c-heading-6 m-chevron"],
    "press_release_date": [
        "div",
        "class",
        "c-paragraph-3 c-meta-text",
    ],
}

nvidia = {
    "url_press": "https://nvidianews.nvidia.com/news",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "https://nvidianews.nvidia.com",
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

tesla = {
    "url_press": "https://ir.tesla.com/press",
    "url_press_prefix_noAcc": "https://ir.tesla.com",
    "url_press_prefix_wAcc": "https://ir.tesla.com",
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

data_dict = {
    "aapl": apple,
    "jnj": johnson_and_johnson,
    "msft": microsoft,
    "nvda": nvidia,
    "tsla": tesla,
}
