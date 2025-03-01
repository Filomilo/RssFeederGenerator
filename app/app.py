import logging

from flask import Flask,request

from logging.config import dictConfig

from FeedGenerator.FeedGenerator import generateFeedResponseForUrl

logger=logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)



dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app=Flask(__name__)


@app.route("/")
def description():
    return "<p>This is a simple server to collect rss feeds from different websites, supported websites can be found on Github</p>"

@app.route('/feed')
def RssFeedGenerator():
    url: str=request.args.get('url')
    logger.info(f"request feed for url: {url}")
    if url is None:
        return "No argument provided"
    try:
        return generateFeedResponseForUrl(url,args=request.args)
    except BaseException as err:
        return f"error occurred: {err}"
    except:
        return "Unknown error occurred"
