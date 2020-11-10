import csv
import re


def init_csv():
    with open('./articles.csv', 'w') as csvfile:
        # original delimiter was $
        spamwriter = csv.writer(csvfile, delimiter='$',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["title", "summary", "content", "tags", "date", "image_url", "image_alt",
                             "image_title", "url_tag", "language"])

    with open('./articles_complement.csv', 'w') as csvfile_complement:
        spamwriter_complement = csv.writer(csvfile_complement, delimiter=';',
                                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter_complement.writerow(["tag", "tag_url"])
    return


def create_csv(title, summary, content, tags, date, image_url, image_alt, image_title, url_tag, language,
               categories):
    with open('./articles.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='$',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([title, summary, content, tags, date, image_url, image_alt, image_title, url_tag, language])

    with open('./articles_complement.csv', 'a') as csvfile_complement:
        spamwriter_complement = csv.writer(csvfile_complement, delimiter=';',
                                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for categorie in categories:
            spamwriter_complement.writerow([categorie, "/news/tags/" + re.sub('[^a-zA-Z.-]+', '-', categorie)])
    return
