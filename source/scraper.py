import sqlite3
import requests
from bs4 import BeautifulSoup
from random import choice
from datetime import datetime
from time import sleep

# avoids bot rejection
USER_AGENT = "YOUR USER_AGENT"

# loop through article tag in all of the html articles
def parse_article(articles):
    article_store = {}
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text().strip('\n')
        url = a_tag['href']

        # if title is empty, set title to url name and remove dashes
        if title == '':
            title = url[30:-5].replace('-', ' ')
        article_store[title] = url
    return article_store


# database entries and commitments
def database_deposit(articles, sci_topic):
    db_items = []
    # deposits article title, link, and topic, as well as today's date
    # into list of tuples for database parsing
    for k, v in articles.items():
        holder = (k, v, sci_topic, datetime.today())
        db_items.append(holder)

    # opens database connection
    conn = sqlite3.connect("article_data.db")
    c = conn.cursor()
    # deposits values into database via query
    c.executemany("INSERT INTO articles VALUES (?,?,?,?)", db_items)
    conn.commit()
    conn.close()


def pick_article():
    db_articles = []
    # opens database connection to access stored article data
    conn = sqlite3.connect("article_data.db")
    c = conn.cursor()
    # for every query row in the table deposit that row into article list
    for row in c.execute('SELECT title, href, topic FROM articles'):
        db_articles.append(row)

    conn.close()
    # randomly chosen article
    article_choice = choice(db_articles)
    # retrieves title, link, and topic from randomly chosen article
    title, link, topic = article_choice[0], article_choice[1], article_choice[2]

    text_string = f"Good Morning! Your article this week is from {topic}.\nThe title is: {title}. \nHere's " \
                  f"the link: {link} \nHave a terrific day!"

    return text_string


def main():
    headers = {"user-agent": USER_AGENT}
    # news topics that will append to website link
    news_pages = ["space", "nanotech", "physics", "earth", "technology", "chemistry", "biology", "science"]
    topic = choice(news_pages)

    # concatenates random news topic onto url
    url = "https://phys.org/" + topic + "-news/"

    # obtains pure html from request using headers as a mask, sleeps for three seconds prior
    sleep(3)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # finds all of the article tags, parses, and deposits into database
    art = soup.find_all("article")
    article_dict = parse_article(art)
    database_deposit(article_dict, topic)


if __name__ == '__main__':
    main()
