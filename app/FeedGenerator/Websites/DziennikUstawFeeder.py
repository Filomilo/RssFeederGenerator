from PythonWebScrapingManager_filomilo.WebsitesModules.Dziennikustawgov.Dziennikustawgov import getDocumentsList
from PythonWebScrapingManager_filomilo.WebsitesModules.Dziennikustawgov.DziennikustawgovDataTypes import \
    DziennikustawgovDocument
from feedgen.feed import FeedGenerator




def generateFeedForDziennikustaw(url):
    docsList: list[DziennikustawgovDocument]=getDocumentsList(url)
    fg = FeedGenerator()
    fg.title("Dziennik ustaw")
    fg.description("Dziennik ustaw")
    fg.link(href=url)

    for doc in docsList:
        fe= fg.add_entry()
        fe.description(doc.title)
        fe.title(doc.title)
        fe.link(href=doc.pdfUrl)
        fe.pubDate(doc.date)

    return fg
