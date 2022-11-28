import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/collection/topselling_paid?clp=ChcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljLCcE4&gsr=ChkKFwoVCg90b3BzZWxsaW5nX3BhaWQQBxgE:S:ANO1ljKn82s&hl=ko&gl=US'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    "Accept-Language" : "ko-KR, ko"
            }

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all("div", attrs={"class":"ULeU3b"})
# print(len(movies))


for movie in movies:
    title = movie.find("div", attrs={'class':'Epkrse'}).get_text()
    print(title)