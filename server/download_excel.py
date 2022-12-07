from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup

url = "https://www.just.ro/registrul-national-ong"
req = Request(url)
a = urlopen(req).read()
soup = BeautifulSoup(a, 'html.parser')
x = (soup.find_all('a'))

for i in x:
    if str(i).find('href'):
        str1 = str(i).rsplit('href="', 1)

        if len(str1) == 2:
            str2 = str(str1[1]).rsplit('"', 1)[0]

        excel = str(str2).rsplit('" style=', 1)[0]

        if excel.endswith("Asociatii.xlsx"):
            urlretrieve(excel, 'C:/Users/Irina/Desktop/PI/my-app/server/ong.xlsx')
