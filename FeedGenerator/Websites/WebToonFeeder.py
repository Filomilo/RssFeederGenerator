import datetime
from feedgen.feed import FeedGenerator

from FeedGenerator.Websites.PythonWebScrapingManager.WebsitesModules.Webtoon import retiveComicPageInfo
from FeedGenerator.Websites.PythonWebScrapingManager.WebsitesModules.Webtoon.WebtoonDataTypes import WebtoonMainPageInfo

def generateFeedForWebToon(url)->FeedGenerator:
    webToonData: WebtoonMainPageInfo=retiveComicPageInfo(url)
    fg = FeedGenerator()
    fg.title(webToonData.webtoonComicInfo.title)
    fg.description(webToonData.webtoonComicInfo.description)
    fg.link(href=url)

    for page in webToonData.webtoonPageEntries:
        fe= fg.add_entry()
        fe.description(str(page.tx))
        fe.title(page.title)
        fe.link(href=page.url)
        fe.pubDate(page.date)

    return fg
