from typing import Dict

from PythonWebScrapingManager_filomilo.WebsitesModules.Dziennikustawgov.Dziennikustawgov import getDocumentsList, getDocumentsListInWholeSection
from PythonWebScrapingManager_filomilo.WebsitesModules.Dziennikustawgov.DziennikustawgovDataTypes import \
    DziennikustawgovDocument
from feedgen.feed import FeedGenerator




def generateFeedForDziennikustaw(url:str,args):
    if args is None or args.get('multipage') is None or args.get('multipage')!= 'True':
        docsList: list[DziennikustawgovDocument]=getDocumentsList(url)
    else:
        docsList: list[DziennikustawgovDocument] = getDocumentsListInWholeSection(url)

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
