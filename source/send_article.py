import scraper
import sms


def main():
    # picks article from article database
    sms_message = scraper.pick_article()

    # sends message
    sms.send(sms_message)


if __name__ == "__main__":
    main()
