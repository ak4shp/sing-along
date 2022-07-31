from bs4 import BeautifulSoup as bfs
import requests as rqs

url = " "
response = rqs.get(url)
soup = bfs(response.text, 'lxml')

# Lyrics TITLE
title_header = str(soup.find('h1', class_ = 'title t_over'))
title_str = title_header[32:].split("Lyrics")
title = title_str[0].strip()


