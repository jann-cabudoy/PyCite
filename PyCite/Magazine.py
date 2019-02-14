from Citation import Citation

class MagazineCitation(Citation):
    """description of class"""

    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, mtitle, issue, pgrng, volume):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.mtitle = mtitle.get()
        self.issue = issue.get()
        self.pgrng = pgrng.get()
        self.volume = volume.get

    def generatecitation(self):
        citation_string = self.authlast + " ," + self.authfirst[0:1] + " (" + self.pubyear + "). " + self.title + ". " + self.mtitle + ", " + self.volume +"(" + self.issue + "), " + "p. " + self.pgrng + "\n" + "\n"
        return citation_string



