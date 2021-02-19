import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
import sms

# masks request from site (even though they've given CLEAR access to scraping...)
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"


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


def pick_article(article_store, topic):
    # pick a random article
    article_title, article_link = choice(list(article_store.items()))
    text_string = f"Good Morning! Your article this week is from {topic}.\nThe title is: {article_title}. \nHere's " \
                  f"the link: {article_link} \nHave a terrific day!"
    return text_string


# opens twilio client api and sends sms message to specified number
def send_message(message):
    # sends message using attached sms script
    return sms.send(message)


def main():
    headers = {"user-agent": USER_AGENT}
    news_pages = ["space", "nanotech", "physics", "earth", "technology", "chemistry", "biology", "science"]
    topic = choice(news_pages)

    # concatenates random news topic onto url
    URL = "https://phys.org/" + topic + "-news/"

    # obtains pure html from request using headers as a mask, sleeps for three seconds prior
    sleep(3)
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # finds all of the article tags
    art = soup.find_all("article")
    # parses articles on front page
    front_page_articles = parse_article(art)
    # randomly chooses article
    sms_message = pick_article(front_page_articles, topic)
    # sends message
    send_message(sms_message)


if __name__ == '__main__':
    main()
