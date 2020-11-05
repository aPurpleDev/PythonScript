import bs4
import csv
import requests
import pages


def init_csv():
    with open('./articles.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["title", "body", "tags", "date", "image url"])
    return


def create_csv(title, content, tags, date, image_url):
    with open('./articles.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([title, content, tags, date, image_url])
    return


def scrap(response):
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    article_title = soup.find("h1", attrs={"class": "h2"})
    article_header = soup.find("p", attrs={"class": "p--excerpt"})
    article_content = soup.find("main", {"class": "container"})
    article_date = soup.find("span", {"class": "single__date"})
    # should only capture first image found
    article_image_url = soup.find("img")
    div_tags = soup.find("ul", {"class": "single__tags"})

    tags = []
    for tag in div_tags.find_all("a", {"class": "btn btn--round"}):
        tags.append(tag.string)

    tags = '|'.join(tags)
    title = article_title.string
    content = str(article_header) + str(article_content)
    date = article_date.string
    image_url = article_image_url["srcset"]

    create_csv(title, content, tags, date, image_url)
    return


def main():
    init_csv()

    for page in pages.pages:
        scrap(requests.get(page))
    return


main()
