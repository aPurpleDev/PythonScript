import bs4
import csv
import requests

pages = [
    "https://chooseparisregion.org/news/paris-regions-promise-for-sustainable-mobility",
    "https://chooseparisregion.org/news/let-migo-help-you-find-your-way-around-paris-region"
]


def init_csv():
    with open('./articles.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='$',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["title", "body", "tags"])
    return


def create_csv(title, content, tags):
    with open('./articles.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='$',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([title, content, tags])
    return


def scrap(response):
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    article_title = soup.find("h1", attrs={"class": "h2"})
    article_header = soup.find("p", attrs={"class": "p--excerpt"})
    article_content = soup.find("main", {"class": "container"})
    div_tags = soup.find("ul", {"class": "single__tags"})

    tags = []
    for tag in div_tags.find_all("a", {"class": "btn btn--round"}):
        tags.append(tag.string)

    tags = '|'.join(tags)
    title = article_title.string
    content = str(article_header) + str(article_content)

    create_csv(title, content, tags)
    return


def main():
    init_csv()

    for page in pages:
        scrap(requests.get(page))
    return


main()
