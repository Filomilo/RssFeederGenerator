from flask import Flask,request
from FeedGenerator.FeedGenerator import generateFeedResponseForUrl
app=Flask(__name__)

@app.route("/")
def description():
    return "<p>This is a simple server to collect rss feeds from different websites, supported websites can be found on Github</p>"

@app.route('/feed')
def RssFeedGenerator():
    url: str=request.args.get('url')
    if url is None:
        return "No argument provided"
    try:
        return generateFeedResponseForUrl(url)
    except TypeError as err:
        return f"error occurred: {err}"
    except:
        return "Unknown error occurred"
