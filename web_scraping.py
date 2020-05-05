# !pip3 install bs4
# import beautifulsoup4
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen

no_pages = 2


def get_data(pageNo: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    url = 'https://www.waterstones.com/books/bestsellers/sort/bestselling/page/'
    r = rq.get(url + pageNo, headers=headers)  # , proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content, 'features="lxml"')
    # print(soup)

    alls = []

    for d in soup.findAll('div',
                          attrs={'class': 'book-preview book-preview-grid-item span3 tablet-span6 mobile-span6'}):
        # print(d)
        name = d.find('a', attrs={'class': 'title link-invert dotdotdot ddd-truncated'})
        n = d.find('img', alt=True)
        if n and len(n.attrs):
            print('> ', n.attrs['alt'])
        author = d.find('div', attrs={'class': 'author'})
        rating = d.find('span', attrs={'class': 'star-rating'})
        price = d.find('span', attrs={'class': 'price'})

        all1 = []

        if name is not None:
            # print(n[0]['alt'])
            all1.append(n[0]['alt'])
        else:
            all1.append("unknown-product")

        if author is not None:
            # print(author.text)
            all1.append(author.text)
        elif author is None:
            author = d.find('span', attrs={'class': 'a-size-small a-color-base'})
            if author is not None:
                all1.append(author.text)
            else:
                all1.append('0')

        if rating is not None:
            # print(rating.text)
            all1.append(rating.text)
        else:
            all1.append('-1')

        if price is not None:
            print('PRICE:', price.text)
            all1.append(price.text)
        else:
            all1.append('0')
        alls.append(all1)
    return alls


results = []
for i in range(1, no_pages + 1):
    results.append(get_data(str(i)))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results), columns=['Book Name', 'Author', 'Rating', 'Price'])
df.to_csv('books.csv', index=False, encoding='utf-8')

df = pd.read_csv("amazon_products.csv")
df.shape
df.head(61)

