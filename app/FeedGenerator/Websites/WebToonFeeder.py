import datetime

from PythonWebScrapingManager_filomilo.WebsitesModules.Webtoon.Webtoon import retiveComicPageInfo
from PythonWebScrapingManager_filomilo.WebsitesModules.Webtoon.WebtoonDataTypes import WebtoonMainPageInfo
from feedgen.feed import FeedGenerator
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
