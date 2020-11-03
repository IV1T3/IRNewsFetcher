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
apple_url_main = "https://www.apple.com"
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

# NVDA information
nvidia_url_main = "https://www.nvidia.com"
nvidia_url_press = "https://nvidianews.nvidia.com/news"
nvidia_main_id = "page-content"
nvidia_press_releases = ["article", "class", "index-item"]
nvidia_press_releases_clean = [
    "div",
    "class",
    "index-item-text-description",
]
nvidia_press_release_title = ["h3", "class", "index-item-text-title"]
nvidia_press_release_date = ["span", "class", "index-item-text-info-date"]