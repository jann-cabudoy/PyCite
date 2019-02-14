from Citation import Citation

class NewspaperCitation(Citation):
    """description of class"""

    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, ntitle, pgrng):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.ntitle = ntitle.get()
        self.pgrng = pgrng.get()

    def generatecitation(self):
        citation_string = self.authlast + " ," + self.authfirst[0:1] + ". (" + self.pubyear + ")." + self.title + "." + self.ntitle + ", p." + self.pgrng + "\n" + "\n"
        return citation_string

