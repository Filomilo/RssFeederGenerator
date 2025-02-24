from feedgen.feed import FeedGenerator
def generateFeedForWebToon(url)->FeedGenerator:
    fg = FeedGenerator()
    fg.id('http://lernfunk.de/media/654321')
    fg.title('Some Testfeed')
    fg.author( {'name':'John Doe','email':'john@example.de'} )
    fg.link( href='http://example.com', rel='alternate' )
    fg.logo('http://ex.com/logo.jpg')
    fg.subtitle('This is a cool feed!')
    fg.link( href='http://larskiesow.de/test.atom', rel='self' )
    fg.language('en')
    return fg