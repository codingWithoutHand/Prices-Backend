# -*- coding: utf-8 -*-
"""finding_news

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H7pFt4lfKWq0Ed_HrIs74gomJuE6gSVY
"""

import requests
from bs4 import BeautifulSoup
import json
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div.NiLAwe.mi8Lec.gAl5If.jVwmLb.Oc0wGc.R7GTQ.keNKEd.j7vNaf.nID9nc > div > div > article > div > div > a
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div:nth-child(2) > div > article > div > div > a
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div:nth-child(3) > div > article > div > div > a
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div:nth-child(1) > div > div > article > div > div > a
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div.NiLAwe.mi8Lec.gAl5If.jVwmLb.Oc0wGc.R7GTQ.keNKEd.j7vNaf.nID9nc > div > div > article > div > div > a
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div:nth-child(2) > div > article > div > div > a
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div:nth-child(1) > div > article > div > div > a
#main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div:nth-child(2) > div > div > article > div > div > a
def get_news_heads(inp):
    result=[]
    url="https://news.google.com/search?q="+inp+"&hl=ko&gl=KR&ceid=KR%3Ako"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    items = soup.select('div > article > h3 > a')
    for idx, item in enumerate(items): # nth-child 는 nth-of-type 으로 바꾸어줘야 한다.
        publisher = soup.select('main > c-wiz > div.lBwEZb.BL5WZb.GndZbb '
                                '> div:nth-of-type('+str(idx+1)+') > div > article '
                                '> div > div > a') # 해당 idx 출판사 이름을 가져옴

        cu=publisher
        if len(cu) == 0: 
          publisher1 = soup.select('main > c-wiz > div.lBwEZb.BL5WZb.GndZbb '
                                '> div:nth-of-type('+str(idx+1)+') > div > div > article '
                                '> div > div > a') # 해당 idx 출판사 이름을 가져옴
          if len(publisher1) == 0: 
            publisher2 = soup.select('main > c-wiz > div.lBwEZb.BL5WZb.GndZbb > div.NiLAwe.mi8Lec.gAl5If.jVwmLb.Oc0wGc.R7GTQ.keNKEd.j7vNaf.nID9nc > div > div > article > div > div > a') # 해당 idx 출판사 이름을 가져옴
            cu=publisher2
          else:
            cu=publisher1

          
        if len(cu)==0:
          continue
        else:
          publisher=cu
        pub = publisher[0].getText() #뉴스 출판사
        title = item.text #뉴스 헤드라인
        link = 'https://news.google.com'+str(item.get('href')) #뉴스 경로
        
        result.append([pub,title,link])
    return result

a=input("검색어")
b=int(input("최대 뉴스 개수"))
A=get_news_heads(a)
for i in range(min(b,len(A))):
  print("#"*50)
  print("제목 :",A[i][1])
  print("출처 :",A[i][0])
  print("링크 :",A[i][2])



