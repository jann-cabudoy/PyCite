class Citation(object):
    """description of class"""

    def __init__(self, authlast, authfirst, title, pubyear):
        self.authlast = str(authlast)
        self.authfirst = str(authfirst)
        self.title = str(title)
        self.pubyear = str(pubyear)

    def getauthlast(self):
        return self.authlast

    def getauthfirst(self):
        return self.authfirst

    def gettitle(self):
        return self.title
    
    def getpubyear(self):
        return self.pubyear


