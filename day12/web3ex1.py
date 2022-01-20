import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#html全体を取得
soup=BeautifulSoup(res.text,'html.parser')

tds=soup.select('td:first-child')
for td in tds:
    print(td.text)

tds=soup.select('td')
tds=tds[0:len(tds):3]
for td in tds:
    print(td.text)

