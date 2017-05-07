# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup

# total index = 22573

data = []
resq = requests.Session() # 雖然名稱同樣叫Session，但是這是 requests 的物件，是專門用來保持網路間連線的！
post_data = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}
resp = resq.post("https://www.ptt.cc/ask/over18", data=post_data)
for i in range(1,500):
    page = 'https://www.ptt.cc/bbs/Gossiping/index' + str(i) + '.html'
    print(page)
    resp = resq.get(page)
    soup = BeautifulSoup(resp.text, "lxml")
    for entry in soup.select('.r-ent'):
        for link in entry.find_all('a'):
            urls = link.get('href')
            content = resq.get("https://www.ptt.cc" + str(urls))
            soup = BeautifulSoup(content.text, "lxml")
            for entry in soup.select('.push'):
                if entry.find('span'):
                    data.append([entry.select('span')[0].text.encode('utf-8'), entry.select('span')[2].text[2:].encode('utf-8'), entry.select('.push-ipdatetime')[0].text.encode('utf-8')])
                   # print entry.select('span')[0].text, entry.select('span')[2].text[2:], entry.select('.push-ipdatetime')[0].text

# print(data)
f = open("mydata.csv","w")
w = csv.writer(f)
w.writerows(data)
f.close()
    
# df.to_csv(file_name, sep='\t', encoding='utf-8')
# 
# resp = resq.get("https://www.ptt.cc/bbs/Gossiping/index1.html")

# # resp = resq.get("https://www.ptt.cc/bbs/Gossiping/M.1481674520.A.251.html")
# soup = BeautifulSoup(resp.text,"html5lib")
# # print(soup)
# for entry in soup.select('.push'):
#     print entry.select('span')[0].text, entry.select('span')[2].text[2:], entry.select('.push-ipdatetime')[0].text

#     for entry in soup.select('.r-ent'):
#         titles = entry.select('.title')[0]
#         print titles.select('a')[0]
#         urls = titles.select('href')
#         print(urls)
