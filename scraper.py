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

# opens twilio client api and sends sms message to specified number
def send_message(message):
    # creates client object from twilio account and api auth token
    client = Client(ACCOUNT_ID, AUTH_TOKEN)
    # sends message
    sms = client.messages \
        .create(
        body=message,
        from_='+18312188286',
        to='+14153195470'
    )

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

    art = soup.find_all("article")
    front_page_articles = parse_article(art)
    sms_message = pick_article(front_page_articles)
    send_message(sms_message)


if __name__ == '__main__':
    main()
