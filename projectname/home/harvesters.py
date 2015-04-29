import urllib2
import re

from bs4 import BeautifulSoup


class AgmGroupHarvester(object):

    def __init__(self):
        self.soup = BeautifulSoup(
            urllib2.urlopen("http://agmgroup.info/news.asp?idx=19")
        )

    def harvest(self):
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


class NameHarvester(object):

    def __init__(self):
        self.soup = BeautifulSoup(
            urllib2.urlopen(
                "http://simple.wikiquote.org/wiki/List_of_people_by_name")
        )

    def harvest(self):
        objects = []
        div = self.soup.findAll('div', {'id': "mw-content-text"})[0]

        pattern = re.compile("\w*, \w*")
        for tag in div.findAll('a'):
            name = re.findall(pattern, tag.text)
            if name:
                objects.append({
                    'name': name[0],
                })

        return objects


class ManufacturerHarvester(object):

    def __init__(self):
        self.soup = BeautifulSoup(
            urllib2.urlopen(
                "http://en.wikipedia.org/wiki/Category:Auto_parts_suppliers")
        )

    def harvest(self):
        objects = []
        div = self.soup.findAll('div', {'class': 'mw-category-group'})[0]

        for a in div.findAll('a'):
            name = a.text
            if name:
                objects.append({
                    'name': name
                })

        return objects
