# -*- coding: utf-8 -*-
"""Team-project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AA0s29QrMNbVikMSy-Ytwop-rFIHbMLI
"""

!pip install beautifulsoup4
!pip install requests

chart_f = open("./recent_chart.txt","w")

import requests as rq
from bs4 import BeautifulSoup as bs

req = rq.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')

html = req.text
soup = bs(html,'html.parser')

words=soup.findAll('div',{'class':'tit3'})

from datetime import datetime as dt
time = dt.now()

print('{}'.format(time))
print('NAVER 영화 실시간 랭킹')
for i in range(20):
  print('{0:2d}위:{1}'.format(i+1,words[i].text))

chart_f.close()

# -*- coding: utf-8 -*-
"""Team-project
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1K1YJB4V3-C4vvZqtyNYjF4B67pTAtn61
"""

import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}
url = "https://movie.naver.com/movie/point/af/list.naver"
r = requests.get(url, headers=header)
bs = BeautifulSoup(r.text, "lxml")

trs = bs.select("table.list_netizen > tbody > tr")

for tr in trs:
    tds = tr.select("td")
    if len(tds) == 3:
        title = tds[1]
        movie_title = title.select_one("a.movie").text
        point = title.select_one("div.list_netizen_score > em").text
        for a in title.select("a"):
            a.decompose()
        title.select_one("div").decompose()
        print(movie_title, point, title.text.strip(), sep="\t")
