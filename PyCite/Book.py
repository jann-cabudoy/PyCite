from Citation import Citation 


class BookCitation(Citation):
    """description of class"""
    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, pub, city, state):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.pub = pub.get()
        self.city = city.get()
        self.state = state.get()

    def generatecitation(self):
        citation_string = self.authlast + ", " + self.authfirst[0:1] + "." + " (" + self.pubyear + "). " + self.title + ". " + self.city + ", " + self.state + ": " + self.pub + "." + "\n" + "\n"
        return citation_string

