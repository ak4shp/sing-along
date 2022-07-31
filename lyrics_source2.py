from bs4 import BeautifulSoup as bfs
import requests as rqs

url = " "
response = rqs.get(url)
soup = bfs(response.text, 'lxml')




