import requests
import sys
from bs4 import BeautifulSoup
from wordcloud import WordCloud #한글 분석모듈 wordcloud 모듈
from collections import Counter #빈도수 분석모듈(내장모듈)
from konlpy.tag import Okt #한글 형태소 분석모듈 Opensource Korean text processor
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

##1.브라우저 제어를 위한 객체 생성
print('--1.크롬 브라우저 열기', end='')
driver = webdriver.Chrome('data/chromedriver.exe')
driver.implicitly_wait(10) 
print('완료--')


print('2.수집준비')
#print('1-1)User-Agent 준비')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
headers = {'User-Agent':user_agent, 'Referer': None}
#print('1-2)접속할 url 주소')


content_url = 'https://www.google.com/maps/place/%EC%A0%95%EC%8B%9D%EB%8B%B9/data=!4m7!3m6!1s0x357ca388c5180b2f:0x85313a9c41fe9088!8m2!3d37.5256192!4d127.0410689!9m1!1b1' #정식당


driver.get(content_url)
time.sleep(3)

try :
    WebDriverWait(driver,3).until(lambda drv : drv.find_element_by_css_selector('.aIFcqe'))
except Exception as ex :
    print('네이버 페이지의 소스코드 구성이 변경되어 크롤링이 불가능합니다. >>', ex)
    driver.quit()   #브라우저 닫기
    sys.exit()
#5)스크롤을 맨 아래로 이동
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(3)
#6)BeautifulSoup 객체 생성
soup = BeautifulSoup(driver.page_source, 'html.parser')
#7)상품정보 박스태그 추출
info_list = soup.select('span.wiI7pd')
print('리뷰 태그개수:', len(info_list))


word_list = []
'''
print('2개만 일단 확인')
for item in info_list [:2]:
    print(item.attrs)
    print('-' * 20)
'''
    
for item in info_list:
    word_list.append(item)
    print(word_list) 
  
content_merge = ''
for i, v in enumerate(word_list) :       
    article_str = word_list[i].text.strip()
    content_merge += article_str
    print(content_merge)
    print('-------------------------')
    
print('3. 결합된 문자열 확인')    
print(content_merge)
print('-------------------------') 


#=> konlpy모듈을 사용하여 형태소 분석을 수행한 후, 명사만 추출=>리스트로 추출됨
nlp = Okt() #konlpy객체생성
nouns = nlp.nouns(content_merge) #명사만 리스트로 추출

#단어 100개만 확인
print(nouns[:100])
print(len(nouns))
print('===============================') 
#한글자 명사는 삭제
for i, v in enumerate(nouns) :
    if len(v) < 2 : del(nouns[i])
print(len(nouns))
#지워지지 않은 한글자 있으면 한번 더 삭제
for i, v in enumerate(nouns) :
    if len(v) < 2 : del(nouns[i])
print(len(nouns))


####필요없는 단어는 수동으로 원하는 갯수만큼 삭제####
'''
for n in nouns :
    if '기자' in n :
        nouns.remove(n)
'''      
remove_list = ['식사','위치','관점','지침','대로','코로나','기간','호선','필수','선택','생각','정말','습','집의','음식','과연','확인','무니','저런','하나','메뉴','일단','점심','이야기','시간','가면','때문','일반']

for n in nouns :
    if n in remove_list :
        nouns.remove(n)

print('4. 단어별 빈도수 검사') #=>딕셔너리로 출력됨
count = Counter(nouns)    
print(count)
print('-------------------------') 
print(len(count))    
print('-------------------------')     
print('5. 상위 50건 추출')
#가장 빈도수가 높은 10개단어 추출=>튜플로 구성되어 출력됨
most = count.most_common(50)
print(most) 
print('-------------------------') 
print(len(most))    
print('-------------------------')     

print('6. 워드 클라우드에서 사용하는 딕셔너리 형식으로 변환')
#[('의원', 57), ('관련', 40)] =>{'의원': 57,'관련': 40 }
tags = {}
#unpacking : 파이썬의 튜플속성값을 개별변수에 담음
for n,c in most :   
    tags[n] = c
print(tags)    
print('-------------------------')     

print('7. 워드클라우드 생성')
#워드클라우드 객체생성
wc = WordCloud(font_path='data/NanumBarunGothic.ttf', width=1200, height=600, background_color='white')   
#워드클라우드 그래프 생성 
wc.generate_from_frequencies(tags)    
#파일로 저장
wc.to_file('정식당.png')
#워드 클라우드 출력
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,8))
plt.imshow(wc) #넘파이 배열을 그래프로 출력시켜주는 명령
plt.axis('off')
plt.show()





     