import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musicData = soup.select('#body-content > div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr')
for Data in musicData:
    number = Data.select_one('tr > td.number').text[0:2].strip()
    name = Data.select_one('tr > td.info > a.title.ellipsis').text.strip()
    singer = Data.select_one('tr > td.info > a.artist.ellipsis').text.strip()
    print('순위 :',number,'곡 제목 :', name,'가수 :', singer)
    db.musicList1.insert_one({'number' : number , 'name' : name, 'singer' : singer})