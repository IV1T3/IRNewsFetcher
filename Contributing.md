# Contributing

If you like to contribute to *IRNewsFetcher* by adding companies, you will have to follow the instructions below.
Please open a new branch for each company you contribute.

- irnewsfetcher/argparser.py
  - Add the company as an argument to the argparser.
- irnewsfetcher/pagedata.py
  - create a new dictionary using the companies name as variable
  - "ticker": enter the companies ticker symbol in lowercase letters
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
- irnewsfetcher/main.py
  - Add the ticker symbol and the respective *pagedata* variable to the *company_dict* dictionary.
- README.md: Add the company to the supported companies table.

After having done these steps, it is common that there are still some adjustments to make in either *irnewsfetcher/PRTitle.py* or *irnewsfetcher/PRDescription.py*

## Style Guidelines

- Write code in snake case (e.g. *this_is_a_variable*).
- Class names are to be written in camel case with a leading uppercase character.

