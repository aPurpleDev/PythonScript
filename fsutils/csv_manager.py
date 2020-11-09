import csv


def init_csv():
    with open('./articles.csv', 'w') as csvfile:
        # original delimiter was $
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["title", "summary", "content", "tags", "date", "image_url", "image_alt",
                             "image_title", "url_tag", "language"])
    return


def create_csv(title, summary, content, tags, date, image_url, image_alt, image_title, url_tag, language):
    with open('./articles.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([title, summary, content, tags, date, image_url, image_alt, image_title, url_tag, language])
    return
