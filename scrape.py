from bs4 import BeautifulSoup
import os
import urllib.request
import re



class Element(object):
    def __init__(self, link, name="NA", email="NA", website="NA", area="NA", target="NA", tel="NA", location="NA", municipality="NA", parish="NA"):
        self.link = link 
        self.name = name 
        self.area = area
        self.email = email
        self.website = website
        self.target = target
        self.tel = tel
        self.location = location
        self.municipality = municipality
        self.parish = parish


def get_email():
#    return soup.findAll('a')
    return soup.select_one("a[href*=mail]").text



url = os.environ['PORTUGAL_URL']
#res = urllib.request.urlopen(url+'3548').read()
#res = res.decode("utf8")

res = open('dl.html','r').read()
soup = BeautifulSoup(res, "html.parser")

name = soup.find('p',{'class':'PageTitleTextOpenSans14pxFont'}).text
area = soup.find('input',{'name':'ActingAreasTextarea'}).get('value')
target = soup.find('input',{'name':'ActingAreasTextarea'}).get('value')

website = soup.find('a',{'target':'_blank'})
email = get_email()

tel = soup.find('input',{'name':'Telephone'}).get('value')
location = soup.find('input',{'name':'DistrictName'}).get('value')
municipality = soup.find('input',{'name':'MunicipalityName'}).get('value')
parish = soup.find('input',{'name':'ParishName'}).get('value')



print(name)
