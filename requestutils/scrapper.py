import bs4
from datetime import datetime
from fsutils import csv_manager


def scrap(response, url_tag):
    if response.status_code != 200:
        csv_manager.create_csv("Status code NOK url" + url_tag, "No data", "No data", "No data", "No data", "No data")
        return

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    article_title = soup.find("h1", attrs={"class": "h2"})
    article_header = soup.find("p", attrs={"class": "p--excerpt"})
    article_content = soup.find("main", {"class": "container"})
    article_date = soup.find("span", {"class": "single__date"})
    article_image = soup.find("img")
    div_tags = soup.find("ul", {"class": "single__tags"})

    tags = []
    for tag in div_tags.find_all("a", {"class": "btn btn--round"}):
        tags.append(tag.string)

    tags = '|'.join(tags).title()
    title = article_title.string
    content = str(article_header) + str(article_content)
    content_clean = content.replace('class="h3"', "")
    date = datetime.strptime(article_date.string, "%B %d, %Y")
    formatted_date = date.strftime("%d %B, %Y")

    if article_image["alt"] == "":
        article_image["alt"] = title

    if not article_image.has_attr("title") or article_image["title"] == "":
        article_image["title"] = title

    csv_manager.create_csv(title, content_clean, tags, formatted_date, article_image, url_tag)
    return
