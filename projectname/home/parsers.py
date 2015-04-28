import urllib2
import re

from bs4 import BeautifulSoup


class AgmGroupParser(object):

    def __init__(self):
        self.soup = BeautifulSoup(
            urllib2.urlopen("http://agmgroup.info/news.asp?idx=19")
        )

    def parse(self):
        objects = []
        pattern = re.compile("[A-Z]+ ?", flags=re.IGNORECASE | re.MULTILINE)
        tags = self.soup.findAll("td", {"class": "cc"})

        for tag in tags:
            for e in tag.stripped_strings:
                text = ' '.join(re.findall(pattern, e))
                objects.append({
                    'name': text.title()
                })

        return objects
