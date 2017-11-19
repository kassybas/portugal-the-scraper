from bs4 import BeautifulSoup
import os
import urllib.request



url = os.environ['PORTUGAL_URL']

res = urllib.request.urlopen(url).read()
res = res.decode("utf8")
print(res)
soup = BeautifulSoup(res, "html.parser")

ActingAreasBox = soup.find('label',{'for':'ActingAreasBox'}).text
TargetGroupsBox = soup.find('label',{'for':'TargetGroupsBox'}).text

