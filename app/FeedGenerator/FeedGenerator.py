from feedgen.feed import FeedGenerator
from flask import make_response, Response
from urllib.parse import urlparse

from werkzeug.datastructures import ImmutableMultiDict

from .Websites import generateFeedForWebToon
from .Websites.DziennikUstawFeeder import generateFeedForDziennikustaw


def generateFeedResponseForUrl(url:str,args:ImmutableMultiDict[str,str])-> Response:
    domain: str=getDomainFromUrl(url)
    match domain:
        case 'www.webtoons.com':
            fg=generateFeedForWebToon(url=url)
        case 'dziennikustaw.gov.pl':
            fg=generateFeedForDziennikustaw(url=url,args=args)
        case _:
            raise TypeError(f"Unable to handle url [{url}]")
    response= make_response(fg.rss_str())
    response.headers.set('Content-Type', 'application/rss+xml')
    return response


def getDomainFromUrl(url:str)->str:
    domain = urlparse(url).netloc
    return domain