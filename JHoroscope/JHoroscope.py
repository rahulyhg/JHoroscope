import urllib.request as urlRequest
import urllib.parse as urlParse
from bs4 import BeautifulSoup
from _datetime import datetime
import json


LINKS = ['https://new.theastrologer.com/daily-horoscope/','https://new.theastrologer.com/mobile/weekly-horoscope/','https://new.theastrologer.com/mobile/yearly-horoscope/',
         'https://new.theastrologer.com/mobile/monthly-horoscope/','https://new.theastrologer.com/']

Zodiac_Names = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']
Horoscopes = {}
class Horoscope:
    def __init__(self):
        self.values = {"q": "python urllib"}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.values = urlParse.urlencode(self.values)
        self.values = self.values.encode("UTF-8")
        link = ""
    def get_by_month(self,zname=Zodiac_Names,json=False):
        targetUrl = urlRequest.Request(url=LINKS[3], data=self.values, headers=self.headers)
        x = urlRequest.urlopen(targetUrl)
        html = x.read()
        soup = BeautifulSoup(html)
        for signs in zname:
            t = soup.find("div", {"id": signs.capitalize() +"Monthly"})
            data = " ".join([line.text for line in t.findAll('p')])
            Horoscopes.update({signs:data})
        if(json):
            return json.dumps(Horoscopes)
        return Horoscopes
    def get_by_year(self,zname=Zodiac_Names,json=False):
        targetUrl = urlRequest.Request(url=LINKS[2], data=self.values, headers=self.headers)
        x = urlRequest.urlopen(targetUrl)
        html = x.read()
        soup = BeautifulSoup(html)
        year = datetime.now().year -1
        for signs in zname:
            t = soup.find("div", {"id": str(signs.capitalize() + str(year))})
            data = " ".join([line.text for line in t.findAll('p')])
            Horoscopes.update({signs:data})
            #print(signs," == ",data)
        if(json):
            return json.dumps(Horoscopes)
        return Horoscopes
    def get_by_week(self,zname=Zodiac_Names,json=False):
        targetUrl = urlRequest.Request(url=LINKS[1], data=self.values, headers=self.headers)
        x = urlRequest.urlopen(targetUrl)
        html = x.read()
        soup = BeautifulSoup(html)
        for signs in zname:
            t = soup.find("div", {"id": signs.capitalize()})
            Horoscopes.update({signs:t.text})
            #print(signs," == ",t.text)
        if(json):
            return json.dumps(Horoscopes)
        return Horoscopes
    def daily_horoscope(self,zname=Zodiac_Names,json=False):
        for sign in zname:
            targetUrl = urlRequest.Request(url=LINKS[4]+sign, data=self.values, headers=self.headers)
            x = urlRequest.urlopen(targetUrl)
            html = x.read()
            soup = BeautifulSoup(html)
            t = soup.find("div", {"id": "today"})
            Horoscopes.update({sign:t.find('p').text})
        if(json):
            return json.dumps(Horoscopes)
        return Horoscopes

