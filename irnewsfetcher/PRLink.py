class PRLink(object):
    def __init__(self, company_data, press_release) -> None:
        self.company_data = company_data
        self.link = self.__parse_link(press_release)

    def __parse_link(self, press_release):
        link = None
        if not press_release.find("th"):
            init_link = press_release.find("a")["href"]

            if "earnings" in init_link:
                link = self.company_data["url_press_prefix_wAcc"] + init_link
            else:
                link = self.company_data["url_press_prefix_noAcc"] + init_link

            if link[0] == "/":
                link = self.company_data["url_press_prefix_wAcc"] + link

        return link

    def get_link(self) -> str:
        return self.link