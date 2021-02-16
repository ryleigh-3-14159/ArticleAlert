import requests
from bs4 import BeautifulSoup
from random import choice
from twilio.rest import Client
from time import sleep

# masks request from site (even though they've given CLEAR access to scraping...)
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# API keys for Twilio
ACCOUNT_ID = "AC45b7c97ab723537ba4c1701d34e516d8"
AUTH_TOKEN = "6deb927e9d0d0c0b6ff1750f1210f2cb"


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

def pick_article(article_store):
    # pick a random article
    article_title, article_link = choice(list(article_store.items()))
    text_string = f"""
    Good Morning! Your article this week is from {topic}, 
    \nthe title is: {article_title}, here's the link: {article_link}
    Have a terrific day!
    """
    return text_string

def main():


if __name__ == '__main__':
    main()
