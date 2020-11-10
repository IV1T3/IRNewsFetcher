alphabet = {
    "rss": False,
    "company_name": "Alphabet Inc.",
    "url_press": "https://abc.xyz/investor",
    "url_press_prefix_noAcc": "https://abc.xyz/investor/",
    "url_press_prefix_wAcc": "https://abc.xyz",
    "main_id": "news",
    "press_releases": ["li"],
    "press_release_clean": [],
    "press_release_title": [],
    "press_release_date": ["div", "class", "date"],
    "press_release_date_day_first": False,
}

apple = {
    "rss": False,
    "company_name": "Apple Inc.",
    "url_press": "https://www.apple.com/newsroom",
    "url_press_prefix_noAcc": "https://www.apple.com",
    "url_press_prefix_wAcc": "https://www.apple.com",
    "main_id": "main",
    "press_releases": ["li", "class", "tile-item"],
    "press_release_clean": [],
    "press_release_title": ["div", "class", "tile__headline"],
    "press_release_date": [
        "div",
        "class",
        "tile__timestamp icon-hide icon icon-before icon-clock",
    ],
    "press_release_date_day_first": False,
}

berkshire_hathaway = {
    "rss": False,
    "company_name": "Berkshire Hathaway Inc.",
    "url_press": "https://www.berkshirehathaway.com/news/2020news.html",
    "url_press_prefix_noAcc": "https://www.berkshirehathaway.com/news/",
    "url_press_prefix_wAcc": "https://www.berkshirehathaway.com/news/",
    "main_id": "",
    "press_releases": ["dl"],
    "press_release_clean": [],
    "press_release_title": ["dd"],
    "press_release_date": ["dt", "a"],
    "press_release_date_day_first": False,
}

facebook = {
    "rss": False,
    "company_name": "Facebook Inc.",
    "url_press": "https://about.fb.com/news/",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "",
    "main_id": "posts",
    "press_releases": ["div", "class", "uk-grid"],
    "press_release_clean": ["div", "class", "article-excerpt-body"],
    "press_release_title": [
        "h3",
        "class",
        "entry-title uk-margin-remove-top ui-heading2",
    ],
    "press_release_date": ["span", "class", "posted-on", "time"],
    "press_release_date_day_first": False,
}

johnson_and_johnson = {
    "rss": False,
    "company_name": "Johnson & Johnson",
    "url_press": "https://johnsonandjohnson.gcs-web.com/press-releases",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "",
    "main_id": "block-nir-pid2893-content",
    "press_releases": ["tr", "id", "noAcc"],
    "press_release_clean": [],
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
    "press_release_date_day_first": False,
}

linde = {
    "rss": False,
    "company_name": "Linde plc",
    "url_press": "https://www.linde.com/news-media",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "",
    "main_id": "main",
    "press_releases": ["article"],
    "press_release_clean": ["div", "p"],
    "press_release_title": ["h5"],
    "press_release_date": ["p"],
    "press_release_date_day_first": False,
}

microsoft = {
    "rss": False,
    "company_name": "Microsoft Corporation",
    "url_press": "https://news.microsoft.com/category/press-releases/",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "",
    "main_id": "content",
    "press_releases": [
        "div",
        "class",
        "m-preview-content",
    ],
    "press_release_clean": [],
    "press_release_title": ["a", "class", "f-post-link c-heading-6 m-chevron"],
    "press_release_date": [
        "div",
        "class",
        "c-paragraph-3 c-meta-text",
    ],
    "press_release_date_day_first": False,
}

netflix = {
    "rss": False,
    "company_name": "Netflix, Inc.",
    "url_press": "https://www.netflixinvestor.com/investor-news-and-events/financial-releases/default.aspx",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "",
    "main_id": "maincontent",
    "press_releases": ["div", "class", "module_item"],
    "press_release_clean": [],
    "press_release_title": ["a", "class", "module_headline-link"],
    "press_release_date": ["span", "class", "module_date-text"],
    "press_release_date_day_first": False,
}

nvidia = {
    "rss": False,
    "company_name": "NVIDIA Corporation",
    "url_press": "https://nvidianews.nvidia.com/news",
    "url_press_prefix_noAcc": "",
    "url_press_prefix_wAcc": "https://nvidianews.nvidia.com",
    "main_id": "page-content",
    "press_releases": ["article", "class", "index-item"],
    "press_release_clean": [
        "div",
        "class",
        "index-item-text-description",
    ],
    "press_release_title": ["h3", "class", "index-item-text-title"],
    "press_release_date": ["span", "class", "index-item-text-info-date"],
    "press_release_date_day_first": False,
}

tesla = {
    "rss": False,
    "company_name": "Tesla, Inc.",
    "url_press": "https://ir.tesla.com/press",
    "url_press_prefix_noAcc": "https://ir.tesla.com",
    "url_press_prefix_wAcc": "https://ir.tesla.com",
    "main_id": "main-content",
    "press_releases": ["section", "class", "press-release-teaser"],
    "press_release_clean": [
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
    "press_release_date_day_first": False,
}

unilever = {
    "rss": False,
    "company_name": "Unilever plc",
    "url_press": "https://www.unilever.com/news/press-releases/",
    "url_press_prefix_noAcc": "https://www.unilever.com",
    "url_press_prefix_wAcc": "https://www.unilever.com",
    "main_id": "grid",
    "press_releases": ["div", "class", "mag__card flex-child"],
    "press_release_clean": [],
    "press_release_title": [
        "span",
        "class",
        "mag__card__content__title mag__card__content__title--pressrelease",
    ],
    "press_release_date": ["span", "class", "mag__card__content__date"],
    "press_release_date_day_first": True,
}
