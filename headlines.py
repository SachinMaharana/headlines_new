from flask import Flask, render_template
import feedparser


app =Flask(__name__)

RSS_FEEDS = {
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    "hollywood": "http://feeds.feedburner.com/thr/news",
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    "screen": "http://screenrant.com/feed/",
    "slash" :"http://feeds2.feedburner.com/slashfilm",
    "time": "http://time.com/feed/"
}

@app.route("/", methods=["GET", "POST"])
def get_news(publication="bbc"):
    query = request.form.get("publication")
      if not query or query.lower() not in RSS_FEEDS:
          publication = "bbc"
      else:
          publication = query.lower()
      feed = feedparser.parse(RSS_FEEDS[publication])
     return render_template("home.html", articles=feed["entries"], publication=publication)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
