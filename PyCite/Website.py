from Citation import Citation

class WebsiteCitation(object):
    """description of class"""

    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, url):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.url = url.get()

    def geturl(self):
        return self.url
