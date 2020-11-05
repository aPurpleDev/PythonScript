import bs4
import csv
import requests
from providers import pages


def init_csv():
    with open('./articles.csv', 'w') as csvfile:
        # original delimiter was $
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["title", "body", "tags", "date", "image url", "image alt", "url_tag", "capitalized_tag"])
    return


def create_csv(title, content, tags, date, image_url, image_alt, url_tag, capitalized_tag):
    with open('./articles.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([title, content, tags, date, image_url, image_alt, url_tag, capitalized_tag])
    return


def scrap(response, url_tag):
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    article_title = soup.find("h1", attrs={"class": "h2"})
    article_header = soup.find("p", attrs={"class": "p--excerpt"})
    article_content = soup.find("main", {"class": "container"})
    article_date = soup.find("span", {"class": "single__date"})
    # should only capture first image found
    article_image = soup.find("img")
    div_tags = soup.find("ul", {"class": "single__tags"})

    tags = []
    for tag in div_tags.find_all("a", {"class": "btn btn--round"}):
        tags.append(tag.string)

    tags = '|'.join(tags)
    title = article_title.string
    capitalized_tag = title.title()
    content = str(article_header) + str(article_content)
    content_clean = content.replace('class="h3"', "")
    date = article_date.string
    image_url = article_image["srcset"]
    image_alt = article_image["alt"]

    create_csv(title, content_clean, tags, date, image_url, image_alt, url_tag, capitalized_tag)
    return


def main():
    init_csv()

    for url in pages.urls:
        url_tag = url.replace("https://chooseparisregion.org", "")
        scrap(requests.get(url), url_tag)
    return


# PyCharm IDE bugs this out
# if name == "main":
#    main()
main()
