from flask import Flask, render_template
import feedparser


app =Flask(__name__)

RSS_FEEDS = {
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    "hollywood": "http://feeds.feedburner.com/thr/news",
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    "screen": "http://screenrant.com/feed/",
    "slash" :"http://feeds2.feedburner.com/slashfilm"
}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    # first_article = feed["entries"][0]
    return render_template("home.html", articles=feed["entries"])

if __name__ == "__main__":
    app.run(port=5000, debug=True)
