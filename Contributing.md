# Contributing

If you like to contribute to *IRNewsFetcher* by adding companies, you will have to follow the instructions below.
Please open a new branch for each company you contribute.

- irnewsfetcher/argparser.py
  - Add the company as an argument to the argparser.
- irnewsfetcher/main.py
  - Add the companies' ticker symbol to the *valid_companies* dictionary.
- irnewsfetcher/pagedata.py
  - "rss": Set the boolean, whether you receive information through an RSS or not. However, RSS is currently not supported. Currently, this has to be always *False*.
  - "company_name": Add the full company name to be displayed.
  - "url_press": Add the main URL of the press releases.
  - "url_press_prefix_noAcc": In case links are only relative paths, include the prefix here. This is only for non-accounting information. If links are non-relative, leave empty.
  - "url_press_prefix_wAcc": In case links are only relative paths, include the prefix here. This is only for accounting information. If links are non-relative, leave empty.
  - "main_id": Add the id of the main HTML-tag that includes all press releases.
  - "press_releases": Add the HTML-tag, -attribute and -attribute-value to select the container of a single press release.
  - "press_release_clean": Add the HTML-tag, -attribute and -attribute-value to select the teaser content of a single press release (no date, no title).
  - "press_release_title": Add the HTML-tag, -attribute and -attribute-value to select the press releases' title.
  - "press_release_date": Add the HTML-tag, -attribute and -attribute-value to select the press releases' date.
  - "press_release_date_day_first": *True* if day in date first (e.g. DD/MM/YYY), *False* if month in date first (e.g. MM/DD/YYY).
  - Add the ticker symbol and the respective dictionary variable to the *company_dict* dictionary.
- README.md: Add the company to the supported companies table.

In case you experience some bugs, you would probably have to fix these in *irnewsfetcher/Company.py*.