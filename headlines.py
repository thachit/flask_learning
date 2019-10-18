import feedparser
from flask import Flask
from pprint import pprint as p

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"


@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    p(feed)
    first_article = feed['entries'][0]
    return """<html>
                <body>
                <h1> BBC Headlines </h1>
                <b>{0}</b> <br/>
                <i>{1}</i> <br/>Getting Started with Our Headlines Project
                [ 24 ]
                <p>{2}</p> <br/>
                </body>
                </html>""".format(first_article.get("title"), first_article.get("published"),
                                  first_article.get("summary"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
