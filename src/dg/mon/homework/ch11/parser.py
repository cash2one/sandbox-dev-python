import util
from HTMLParser import HTMLParser

class HP(HTMLParser):
    def __init__(self, *args):
        HTMLParser.__init__(self)
        self.links = []
        if args:
            self.urlString = args[0]

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)
        if tag == 'img':
            for name,value in attrs:
                if name == 'src':
                    util.get_img(self.urlString.rsplit('/',1)[0]  + "/" + value)