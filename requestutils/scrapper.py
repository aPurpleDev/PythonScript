import bs4
import re
from datetime import datetime
from fsutils import csv_manager


def find_handler(soup, name, attrs = None):
    to_find = None

    if soup is not None:
        try:
            to_find = soup.find(name, attrs)
        except AttributeError as attributeErr:
            print("find_handler:", attributeErr)
        except ValueError as valueErr:
            print("find_handler:", valueErr)

    return to_find


def scrap(response, url_tag):
    if response.status_code != 200:
        csv_manager.create_csv("Status code NOK url" + url_tag, "No data", "No data", "No data", "No data", "No data")
        return

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    article_title = soup.find("h1", attrs={"class": "h2"})
    article_content = soup.find("main", {"class": "container"})
    article_date = soup.find("span", {"class": "single__date"})
    article_image = soup.find("img")
    div_tags = soup.find("ul", {"class": "single__tags"})

    l_tags = find_handler(soup, "ul", attrs={"class": "single__tags"})
    tags = []
    # Change a['href'] url
    for a_html in l_tags.find_all("a", {"class": "btn btn--round"}):
        a_html.string = text = a_html.getText().title()  # Capitalization
        tags.append(text)  # Add tag
        # Convert to url format
        if text is not None:
            text = re.sub(r"\s+", '-', text)
        a_html['href'] = "/news/tags/" + text
    tags = '|'.join(tags)
    title = article_title.string
    article_header = soup.find("p", attrs={"class": "p--excerpt"})
    content = str(article_header) + str(article_content)
    content_clean = content.replace('class="h3"', "")
    date = datetime.strptime(article_date.string, "%B %d, %Y")
    formatted_date = date.strftime("%d %B, %Y")
    language = 'en'

    article_image_url = article_image["src"]

    if article_image["alt"] == "":
        article_image["alt"] = title

    if not article_image.has_attr("title") or article_image["title"] == "":
        article_image["title"] = re.sub('[^a-zA-Z.-]+', '-', title)

    csv_manager.create_csv(title, article_header, content_clean, tags, formatted_date, article_image_url,
                           article_image["alt"], article_image["title"],
                           url_tag, language)
    return
