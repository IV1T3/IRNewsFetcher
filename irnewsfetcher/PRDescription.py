import bs4


class PRDescription(object):
    def __init__(self, company_data, press_release) -> None:
        self.company_data = company_data
        self.description = self.__parse_description(press_release)

    def __parse_description(self, press_release) -> bs4.BeautifulSoup:
        clean_press_release = []
        pagedata_tag, pagedata_attr, pagedata_attr_val = [], [], []
        no_press_release_teaser = False

        data_press_release_clean = self.company_data["press_release_clean"]

        if len(data_press_release_clean) > 0:
            pagedata_tag = data_press_release_clean[0]

            if len(data_press_release_clean) > 1:
                pagedata_attr = data_press_release_clean[1]

                if len(data_press_release_clean) > 2:
                    pagedata_attr_val = data_press_release_clean[2]

                    clean_press_release = press_release.find(
                        pagedata_tag, {pagedata_attr: pagedata_attr_val}
                    )
                else:
                    clean_press_release = press_release.find(pagedata_tag).find(
                        pagedata_attr
                    )
            else:
                clean_press_release = press_release.find(pagedata_tag)

            no_press_release_teaser = True

        if self.company_data["ticker"] == "tsla":
            clean_press_release = clean_press_release.find_all("div")[2].contents[0]
        elif (
            self.company_data["ticker"] == "nvda"
            or self.company_data["ticker"] == "fb"
            or self.company_data["ticker"] == "lin"
        ):
            clean_press_release = clean_press_release.contents[0]

        if self.company_data["ticker"] == "lin":
            clean_press_release = clean_press_release.split("Linde")[1]
            clean_press_release = "Linde" + clean_press_release

        if no_press_release_teaser:
            clean_press_release = clean_press_release.lstrip().rstrip()

        return clean_press_release

    def get_description(self) -> bs4.BeautifulSoup:
        return self.description