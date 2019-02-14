from Citation import Citation

class FilmCitation(Citation):
    """description of class"""

    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, origin_country, studio):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.origin_country = origin_country.get()
        self.studio = studio.get()

    def getorigincountry(self):
        return self.origin_country

    def getstudio(self):
        return self.studio