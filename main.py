import requests
from fsutils import csv_manager
from requestutils import scrapper
from providers import pages


def main():
    csv_manager.init_csv()

    for url in pages.urls:

        try:
            response = requests.get(url)
            response.raise_for_status()
        except (ValueError, Exception):
            return print("Invalid URL error : " + url)

        url_tag = url.replace("https://chooseparisregion.org", "")
        scrapper.scrap(requests.get(url), url_tag)
    return


# PyCharm IDE bugs this out
# if name == "main":
#    main()
main()
