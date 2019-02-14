from Citation import Citation

class WebsiteCitation(Citation):
    """description of class"""

    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, url):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.url = url.get()

    def generatecitation(self):
        citation_string = self.authlast + ", " + self.authfirst[0:1] + " (" + self.pubyear + ")." + self.title + "Retrieved from " + self.url + "\n" + "\n"
        return citation_string
