class PRTitle(object):
    def __init__(self, ticker, company_data, press_release) -> None:
        self.ticker = ticker
        self.company_data = company_data
        self.title = self.__parse_title(press_release)

    def __parse_title(self, press_release) -> str:
        data_press_release_title = self.company_data["press_release_title"]

        pagedata_tag = None
        pagedata_index = None
        pagedata_attr = None
        pagedata_attr_val = None
        pagedata_tag_two = None

        if len(data_press_release_title) == 2:
            pagedata_tag = data_press_release_title[0]
            pagedata_index = data_press_release_title[1]
        else:
            if len(data_press_release_title) > 0:
                pagedata_tag = data_press_release_title[0]

                if len(data_press_release_title) > 1:
                    pagedata_attr = data_press_release_title[1]

                    if len(data_press_release_title) > 2:
                        pagedata_attr_val = data_press_release_title[2]

                        if len(data_press_release_title) > 3:
                            pagedata_tag_two = data_press_release_title[3]

        if not press_release.find("th"):
            # Parsing
            if len(data_press_release_title) == 1:
                title = press_release.find(pagedata_tag)
            elif len(data_press_release_title) == 2:
                title = press_release.findAll(pagedata_tag)[pagedata_index]
            elif len(data_press_release_title) > 2:
                title = press_release.find(
                    pagedata_tag, {pagedata_attr: pagedata_attr_val}
                )
            else:
                title = list(press_release)[2]

            if self.ticker == "tsla":
                title = title.find(pagedata_tag_two)
            elif (
                self.ticker == "nvda"
                or self.ticker == "fb"
                or self.ticker == "ilmn"
                or self.ticker == "txn"
            ):
                title = title.find("a")

            if self.ticker == "jnj":
                title = title.contents[1].contents[0]
            elif self.ticker == "goog":
                carriage_index = title.index("\n")
                title = title[:carriage_index] + title[carriage_index + 18 :]
            elif self.ticker == "lin":
                title = title.contents[0].contents[0]
            else:
                title = title.contents[0]

            title = title.lstrip().rstrip()
            title = "".join(list(map(lambda x: " " if x == "\n" else x, title)))

            return title

    def get_title(self) -> str:
        return self.title