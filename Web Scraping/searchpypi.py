# searchpypi.py - Opens several search results on pypi.org

import sys, webbrowser, requests, bs4

print('Searching...')
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup('res.text', 'parser.html')
link_elems = soup.select('.package-snippet')
