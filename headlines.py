from flask import Flask, render_template, request
import json
import urllib

import feedparser

app =Flask(__name__)

DEFAULTS = {
    "publication" : "bbc",
    "city" : "London, UK"
}

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=49edf448fe3e52ba925bd5549dc6ffc6"


RSS_FEEDS = {
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    "time": "http://time.com/feed/",
    "ndtv": "http://feeds.feedburner.com/ndtvnews-latest",
    "fortune" : "http://fortune.com/feed/"

}

@app.route("/")
def home():
    publication = request.args.get("publication")
    if not publication:
        publication = DEFAULTS["publication"]
    articles = get_news(publication)
    city = request.args.get("city")
    if not city:
        city = DEFAULTS["city"]
    weather = get_weather(city)
    return render_template("home.html", articles=articles, weather=weather, publication=RSS_FEEDS)


def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS["publication"]
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed["entries"]

def get_weather(query):
    query = urllib.parse.quote(query)
    url = WEATHER_URL.format(query)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":parsed["weather"][0]["description"],"temperature":parsed["main"]["temp"],"city":parsed["name"]
                  }
    return weather




if __name__ == "__main__":
    app.run(port=5000, debug=True)
