import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# url 파라미터 pg를 5까지 늘려 250위까지 추출한다
# 화면에는 200위까지 볼 수 있게 해놨지만, page는 5까지 있다.
for page in range(1,6):
    url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg='
    url +=  str(page)

    data = requests.get(url,headers=headers) #request로 url 내 에 있는 내용을 불러온다.
    soup = BeautifulSoup(data.text, 'html.parser') # data 내 html만 parsing 해준다
    songs = soup.select('#body-content > div.newest-list > div > table > tbody> tr') # select를 이용해서, 해당 태그 내 모든 tr들을 불러온다 
    for song in songs:
        # song 안에 내용이 있으면,
        if song is not None:
            rank = song.select_one('td.number') #print(rank)
            unwanted = rank.find('span').extract()                      #원치 않는 span 태그들을 제거해준다.
            rank = rank.text.strip()                                    #text만 추출하기 위한 strip 함수 사용            
            title = song.select_one('td.info>a.title.ellipsis').text.strip() #print(title)
            artist = song.select_one('td.info>a.artist.ellipsis').text.strip() #print(title)
            print(rank, title , artist)
            
#순위 Tag 1,2위 
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number        
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
#제목 Tag
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#가수 Tag
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
