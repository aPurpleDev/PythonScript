import csv


def init_csv():
    with open('./articles.csv', 'w') as csvfile:
        # original delimiter was $
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["title", "body", "tags", "date", "image", "url_tag"])
    return


def create_csv(title, content, tags, date, image, url_tag):
    with open('./articles.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([title, content, tags, date, image, url_tag])
    return
